#The following lab is for cloud computing 2
import requests
import sqlite3

# #create database
db = sqlite3.connect('database2.db')
c = db.cursor()

c.execute('drop table if exists Starships')
c.execute('create table Starships(name TEXT, ship TEXT)')

listOfFlyingVehicles = []
listOfStarships = []

def name(record):
    name = record.get('name')
    for n in record.get('name'):

        for s in record.get('starships'):
            if str(s) != '[]':
                # get data from the url of land speeders
                starshipURL = requests.get(s)

                if starshipURL.json().get('name') != 'unknown':
                    # create a dictionary of name and speed
                    d = {starshipURL.json().get('name'): name}
                    # add to list
                    listOfStarships.append(d)

def starships(record, page):
    for s in record.get('starships'):
        if str(s) != '[]':

            #get data from the url of land speeders
            starshipURL = requests.get(s)

            if starshipURL.json().get('cargo_capacity') != 'unknown':
                #create a dictionary of name and speed
                d = {'ship:cargo':(starshipURL.json().get('name'),starshipURL.json().get('cargo_capacity'), page) }
                #add to list
                listOfFlyingVehicles.append(d)


numberofRecords = 0
pageNumber = 1 # for looping through pages

print("Fetching data....")

while(True):
    #the following loop counts the number of pages.
    #it then counts the number of people on each page
    url = 'https://swapi.co/api/people/?page='
    url += str(pageNumber)

    page = requests.get(url)
    #get number of records

    for record in page.json().get('results'):
        numberofRecords += 1


        starships(record, pageNumber) #part 3 and 4
        name(record) # part 4

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1

#part 4
print(listOfStarships)

count = 0
for dict in listOfStarships:
    for key,value in dict.items():
        if value == 'Luke Skywalker' or value == 'Darth Vadar':
            count += 1

            sqlInsert2 = "insert into Starships values('{}', '{}')".format(value,key)
            c.execute(sqlInsert2)

            # print(key)
            # print(value)

print('number of ships:',count)
db.commit()
#returning the data set
c.execute("SELECT DISTINCT ship from Starships")
result = c.fetchall()
for row in result:
    print(row)
