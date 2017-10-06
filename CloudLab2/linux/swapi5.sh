#!/bin/bash

url='https://www.swapi.co/api/planets/?page='
END='null'
ARRAY=()
#get value for planets sorted by diameter
function diameter(){
	echo "planets sorted by diameter $1" >> diameter.txt
	curl $1 | jq '.results[] | {name:.name,diameter:.diameter,population:.population'} | jq 'if .diameter == "unknown" then empty elif .population == "unknown" then empty else {name:.name,diameter:.diameter |tonumber, population:.population |tonumber} end' | jq -s -c 'sort_by(.diameter) | .[] '  >> diameter.txt
	
}

function population(){
        echo "planets sorted by population $1" >> population.txt
	curl $1 | jq '.results[] | {name:.name,diameter:.diameter,population:.population'} | jq 'if .diameter == "unknown" then empty elif .population == "unknown" then empty else {name:.name,diameter:.diameter |tonumber, population:.population |tonumber} end' | jq -s -c 'sort_by(.population) | .[] ' >> population.txt
			
        
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
	diameter $x
	population $x
	num=$((num + 1))

	echo $s

done
clear
echo "------DIAMETER LIST------"
cat diameter.txt
echo "-----POPULATION LIST-----"
cat population.txt 

rm diameter.txt 
rm population.txt
