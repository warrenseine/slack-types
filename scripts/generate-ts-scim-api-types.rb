#!/usr/bin/env ruby

require 'open3'
require __dir__ + '/lib/ts_writer.rb'

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
    Target.new(__dir__ + '/../json/scim-api/v1/Groups.json', 'GroupsResponse', "scim-api/v1/GroupsResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v1/Users.json', 'UsersResponse', "scim-api/v1/UsersResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v1/ServiceProviderConfigs.json', 'ServiceProviderConfigsResponse', "scim-api/v1/ServiceProviderConfigsResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v1/Users/00000000000.json', 'UserResponse', "scim-api/v1/UserResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v1/Groups/00000000000.json', 'GroupResponse', "scim-api/v1/GroupResponse.d.ts"),
  ],
  'v2' => [
    Target.new(__dir__ + '/../json/scim-api/v2/Groups.json', 'GroupsResponse', "scim-api/v2/GroupsResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v2/Users.json', 'UsersResponse', "scim-api/v2/UsersResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v2/ServiceProviderConfigs.json', 'ServiceProviderConfigsResponse', "scim-api/v2/ServiceProviderConfigsResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v2/ResourceTypes.json', 'ResourceTypesResponse', "scim-api/v2/ResourceTypesResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v2/Users/00000000000.json', 'UserResponse', "scim-api/v2/UserResponse.d.ts"),
    Target.new(__dir__ + '/../json/scim-api/v2/Groups/00000000000.json', 'GroupResponse', "scim-api/v2/GroupResponse.d.ts"),
  ],
}

versions.each do |version, targets|
  ts_writer = TsWriter.new("scim-api/#{version}/index.ts")
  targets.each do |target|
    File.open(target.json_path) do |json_file|
      input_json = json_file.read
      ts_writer.write(target.class_name, target.json_path, target.output_path, input_json)
      ts_writer.append_to_index_ts(target.class_name)
    end
  end
end
