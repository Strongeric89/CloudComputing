#the following program is for cloud computing lab 2 - q9

"""For   all   people   associated   with   spaceships,
list   their   names,   the spaceships’
names   and   the   cost   of   each   spaceship"""
import requests

listofpeopleandships = []

def shipinfo(url):

    page = requests.get(url)
    info = page.json()
    name = info['name']
    cost = info['cost_in_credits']
    t = (name,cost)
    return t


def peopleandships(record):
    starshipsURL = record.get('starships')

    if(starshipsURL != []):

        name = record.get('name')
        for url in starshipsURL:
            t= shipinfo(url)



        d = {name:t}
        listofpeopleandships.append(d)


numberofRecords = 0
pageNumber = 1 # for part 1
while(True):
    #the following loop counts the number of pages.
    #it then counts the number of planets on each page
    url = 'https://swapi.co/api/people/?page='
    url += str(pageNumber)

    page = requests.get(url)
    #get number of records

    for record in page.json().get('results'):
        numberofRecords += 1

        #call specific functions here
        peopleandships(record)

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1
################################
for item in listofpeopleandships:
    print(item)

