#!/bin/bash
url='https://www.swapi.co/api/people/?page='
END='null'
#function to countOccurance of names
function countNames(){
	 x=$(curl $1 | jq '.results[].name' | wc -l)
	let count=count+x
	
}
#loop through numbers  until next = null
num=1
s=''
count=0
while true; 
do
	if [ "$s" == "$END"  ];
		then
			break
		fi
	
	x=$url$num
	s=$(curl $x | jq '.next')
	countNames $x $count
	num=$((num + 1))
	
	echo $s

done
echo 'The number of records is'
echo $count

