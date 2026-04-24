# Slack API types

See:
- https://pypi.org/project/slack-types

This npm package is a collection of Python and TypeScript type definition of Slack APIs.

Currently, the package support the following APIs.

* API Methods (web-api)
* Events API (events-api)
* Real Time Messaging API (rtm-api)
* Incoming payloads from Slack Platform (app-backend)
  * Dialogs (dialog_submission, cancellation, suggestion)
  * Interactive Messages (interactive_message, block_action)
  * Message Actions (message_action)
  * Slash Commands

## How to use

For Python (Pydantic v2):
```python
from typing import Callable

# Requirement: install aiohttp
from slack_bolt.async_app import AsyncApp
from slack_sdk.web.async_client import AsyncWebClient
from slack_types.events_api.app_mention_payload import Event as AppMentionEvent

app = AsyncApp()

@app.event("app_mention")
async def handle_mentions(event: dict, client: AsyncWebClient, say: Callable):
    slack_mention = AppMentionEvent.model_validate(event)
    await client.reactions_add(
        channel=slack_mention.channel,
        timestamp=slack_mention.ts,
        name="eyes",
    )
    await say("What's up?")

if __name__ == "__main__":
    app.start(3000)
```

Web API responses expose the same `BaseModel` interface:
```python
from slack_types.web_api.conversations_history_response import ConversationsHistoryResponse

response = await client.conversations_history(channel="C123")
history = ConversationsHistoryResponse.model_validate(response.data)
for message in history.messages or []:
    print(message.ts, message.text)
```

For TypeScript:
```typescript
import * as express from 'express';
import { Express, Request, Response } from 'express';

import * as Slack from '@slack/web-api';
import * as WebApi from 'seratch-slack-types/web-api';
import * as EventsApi from 'seratch-slack-types/events-api';

export const slackApi = new Slack.WebClient(process.env.SLACK_API_TOKEN);

export const app: Express = express();

app.post('/events', function (req: Request, res: Response) {
  const body = JSON.parse(req.body); // still "any" here

  if (body.type === 'url_verification') {
    // url verification
    res.status(200).send(body.event.challenge);

  } else if (body.type === 'event_callback' && body.event.type === 'message') { // still "any" here
    const payload = body as EventsApi.MessagePayload;
    // `payload.event.text` here is typesafe
    slackApi.api.test({ text: payload.event.text })
      .then((response: WebApi.ApiTestResponse) => { // `response` is typesafe
        if (response.ok) {
         // do something here
        } else {
         // do something here
        }
      }).catch(reason => {
        // do something here
      });
  } else {
    // do something here
  }
  res.status(200).json({ message: 'thanks!' });
});
```

## How are the types generated

Input samples come from [java-slack-sdk](https://github.com/slackapi/java-slack-sdk)
(recorded JSON responses). Python models are generated with
[genson](https://github.com/wolverdude/GenSON) (JSON → JSON Schema) piped into
[datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator)
(Schema → Pydantic v2). TypeScript `.d.ts` files are generated with
[quicktype](https://github.com/glideapps/quicktype).

Coverage may not be 100% and some properties may be incorrect. File issues at
https://github.com/warrenseine/slack-types/issues.

To re-generate:

```bash
npm install
npm run build  # clones java-slack-sdk/ on first run
```

Requires `uv` on the `PATH` for the Python pipeline.

## License

The MIT License
