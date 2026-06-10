# Changelog

## 1.2.5

- Exhaustive type hardening across **all** generated modules, replacing the
  per-shape fixture patches (`1.1.0`–`1.2.4`) that only widened one observed
  payload at a time. A post-generation pass in `scripts/build.py` now widens
  two field families everywhere they appear:

  - **File dimensions** — every `thumb_*_{w,h}` (incl. `thumb_pdf_*`,
    `thumb_video_*`) and `original_{w,h}` declared as `str | None` becomes
    `int | str | None`. The Slack file object reference documents these as
    integers; the upstream java-slack-sdk samples carried them as strings.
  - **Block Kit `text` / `title`** — object-only declarations (`Text | None`,
    `Title | None`) become `str | <Object> | None`. rich_text sections and
    third-party app unfurls inline a raw string where the object is expected.

  ~2750 dimension fields and ~1300 text/title fields widened. A regression
  test (`tests/test_type_hardening.py`) asserts no narrow declaration survives
  a regeneration, so the hardening can't silently regress.

## 1.2.4

- `conversations.history` / `conversations.replies`: accept `int` on image
  thumbnail / original dimension fields of **attachment** files —
  `messages[].attachments[].files[].thumb_{360,480,720,800,960,1024}_{w,h}` and
  `original_{w,h}`. Real Slack responses ship these as integers; the model typed
  them as `str`, so channel backfill failed with `Input should be a valid string
  [type=string_type, input_type=int]` (28 errors on a single image attachment)
  and dropped the whole page.

  The `1.2.0`/`1.2.2` fixes widened the same fields on message-level files
  (`messages[].files[]`); files nested under an attachment are a separate
  generated class (`File5` on history, `File4` on replies) that stayed tight.
  Field types change from `str | None` to `int | str | None`. Implemented by
  adding an int-dimension image file under the `attachments[]` entry of the
  existing `file_dimensions.json` fixtures, with values captured from a real
  production payload.

## 1.2.3

- `conversations.history` / `conversations.replies`: accept a raw `str` under
  `messages[].attachments[].blocks[].elements[].text`. Real Slack responses
  ship app-unfurl `context` blocks (e.g. Linear) whose `mrkdwn` elements carry
  `text` as a plain string (`"*State*  Next"`), but the generated model typed
  the attachment-block element `text` as a `Text` object only — so channel
  backfill failed with `Input should be a valid dictionary or instance of Text
  [type=model_type, input_type=str]` and dropped the whole page.

  The `1.1.0` fix widened the message-level element (`messages[].blocks[]`);
  attachment blocks were still tight. Pydantic field type changes from
  `Text | None` to `str | Text | None` for the attachment-block element
  (`Element6` on replies, `Element8` on history). Implemented by adding a
  `linear_unfurl.json` supplementary sample per endpoint, fed into genson in
  `scripts/build.py`, with field values captured from a real production
  payload.

## 1.2.2

- `conversations.history` / `conversations.replies`: accept `int` on two more
  fields that real Slack responses ship as integers —
  `messages[].files[].thumb_pdf_w` / `thumb_pdf_h` (PDF thumbnail dimensions)
  and `messages[].attachments[].ts` (link-unfurl epoch). The `1.2.0` fix only
  covered image thumbnails (`thumb_{360..1024}_{w,h}`, `original_{w,h}`); PDF
  uploads and link unfurls still broke channel backfill with
  `Input should be a valid string [type=string_type, input_type=int]`.

  Pydantic field types change from `str | None` to `int | str | None` for
  `thumb_pdf_w` / `thumb_pdf_h` on the message `File` and from `str | None`
  to `int | str | None` for `Attachment.ts`.

  Implemented by extending the existing `file_dimensions.json` fixtures (one
  per endpoint) fed into genson in `scripts/build.py`, using field values
  captured from real production payloads.

## 1.2.1

- `events-api` `MessagePayload`: accept a raw `str` under
  `event.blocks[].elements[].text`. Slack `context` blocks ship their
  text-object elements as `{"type": "mrkdwn", "text": "<string>", ...}` —
  the `text` is already a plain string, not a nested text object. The
  upstream `java-slack-sdk` samples only carried the object form, so the
  generated Pydantic `Element.text` was typed `Text | None` and rejected
  every real Socket Mode message containing a context block (e.g. `/giphy`
  posts).

  Pydantic field type for `Element.text` in `message_payload` changes from
  `Text | None` to `str | Text | None`.

  Implemented by feeding a repo-owned supplementary fixture
  (`samples/events-api/MessagePayload/giphy_context.json`) into the genson
  schema inference inside `scripts/build.py`. The fixture mirrors a real
  `/giphy` message envelope captured from a production workspace.

## 1.2.0

- `conversations.history` / `conversations.replies`: accept `int` on
  image-file dimension fields under `messages[].files[]` —
  `thumb_{360,480,720,800,960,1024}_{w,h}` and `original_{w,h}`. Real Slack
  responses ship these as integers; the upstream `java-slack-sdk` samples
  only carried the string form, so Pydantic validation rejected every
  message with an image upload.

  Pydantic field types for the relevant File class in each response change
  from `str | None` to `int | str | None`.

  Implemented by feeding two repo-owned supplementary fixtures
  (`samples/web-api/conversations.history/file_dimensions.json`,
  `samples/web-api/conversations.replies/file_dimensions.json`) into the
  genson schema inference inside `scripts/build.py`. The fixtures were
  captured from a real Slack workspace and contain image uploads tall
  enough to trigger every thumbnail breakpoint Slack emits.

## 1.1.0

- `conversations.history` / `conversations.replies`: accept raw strings on
  `messages[].blocks[].elements[].text` (rich_text_section) and on
  `messages[].blocks[].title` (third-party app unfurls — Granola, Claude,
  etc.). Real Slack responses ship both the object and string forms; the
  upstream `java-slack-sdk` samples only carried the object form.

  Pydantic field types for the affected Block Kit container classes change
  from `Text | None` / `Title | None` to `str | Text | None` /
  `str | Title | None`.

  Implemented by feeding repo-owned supplementary fixtures
  (`samples/web-api/conversations.history/`,
  `samples/web-api/conversations.replies/`) into the genson schema inference
  inside `scripts/build.py`. Re-running the generator preserves the
  polymorphism.

- Drop the per-run temp filename from generated module headers
  (`# generated by datamodel-codegen` only) to keep regeneration diffs small.
