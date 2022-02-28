#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/py_writer.rb'

py_writer = PyWriter.new('rtm_api/__init__.py')

Dir.glob(__dir__ + '/../json/rtm-api/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    root_class_name = filename
    typedef_filepath = "rtm_api/#{root_class_name.underscore}.py"
    input_json = json_file.read
    py_writer.write(root_class_name, json_path, typedef_filepath, input_json)
  end
end