#This program populates the number of words in a text file into a hash.
use strict;
use warnings;

my ($fh, $size, $buffer, $word_count);

open($fh, "<", "Datafile.txt") || die("Unable to open the file $@\n");
$size = -s $fh;
read($fh,$buffer,$size);

$buffer =~ s/\s/:/sg;
$buffer =~ s/\.//sg;

my @lines = split(':',$buffer);
foreach my $line (@lines){
	if($line =~ /\w/){
		$word_count->{$line}++;
	} else {
		next;
	}
}
while((my $keys, my $values) = each(%$word_count)){
	print("$keys => $values\n");
}
