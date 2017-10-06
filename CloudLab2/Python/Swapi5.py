#The following lab is for cloud computing lab 2 - Q5
import requests
import sqlite3

#create database
db = sqlite3.connect('database2.db')
c = db.cursor()
c.execute('drop table if exists Planets')
c.execute('create table Planets(name TEXT, diameter TEXT, population TEXT)')


diameterPlanets = []
populationPlanets = []
def planets(record):
     name = record.get('name')
     diameter = record.get('diameter')
     population = record.get('population')

     # print(name)
     # print(diameter)
     # print(population)

     sqlInsert5 = "insert into Planets values('{}', '{}', '{}')".format(name,diameter,population)
     c.execute(sqlInsert5)
     db.commit()





numberofRecords = 0
pageNumber = 1 # for part 1
while(True):
    #the following loop counts the number of pages.
    #it then counts the number of planets on each page
    url = 'https://swapi.co/api/planets/?page='
    url += str(pageNumber)

    page = requests.get(url)
    #get number of records

    for record in page.json().get('results'):
        numberofRecords += 1

        #call specific functions here
        planets(record) #question 5

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1



####################
#q5 - name all planets
print('part 1')
# returning the data set for diameter
c.execute("SELECT name, diameter from Planets ORDER BY diameter ASC")
result = c.fetchall()
for row in result:
 print(row)


print('part 2')
# returning the data set for Population
c.execute("SELECT name, population from Planets ORDER BY population DESC")
result = c.fetchall()
for row in result:
 print(row)

