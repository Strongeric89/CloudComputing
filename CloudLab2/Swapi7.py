# this python script is for Q7 -Cloud computing lab 2
#The following lab is for cloud computing lab 2 - Q6


import requests
import sqlite3


#create database
db = sqlite3.connect('database2.db')
c = db.cursor()
c.execute('drop table if exists Specie')
c.execute('create table Specie(specieNum INT)')


listofspecies= []

def findSpecie(index):
    url = 'https://swapi.co/api/species/'
    url += str(index) + '/'

    print(url)
    c = ''
    specie = requests.get(url)
    for record in specie.json().get('name'):
        c += record
    return c

def speciesInfo(record):
    specieURL = record.get('species')

    #just get number from url

    for item in specieURL:
        specieNum = item.split('/')
        # print(specieNum[5])

        sqlInsert7 = "insert into Specie values({})".format(int(specieNum[5]))
        c.execute(sqlInsert7)
        db.commit()


numberofRecords = 0
pageNumber = 1 # for part 1
while(True):
    #the following loop counts the number of pages.
    #it then counts the number of planets on each page
    url = 'https://swapi.co/api/films/?page='
    url += str(pageNumber)

    page = requests.get(url)
    #get number of records

    for record in page.json().get('results'):
        numberofRecords += 1

        #call specific functions here
        speciesInfo(record)

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1



####################
#q6 - get the number for the specie that is second most in a film (ie.. number that appears most second)
print('part 1')
# returning the data set for number of species that meet the requirment
c.execute("SELECT  'Specie ' || specieNum || ' Appeared in ' || count(specieNum) || ' Movies' from Specie group by specieNum having count(specieNum) > 6 ORDER BY count(specieNum)  DESC " )
result = c.fetchall()
for row in result:
 print(row)

print('part 2')
# returning the top species
c.execute("SELECT specieNum from Specie group by specieNum having count(specieNum) > 6 " )
result = c.fetchall()
for row in result:
 # print(row)
 listofspecies.append(row)



index = str(listofspecies[1])
#clean the output
num = index[0]
winner = findSpecie(num)
print('The Specie that appears second most in movies is: ', winner)





