#!/bin/bash

url='https://www.swapi.co/api/films/?page='
END='null'
ARRAY=()
#get value for number of directors  per movie
function directors(){
#	echo "directors $1" >> directors.txt
	curl $1 | jq '.results[] | {director:.director,film:.title}' >> directors.txt
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
	directors $x
	num=$((num + 1))

	echo $s

done
clear

echo "--------directors per movie"
cat directors.txt

g=$(grep -o 'George Lucas' directors.txt | wc -l)
echo "George Lucas:$g" >> s.txt

r=$(grep -o 'Richard Marquand' directors.txt | wc -l)
echo "Richard Marquand:$r" >> s.txt

v=$(grep -o 'Irvin Kershner' directors.txt | wc -l)
echo "Irvin Kershner:$v" >> s.txt

j=$(grep -o 'J. J. Abrams' directors.txt | wc -l)
echo "J. J. Abrams:$j" >> s.txt

cat s.txt


echo "The director that appears most is:"
y=$(grep -Eo '[0-9]+' s.txt | sort -rn | head -n 1)
cat s.txt | grep $y s.txt 

rm s.txt
rm directors.txt
