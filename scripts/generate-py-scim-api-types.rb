#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/py_writer.rb'

class Target
  attr_reader :json_path, :class_name, :output_path

  def initialize(json_path, class_name, output_path)
    @json_path = json_path
    @class_name = class_name
    @output_path = output_path
  end
end

versions = {
  'v1' => [
    Target.new(__dir__ + '/../json/scim-api/v1/Groups.json', 'GroupsResponse', "scim_api/v1/groups_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v1/Users.json', 'UsersResponse', "scim_api/v1/users_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v1/ServiceProviderConfigs.json', 'ServiceProviderConfigsResponse', "scim_api/v1/service_provider_configs_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v1/Users/00000000000.json', 'UserResponse', "scim_api/v1/user_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v1/Groups/00000000000.json', 'GroupResponse', "scim_api/v1/group_response.py"),
  ],
  'v2' => [
    Target.new(__dir__ + '/../json/scim-api/v2/Groups.json', 'GroupsResponse', "scim_api/v2/groups_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v2/Users.json', 'UsersResponse', "scim_api/v2/users_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v2/ServiceProviderConfigs.json', 'ServiceProviderConfigsResponse', "scim_api/v2/service_provider_configs_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v2/ResourceTypes.json', 'ResourceTypesResponse', "scim_api/v2/resource_types_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v2/Users/00000000000.json', 'UserResponse', "scim_api/v2/user_response.py"),
    Target.new(__dir__ + '/../json/scim-api/v2/Groups/00000000000.json', 'GroupResponse', "scim_api/v2/group_response.py"),
  ],
}

versions.each do |version, targets|
  py_writer = PyWriter.new("scim_api/#{version}/__init__.py")
  targets.each do |target|
    File.open(target.json_path) do |json_file|
      input_json = json_file.read
      py_writer.write(target.class_name, target.json_path, target.output_path, input_json)
    end
  end
end
