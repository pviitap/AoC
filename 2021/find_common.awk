BEGIN {
	FS="";
}

{
	for (i=1; i<=NF; i++) a[i]+=$i;
}


END { 
	i=pos;
	if (a[i]>=total) { a[i]=1; b[i]=0 } else { a[i]=0; b[i]=1; }
	print a[i]
}

