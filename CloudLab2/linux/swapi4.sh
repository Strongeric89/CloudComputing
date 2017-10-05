#!/bin/bash
clear
curl https://www.swapi.co/api/people/?page=1 | jq '.results[] | {name:.name, ship:.starships}' | jq 'if .name == "Luke Skywalker" then {name:.name,ship:.ship} elif .name == "Darth Vader" then {name:.name,ship:.ship} else empty end' | jq '. | {name:.name,ships:.ship | length}'

#cat ships.txt
#rm ships.txt
