#the following program is for cloud computing lab 2 - q8
"""What   is   the   name   and   planet   origin   of   the   species   is   associated   with
the   largest   number   of   characters   (people)?"""



import requests
import sqlite3


#create database
db = sqlite3.connect('database2.db')
c = db.cursor()
c.execute('drop table if exists Homeworld')
c.execute('create table Homeworld(worldid INT)')

def getPlanet(num):
    url = 'https://swapi.co/api/planets/'
    url += str(num) + '/'

    page = requests.get(url)
    for record in page.json().get('name'):
        print(record, end='')



def peopleworlds(record):
    #get peoples homeworlds - return the highest amount of occurance of the homeworld id
    worldURL = record.get('homeworld')
    worldID = worldURL.split('/')
    # print(worldID[5])

    sqlInsert8 = "insert into Homeworld values({})".format(int(worldID[5]))
    c.execute(sqlInsert8)
    db.commit()


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
        peopleworlds(record)

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1



####################
#return planet name and origin who has the largest number of characters
# look at homeworld attribute
print('part 1')

# returning the data set for number of species that meet the requirment
c.execute("SELECT  worldid, count(worldid) from Homeworld group by worldid  ORDER BY count(worldid) DESC" )
result = c.fetchall()
topPlanet = result[0]

print('planet with the most people is:', topPlanet[0])
print('There are {} characters from this planet'.format(topPlanet[1]))
getPlanet(topPlanet[0])
