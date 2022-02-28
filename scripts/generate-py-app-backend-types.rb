#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/py_writer.rb'

# dialogs
py_writer = PyWriter.new('app_backend/dialogs/__init__.py')

Dir.glob(__dir__ + '/../json/app-backend/dialogs/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    root_class_name = filename
    typedef_filepath = "app_backend/dialogs/#{root_class_name.underscore}.py"
    input_json = json_file.read
    py_writer.write(root_class_name, json_path, typedef_filepath, input_json)
  end
end

# interactive messages
py_writer = PyWriter.new('app_backend/interactive_components/__init__.py')

Dir.glob(__dir__ + '/../json/app-backend/interactive-components/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    root_class_name = filename
    typedef_filepath = "app_backend/interactive_components/#{root_class_name.underscore}.py"
    input_json = json_file.read
    py_writer.write(root_class_name, json_path, typedef_filepath, input_json)
  end
end

# slash commands
py_writer = PyWriter.new('app_backend/slash_commands/__init__.py')

Dir.glob(__dir__ + '/../json/app-backend/slash-commands/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    root_class_name = filename
    typedef_filepath = "app_backend/slash_commands/#{root_class_name.underscore}.py"
    input_json = json_file.read
    py_writer.write(root_class_name, json_path, typedef_filepath, input_json)
  end
end

# views
py_writer = PyWriter.new('app_backend/views/__init__.py')

Dir.glob(__dir__ + '/../json/app-backend/views/*').sort.each do |json_path|
  File.open(json_path) do |json_file|
    filename = json_path.split('/').last.gsub(/\.json$/, '')
    root_class_name = filename
    typedef_filepath = "app_backend/views/#{root_class_name.underscore}.py"
    input_json = json_file.read
    py_writer.write(root_class_name, json_path, typedef_filepath, input_json)
  end
end
