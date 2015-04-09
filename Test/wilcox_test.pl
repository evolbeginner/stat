#! /usr/bin/perl

use 5.010;

use Statistics::Test::WilcoxonRankSum;
use List::Util qw(sum first);
#use Statistics::Basic qw(:all);
use Statistics::PointEstimation;
my $wilcox_test = Statistics::Test::WilcoxonRankSum->new();

$file1 = shift @ARGV; #$a1=1;
$file2 = shift @ARGV; #$a2=2;

@a1=&read_file($file1);
@a2=&read_file($file2);

@a1=map {chomp;s/\%//g;$_} (@a1);
@a2=map {chomp;s/\%//g;$_} (@a2);

foreach(\@a1,\@a2){
        $mean = &mean(@$_);
        print $mean."\t";
        }
print "\n";

    $wilcox_test->load_data(\@a1, \@a2);
    my $prob = $wilcox_test->probability();

	print $prob."\n";

################################################
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



