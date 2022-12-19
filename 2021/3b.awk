BEGIN {
	FS="";
}

{
	if ($pos == filter_a) print $0
}
