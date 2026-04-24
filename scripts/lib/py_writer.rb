require 'fileutils'

class PyWriter
  def initialize(index_file)
    @project_name = "slack_types"
    @output_prefix_path = __dir__ + '/../../python'
    @index_file = "#{@output_prefix_path}/#{@project_name}/#{index_file}"
    @helper = __dir__ + '/py_generate.py'

    create_file()
  end

  def write(root_class_name, json_path, typedef_filepath, input_json)
    output_path = "#{@output_prefix_path}/#{@project_name}/#{typedef_filepath}"
    cmd = [
      'uv', 'run', '--group', 'dev', 'python', @helper,
      '--input', json_path,
      '--output', output_path,
      '--class-name', root_class_name,
    ]
    puts "Generating #{root_class_name} from #{json_path}"
    system(*cmd) || raise("py_generate failed for #{json_path}")
  end

  def create_file()
    dirname = File.dirname(@index_file)
    unless File.directory?(dirname)
      FileUtils.mkdir_p(dirname)
    end
    File.open(@index_file, 'w+') {|file| file.truncate(0) }
  end
end

class String
  def underscore
    self.gsub(/::/, '/').
    gsub(/([A-Z]+)([A-Z][a-z])/,'\1_\2').
    gsub(/([a-z\d])([A-Z])/,'\1_\2').
    tr("-", "_").
    downcase
  end
end
