#! /usr/bin/perl

use 5.010;
use List::Util qw(sum first);
use Statistics::Basic qw(:all);
use Statistics::TTest;
use Statistics::PointEstimation;

$file1 = shift @ARGV; #$a1=1;
$file2 = shift @ARGV; #$a2=2;

@a1=&read_file($file1);
@a2=&read_file($file2);


@a1 = map {chomp;s/\%//g;$_} (@a1);
@a2 = map {chomp;s/\%//g;$_} (@a2);

####################################
#$file1 = shift @ARGV;
#$file2 = shift @ARGV;

#open(IN,$file1); @a1=<IN>; close IN;
#open(IN,$file2); @a2=<IN>; close IN;

$ttest = new Statistics::TTest;
$ttest->set_significance(90);
$ttest->load_data(\@a1,\@a2);
my $prob = $ttest->{t_prob};
####################################


foreach(\@a1,\@a2){
	$mean = &mean(@$_);
	print $mean."\t";
	}
print "\n".$prob."\n";


###############################################
sub mean{
	return sum(@_)/@_;
}

sub read_file{
	my ($in_file)=@_;
	my @return;
	open(IN,'<',$in_file);
	while(<IN>){
		chomp;
		my @line=split;
		my $value = first {$_=~/^-?[.0-9%]+$/} @line;
		next if not defined $value;
		push @return,$value;
	}
	return (@return);
}

