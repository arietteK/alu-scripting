#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flag:(.*?)\]/).map{|match| match.join(",")}.join("\n")
