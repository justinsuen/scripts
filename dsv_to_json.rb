### Simple script to parse delimiter separated valued files

def parse_dsv(delim, file)
  lines = file.split("\n")
  lines.map do |line|
    line.to_s.chomp.split(delim, -1)
  end
end

def dsv_to_json(data)
  headers = data[0]
  json = {}
  (1...data.length).each do |row|
    json[row] = {}
    headers.each_with_index do |header, col|
      json[row][header] = data[row][col]
    end
  end
  json
end
