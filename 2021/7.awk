{
	split($0,input,",")

	cost_min = 10000000000000
	for (dest=1;dest<=1000;dest++) {
		cost = 0
		for (i=1;i<=length(input);i++) {
			if (input[i] > dest) {
				d = input[i] - dest
			}
			else {
				d = dest - input[i]
			}
			#cost += d #Part 1
			cost += d*((1+d)/2)
		}
		if (cost < cost_min) {
			cost_min = cost
			dest_min = dest
		}
	}
	print "dest: " dest_min ", cost: " cost_min
}
