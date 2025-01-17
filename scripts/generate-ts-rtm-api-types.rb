#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/ts_writer.rb'

ts_writer = TsWriter.new('rtm-api/index.ts')

Dir.glob(__dir__ + '/../json/rtm-api/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    root_class_name = filename
    typedef_filepath = "rtm-api/#{root_class_name}.d.ts"
    input_json = json_file.read
    ts_writer.write(root_class_name, json_path, typedef_filepath, input_json)
    ts_writer.append_to_index_ts(root_class_name)
  end
end