#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/ts_writer.rb'

ts_writer = TsWriter.new('audit-api/v1/index.ts')

Dir.glob(__dir__ + '/../json/audit-api/v1/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    root_class_name = ''
    prev_c = nil
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    filename.split('').each do |c|
      if prev_c.nil? || prev_c == '.'
        root_class_name << c.upcase
      elsif c == '.'
        # noop
      else
        root_class_name << c
      end
      prev_c = c
    end
    root_class_name << 'Response'

    typedef_filepath = "audit-api/v1/#{root_class_name}.d.ts"
    input_json = json_file.read
    ts_writer.write(root_class_name, json_path, typedef_filepath, input_json)
    ts_writer.append_to_index_ts(root_class_name)
  end
end