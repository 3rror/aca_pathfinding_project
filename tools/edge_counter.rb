#!/usr/bin/env ruby

filename = ARGV.first
edges = 0
nodes = 0

File.foreach(filename) do |line|
  edges += line.split.map(&:to_i).reject(&:zero?).count
  nodes += 1
end

# Separate numbers like "10000" in "10 000"
puts (edges / 2).to_s.gsub(/(\d)(?=(\d\d\d)+(?!\d))/, "\\1 ")
