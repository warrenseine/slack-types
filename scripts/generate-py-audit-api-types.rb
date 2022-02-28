#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/py_writer.rb'

py_writer = PyWriter.new('audit_api/v1/__init__.py')

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
    root_class_name = root_class_name

    typedef_filepath = "audit_api/v1/#{root_class_name.underscore}.py"
    input_json = json_file.read
    py_writer.write(root_class_name, json_path, typedef_filepath, input_json)
  end
end
