require 'fileutils'

class PyWriter
  def initialize(index_file)
    @project_name = "slack_types"
    @output_prefix_path = __dir__ + '/../../python'
    @index_file = "#{@output_prefix_path}/#{@project_name}/#{index_file}"

    create_file()
  end

  def write(root_class_name, json_path, typedef_filepath, input_json)
    cmd = "quicktype --all-properties-optional --nice-property-names --python-version 3.7 -t #{root_class_name} -l python -o #{@output_prefix_path}/#{@project_name}/#{typedef_filepath}"
    puts "Generating #{root_class_name} from #{json_path}"
    Open3.popen3(cmd) do |stdin, stdout, stderr, wait_thr|
      stdin.write(input_json)
    end
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
