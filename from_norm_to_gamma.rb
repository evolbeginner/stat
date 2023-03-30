#! /bin/env ruby


###################################################
require 'getoptlong'

require 'SSW_math'


###################################################
mean = nil
sd = nil
var = nil


###################################################
opts = GetoptLong.new(
  ['--mean', GetoptLong::REQUIRED_ARGUMENT],
  ['--sd', GetoptLong::REQUIRED_ARGUMENT],
  ['--var', GetoptLong::REQUIRED_ARGUMENT],
)

opts.each do |opt, value|
  case opt
    when '--mean'
      mean = value.to_f
    when '--sd'
      sd = value.to_f
    when '--var'
      var = value.to_f
  end
end


###################################################
sd = Math.sqrt(var) unless var.nil?
puts from_norm_to_gamma(mean, sd).join("\t")


