#! /usr/bin/perl

use 5.010;
use List::Util qw(sum first);
use Statistics::Basic qw(:all);
use Statistics::TTest;
use Statistics::PointEstimation;


####################################
my (@files, @fields);
my ($file1, $file2, $sep, $max, $min);
my $sep="\t";
my $is_next = '';


foreach my $order (0..$#ARGV){
    if ($is_next){
        $is_next = '';
        next;
    }
    my $ele = $ARGV[$order];
    given($ele){
        when (/^-f1$/){
            $fields[0] = $ARGV[$order+1];
            $is_next = 1;
        }
        when (/^-f2$/){
            $fields[1] = $ARGV[$order+1];
            $is_next = 1;
        }
        when (/^--sep$/){
            $sep = $ele;
            $is_next = 1;
        }
        when (/^-?-max$/){
            $max = $ARGV[$order+1];
            $is_next = 1;
        }
        when (/^-?-min$/){
            $min = $ARGV[$order+1];
            $is_next = 1;
        }
        when (/^-.*/){
            &help;
        }
        default{
            push @files, $ele;
        }
    }
}


die "Exactly two files need to be given!" if scalar(@files) != 2;

($file1, $file2) = (@files)[0,1];


foreach (0..1){
    $fields[$_]=1 if not defined $fields[$_];
}


@a1=&read_file($file1, $sep, $fields[0], $max, $min);
@a2=&read_file($file2, $sep, $fields[1], $max, $min);


@a1 = map {chomp;s/\%//g;$_} (@a1);
@a2 = map {chomp;s/\%//g;$_} (@a2);


####################################
$ttest = new Statistics::TTest;
$ttest->set_significance(90);
$ttest->load_data(\@a1,\@a2);
my $prob = $ttest->{t_prob};


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
	my ($in_file, $sep, $field, $max, $min)=@_;
	my @return;
	open(IN,'<',$in_file) || die "infile $infile cannot be opened!";
	while(<IN>){
		chomp;
		my @line = split($sep);
		#my $value = first {$_=~/^-?[.0-9%]+$/} @line;
        my $value = $line[$field-1];
		next if not defined $value;
        next if $value !~ /(\d+\.)?\d/;
        if (defined $max){
            next if $value > $max;
        }
        if (defined $min){
            next if $value < $min;
        }
		push @return,$value;
	}
	return (@return);
}


sub help{
    print "Exiting ......\n";
    exit;
}

