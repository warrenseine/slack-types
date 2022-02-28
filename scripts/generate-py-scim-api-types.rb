#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/py_writer.rb'

py_writer = PyWriter.new('scim_api/v1/__init__.py')

class Target
  attr_reader :json_path, :class_name, :output_path

  def initialize(json_path, class_name, output_path)
    @json_path = json_path
    @class_name = class_name
    @output_path = output_path
  end
end

targets = [
  Target.new(__dir__ + '/../json/scim-api/v1/Groups.json', 'GroupsResponse', "scim_api/v1/groups_response.py"),
  Target.new(__dir__ + '/../json/scim-api/v1/Users.json', 'UsersResponse', "scim_api/v1/users_response.py"),
  Target.new(__dir__ + '/../json/scim-api/v1/ServiceProviderConfigs.json', 'ServiceProviderConfigsResponse', "scim_api/v1/service_provider_configs_response.py"),
  Target.new(__dir__ + '/../json/scim-api/v1/Users/00000000000.json', 'UserResponse', "scim_api/v1/user_response.py"),
  Target.new(__dir__ + '/../json/scim-api/v1/Groups/00000000000.json', 'GroupResponse', "scim_api/v1/group_response.py"),
]
targets.each do |target|
  File.open(target.json_path) do |json_file|
    root_class_name = target.class_name
    typedef_filepath = target.output_path
    input_json = json_file.read
    py_writer.write(root_class_name, target.json_path, typedef_filepath, input_json)
  end
end
