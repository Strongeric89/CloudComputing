#!/bin/bash
rm answer9.txt
rm namesandships.txt
rm url.txt

url='https://www.swapi.co/api/starships/?page='
END='null'
#get value for name and urls of each person associated with starships
function names(){
	curl $1 | jq '.results[] | {name:.name,cost:.cost_in_credits,pilots:[.pilots]}'| jq 'if .pilots == [] then empty else . end'| jq 'flatten' >> namesandships.txt

	grep '.*https://www.swapi.co/api/people/' namesandships.txt >> urls.txt
	
while read URL1
do
        #santitising the url
	u=$(echo $URL1 |tr -d '"' | tr -d ',')
	echo "Looking for People: $u"
#	echo "------------------------"
	
	curl $u | jq '. | {name:.name,ships:[.starships]} ' >> answer9.txt
done < urls.txt	
	curl $1 | jq '.results[] | {name:.name,cost:.cost_in_credits,pilots:[.pilots]}'| jq 'if .pilots == [] then empty else . end' >> answer9.txt
	
#will return the number of species per film
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
	names $x
	num=$((num + 1))

	echo $s

done
clear

rm namesandships.txt
rm urls.txt

cat answer9.txt
rm answer9.txt
