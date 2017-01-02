use strict;
use warnings;

my $emp_database = [
	
		{'id' => 9157,	'name' => 'Sudarsan',	'salary' => 90000},
		{'id' => 9165,	'name' => 'Dhavamani',	'salary' => 95000},
		{'id' => 9257,	'name' => 'Mukesh',	'salary' => 90000},
];

print("***************************************\n");
foreach my $item(@$emp_database){
	foreach my $key (sort keys (%$item)){
		print("$key\t=>\t$item->{$key}\n");
	}
	print("***************************************\n");
}
