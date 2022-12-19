#Part 1
#BEGIN {tmp=0; count=0} 
#
#{ if (NR>1 && $1>tmp) then count++; tmp=$1 }
#
#END { print count }


#Part 2
BEGIN {tmp=0; tmp2=0; tmp3=0; count=0} 
{
	if (NR>3 && ($1+tmp2+tmp) > (tmp3+tmp2+tmp)) {
	       	count++;
	}
	tmp3=tmp2
	tmp2=tmp
	tmp=$1
}

END { print count }
