#! /usr/bin/perl

# Note that the total (instead of the rest) should be behind the first number

use strict;
require chitest;

my (@a, @b, @a2, @b2);
my @argument;
@argument = @ARGV;

@a = @ARGV[0,1];
@b = @ARGV[2,3];

@a = reverse @a if $a[0] > $a[1];
@b = reverse @b if $b[0] > $b[1];

foreach (0..$#argument){
	push @a, $argument[$_] if $_ % 2 == 0;
	push @b, $argument[$_] if $_ % 2 != 0;
}

@a2 = ($a[0], abs($a[1]-$a[0]));
@b2 = ($b[0], abs($b[1]-$b[0]));

print "The proportion of the array is:\t".$a[0]/$a[1]."\n";
print "The proportion of the array is:\t".$b[0]/$b[1]."\n";

my $result = &chitest::chitest([@a2],[@b2],[qw(all)]);
print $result."\n";


