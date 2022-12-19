BEGIN {
	FS="";
}

{
	for (i=1; i<=NF; i++) a[i]+=$i;
}


END { 
	for (i=1; i<=NF;i++) if (a[i]>=total) { a[i]=1; b[i]=0 } else { a[i]=0; b[i]=1; }


	for (i=1; i<=NF;i++) gamma=gamma a[i];
	for (i=1; i<=NF;i++) epsilon=epsilon b[i];

	#gamma = system("bc -l <<< 'ibase=2;" gamma "' ") #system call returns exit status code only
	cmd="bc -l <<< 'ibase=2;" epsilon "' "
	cmd | getline gamma_dec
	close(cmd)
	cmd="bc -l <<< 'ibase=2;" gamma "' "
	cmd | getline epsilon_dec
	close(cmd)

	print gamma_dec*epsilon_dec

}

