#!/bin/bash

url='https://www.swapi.co/api/species/?page='
END='null'
ARRAY=()
#get value for number of species per page
function species(){
#	echo "species $1" >> species.txt
	curl $1 | jq '.results[] | {specie:.classification,numFilms:.films | length} | flatten' >> species.txt

	curl $1 | jq '.results[] | {s:.classification,numFilms:.films |length}'| jq -s -c 'sort_by(.films) | .[] ' >> results.txt
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
	species $x
	num=$((num + 1))

	echo $s

done
clear

echo "--------species per movie"
cat species.txt

m=$(grep -o 'mammal' species.txt | wc -l)
echo "mammal:$m" >> s.txt

g=$(grep -o 'gastropod' species.txt | wc -l)
echo "gastropod:$g" >> s.txt

r=$(grep -o 'reptile' species.txt | wc -l)
echo "reptile:$r" >> s.txt

a=$(grep -o 'amphibian' species.txt | wc -l)
echo "amphibian:$a" >> s.txt

u=$(grep -o 'unknown' species.txt | wc -l)
echo "unknown:$u" >> s.txt

m2=$(grep -o 'mammals' species.txt | wc -l)
echo "mammals:$m2" >> s.txt

i=$(grep -o 'insectoid' species.txt | wc -l)
echo "insectoid:$i" >> s.txt

r2=$(grep -o 'reptilian' species.txt | wc -l)
echo "reptilian:$r2" >> s.txt

 
a2=$(grep -o 'artificial' species.txt | wc -l)
echo "artificial:$a2" >> s.txt

s=$(grep -o 'sentient' species.txt | wc -l)
echo "sentiant:$s" >> s.txt

cat s.txt
rm s.txt

echo "The specie that appears most and second most are:"
y=$(grep -Eo '[0-9]+' results.txt | sort -rn | head -n 1)
cat results.txt | grep $y results.txt 

rm species.txt
rm results.txt
