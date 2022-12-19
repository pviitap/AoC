BEGIN { FS="" }
{
	for (i=1;i<=NF;i++) {
		map[NR][i]=$i
	}
}
END {

	rows = length(map)
	cols = length(map[1])
	risk_level = 0
	for (i=1;i<=rows;i++) {
		for (j=1;j<=cols;j++) {
			x=map[i][j]
			if ((x < (map[i][j-1]) || j==1) && 
			    (x < (map[i][j+1]) || j==cols) &&
			    (x < (map[i-1][j]) || i==1) &&
			    (x < (map[i+1][j]) || i==rows)) {
				    risk_level +=1+x
		    	}
		}
	}
	print risk_level
}
