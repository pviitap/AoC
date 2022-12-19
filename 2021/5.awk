BEGIN { 
	FS=" -> "
	width=1000
	height=1000
	for (y=0;y<height;y++) {
		for (x=0;x<width;x++) {
			map[y][x] = "."
		}
	}
}
{
	split($1,line1,",")
	split($2,line2,",")
	x1 = line1[1]
	y1 = line1[2]
	x2 = line2[1]
	y2 = line2[2]
	
	if ((x2-x1) != 0) {
		k = (y2-y1)/(x2-x1)
	} else {
		k = "-"
	}

	if (x1>x2) { xmin=x2; xmax=x1 } else { xmin=x1; xmax=x2  }
	if (y1>y2) { ymin=y2; ymax=y1 } else { ymin=y1; ymax=y2  }

	if (k == 0) {
		y=y1
		for (x=xmin;x<=xmax;x++) {
			#print "x " x "," y
			if (map[y][x] == ".") {
				map[y][x] = 1
			} else {
				map[y][x]++
			}
		}
	} else if (k == "-") {
		x=x1
		for (y=ymin;y<=ymax;y++) {
			#print "x " x "," y
			if (map[y][x] == ".") {
				map[y][x] = 1
			} else {
				map[y][x]++
			}
		}
	#Part 2:
	} else if (k == 1) {
		y = ymin
		for (x=xmin;x<=xmax;x++) {
			if (y<=ymax) {
				#print "x " x "," y
				if (map[y][x] == ".") {
					map[y][x] = 1
				} else {
					map[y][x]++
				}
			}
			y++
		}
	} else if (k == -1) {
		y = ymin
		for (x=xmax;x>=xmin;x--) {
			if (y<=ymax) {
				#print "x " x "," y
				if (map[y][x] == ".") {
					map[y][x] = 1
				} else {
					map[y][x]++
				}
			}
			y++
		}
        } 

}
END {

	points = 0
	for (y=0;y<height;y++) {
		row = ""
		for (x=0;x<width;x++) {
			if (map[y][x] != ".") {
				if (map[y][x] > 1) points++
			}
			row = row map[y][x]
		}
		#print row
	}
	print points
	
}

