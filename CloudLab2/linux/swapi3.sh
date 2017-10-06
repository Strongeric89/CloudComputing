#!/bin/bash
url='https://www.swapi.co/api/starships/?page='
END='null'
ARRAY=()
#get value for starship and cargo
function vehicle(){
	echo "-----LIST FROM $1" >> cargo.txt
	x=$(curl $1 | jq '.results[] | {name:.name, cargo:.cargo_capacity}' | jq 'if .cargo == "unknown" then empty else {name:.name,cargo:.cargo | tonumber} end' | jq -s -c 'sort_by(.cargo) | .[] ')
	curl $1 | jq '.results[] | {name:.name, cargo:.cargo_capacity}' | jq 'if .cargo == "unknown" then empty else {name:.name,cargo:.cargo | tonumber} end' | jq -s -c 'sort_by(.cargo) | .[] ' >> cargo.txt

		
let ARRAY=ARRAY
	ARRAY+=(${x})
#	echo $x
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
	vehicle $x 
	num=$((num + 1))
	
	echo $s

done


#for each in "${ARRAY[@]}"
#do
#  echo $each
#done
#echo ${ARRAY[@]}
echo "----CARGO LIST------"
cat cargo.txt
echo "The largest cargo is"
i=$(grep -Eo '[0-9]+' cargo.txt | sort -rn | head -n 1)

grep $i cargo.txt

 
rm cargo.txt

