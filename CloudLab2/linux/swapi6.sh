#!/bin/bash

url='https://www.swapi.co/api/people/?page='
END='null'
ARRAY=()
#get value for planets sorted by diameter
function people(){
#	echo "people $1" >> people.txt
	curl $1 | jq '.results[] | {name:.name,numfilms:.films | length}' | jq -s -c 'sort_by(-.numfilms) | .[0]' >> people.txt	
	#will return the character who was in most movies from each page
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
	people $x
	num=$((num + 1))

	echo $s

done
clear

echo "--------PEOPLE THAT APPEAR MOST IN MOVIES"
cat people.txt

echo "THE CHARACTER THAT APPEARS MOST IS: "
cat people.txt  | head -1
rm people.txt
echo "-----------RELEASE DATES"
curl https://www.swapi.co/api/films/?page=1 | jq '.results[0] | {title:.title,release:.release_date} ' 
curl https://www.swapi.co/api/films/?page=1 | jq '.results[6] | {title:.title,release:.release_date} ' 

