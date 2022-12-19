BEGIN {

	#split("7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",numbers,",")
	split("14,30,18,8,3,10,77,4,48,67,28,38,63,43,62,12,68,88,54,32,17,21,83,64,97,53,24,2,60,96,86,23,20,93,65,34,45,46,42,49,71,9,61,16,31,1,29,40,59,87,95,41,39,27,6,25,19,58,80,81,50,79,73,15,70,37,92,94,7,55,85,98,5,84,99,26,66,57,82,75,22,89,74,36,11,76,56,33,13,72,35,78,47,91,51,44,69,0,90,52",numbers,",")

	board_id=1
	j=0
}

{ 
	if ($0 == "") {
		board_id++ 
		print board_id
		j=0
	} else { 
		j++
		for (i=1;i<=NF;i++) boards[board_id][j][i]=$i
	}
}

END {
	for (number_id=1;number_id<=length(numbers);number_id++) {
		number = numbers[number_id]
		print "=== number " number
		for (board_id=1;board_id<=length(boards);board_id++) {
			print "=== checking board " board_id
			for (j=1;j<=5;j++) {
				for (i=1;i<=5;i++) {
					if (number == boards[board_id][j][i]) {
						print "found " number " on board " board_id
						boards[board_id][j][i] = "x"
						bingo = 0
						for (jj=1;jj<=5;jj++) {
							r = ""
							for (ii=1;ii<=5;ii++) {
								r = r " " boards[board_id][jj][ii]
								if (r == " x x x x x") {
									bingo=1
									print "h bingo!"
								}
							}
							print r
						}

						for (jj=1;jj<=5;jj++) {
							r = ""
							for (ii=1;ii<=5;ii++) {
								r = r " " boards[board_id][ii][jj]
								if (r == " x x x x x") {
									bingo=1
									print "v bingo!"
								}
							}
						}

						if (bingo ==1 ) { 
							total = 0
							for (jj=1;jj<=5;jj++) {
								for (ii=1;ii<=5;ii++) {
									val = boards[board_id][ii][jj]
									if (val != "x") {
										total += val
									} 
								}
							}
							print total*number
							#exit #Part 1

							winning_boards[board_id] = board
							if (length(winning_boards) == length(boards)) {
								print "Part 2"
								print total * number
								exit
							}
						}

					}
				}
			}
		}
	}
}
