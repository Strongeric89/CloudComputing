#!/bin/bash
url='https://www.swapi.co/api/vehicles/?page='
END='null'
ARRAY=()
#get value for vehicle speed

function vehicle(){
	echo "------LAND VEHICLES $1" >> fastestVehicle.txt
	x=$(curl $1 | jq '.results[] | {name:.name, speed:.max_atmosphering_speed}' | jq 'if .speed == "unknown" then empty else {name:.name,speed:.speed | tonumber} end' | jq -s -c 'sort_by(.speed) | .[] ' | tail -1)
	curl $1 | jq '.results[] | {name:.name, speed:.max_atmosphering_speed}' | jq 'if .speed == "unknown" then empty else {name:.name,speed:.speed | tonumber} end' | jq -s -c 'sort_by(.speed) | .[] ' | tail -1 >> fastestVehicle.txt
	
let ARRAY=ARRAY
	ARRAY+=(${x})

}
#loop through numbers  until next = null
num=1
s=''
count=0
while true; 
do	
	x=$url$num
	s=$(curl $x | jq '.next')
	vehicle $x 

	if [ "$s" == "$END"  ];
        	        then
                	        break
                	fi

		num=$((num + 1))	

done


#for each in "${ARRAY[@]}"
#do
#  echo $each
#done

echo "FASTEST VEHICLE LIST"
cat fastestVehicle.txt
echo "The Fastest Vehicle is "
i=$(grep -Eo '[0-9]+' fastestVehicle.txt | sort -rn | head -n 1) 
grep $i fastestVehicle.txt 
rm fastestVehicle.txt
