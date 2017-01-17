use strict;
use warnings;
use Carp;
#This is a tool used to grep an Ipv4 address

my $ip = <STDIN>;
chomp($ip);

if($ip =~ /(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3})/){
	print("Entered value is in ip-address format\n");
	print("$1\t$2\t$3\t$4\n");
}
else {
	print("Not an ip-address\n");
}
my @values = split(/\./,$ip);
foreach (@values){
	if (($_ >=0) && ($_ <=255)){
		next;
	}
	else{
		die("Not an Ip-address\n");
	}
}
print("entered value is an ip-address\n")
