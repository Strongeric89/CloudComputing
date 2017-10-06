#!/bin/bash
url='https://www.swapi.co/api/planets/?page='
END='null'

#get value for planets
function planet(){
	#echo "-----LIST FROM $1" >> planets.txt
	curl $1 | jq '.results[] | {name:.name, numCharacters:.residents | length}' | jq 'if .numCharacters == 0 then empty else {name:.name,num:.numCharacters} end' | jq -s -c 'sort_by(.num) | .[] ' >> planets.txt

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
	planet $x 
	num=$((num + 1))
	
	echo $s

done


echo "----Planet LIST------"
cat planets.txt

echo "The largest amout of characters on a planet is"
i=$(grep -Eo '[0-9]+' planets.txt | sort -rn | head -n 1)

grep $i planets.txt

 
rm planets.txt
