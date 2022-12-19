BEGIN {
	fleet[0]=0
	fleet[1]=0
	fleet[2]=0
	fleet[3]=0
	fleet[4]=0
	fleet[5]=0
	fleet[6]=0
	fleet[7]=0
	fleet[8]=0
	
}

END {
	split($0,input,",")

	for (i=0;i<length(input);i++) {
		fleet[input[i]]++
	}

	for (day=1;day<=256;day++) {
		duplicating=fleet[0]
		fleet[0]=fleet[1]
		fleet[1]=fleet[2]
		fleet[2]=fleet[3]
		fleet[3]=fleet[4]
		fleet[4]=fleet[5]
		fleet[5]=fleet[6]
		fleet[6]=fleet[7]+duplicating
		fleet[7]=fleet[8]
		fleet[8]=duplicating

		l= length(fleet)
		total =0
		for (i=0;i<l-1;i++) {
			total = (total+fleet[i])
		}
		print "After " (day) " days: " total
	}

}
