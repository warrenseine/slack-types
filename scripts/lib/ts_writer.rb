require 'fileutils'

class TsWriter
  def initialize(index_file)
    @output_prefix_path = __dir__ + '/../../'
    @index_file = @output_prefix_path + index_file

    create_file()
  end

  def write(root_class_name, json_path, typedef_filepath, input_json)
    cmd = "quicktype --just-types --all-properties-optional --acronym-style original -t #{root_class_name} -l ts -o #{@output_prefix_path}#{typedef_filepath}"
    puts "Generating #{root_class_name} from #{json_path}"
    Open3.popen3(cmd) do |stdin, stdout, stderr, wait_thr|
      stdin.write(input_json)
    end
  end

  def append_to_index_ts(root_class_name)
    File.open(@index_file, 'a') do |index_f|
      index_f.puts("export { #{root_class_name} } from './#{root_class_name}';")
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
