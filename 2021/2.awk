BEGIN { h=0; d=0; a=0 }
{ if ($1=="forward") { h+=$2; d+=a*$2 } }
{ if ($1=="up") a-=$2 }
{ if ($1=="down") a+=$2 }
END { print h*d }
