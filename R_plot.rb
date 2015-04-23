#! /bin/env ruby

require 'getoptlong'

infiles=Array.new
outfile=nil
out_prefix=nil
x_label=nil
y_label=nil
Plot=File.expand_path("/home/sswang/tools/self_bao_cun/stat/Plot_ErrorBar.R")


############################################################
opts=GetoptLong.new(
  ['-i', '--in', '--infile', GetoptLong::REQUIRED_ARGUMENT],
  ['-o', '--out', '--outfile', GetoptLong::REQUIRED_ARGUMENT],
  ['-x', '--x_label', GetoptLong::REQUIRED_ARGUMENT],
  ['-y', '--y_label', GetoptLong::REQUIRED_ARGUMENT],
  ['--mode', GetoptLong::REQUIRED_ARGUMENT],
  ['--out_prefix', GetoptLong::REQUIRED_ARGUMENT],
  ['--BoxPlot',GetoptLong::REQUIRED_ARGUMENT],
)

opts.each do |opt,value|
  case opt
    when '-i', '--in', '--infile'
      infiles.push File.expand_path(value)
    when '-o', '--out', '--outfile'
      outfile=value
    when '-x', '--x_label'
      x_label=value
    when '-y', '--y_label'
      y_label=value
    when '--mode'
      mode=value
    when '--outfile'
      outfile=value
    when '--out_prefix'
      out_prefix=value
    when '--BoxPlot'
      BoxPlot=value
  end
end

outfile=outfile.nil? ? (out_prefix+'.pdf') : outfile
raise "outfile not given!" if outfile.nil?


############################################################
infiles_arg=[infiles.join(' '), x_label, y_label].join(' ')
`Rscript #{Plot} #{infiles_arg}`
#dirname=File.dirname BoxPlot
`mv Rplots.pdf #{outfile}`


