#The following lab is for cloud computing lab 2 - Q6
import requests
import sqlite3

#create database
db = sqlite3.connect('database2.db')
c = db.cursor()
c.execute('drop table if exists People')
c.execute('create table People(numoffilms int, name TEXT)')

c.execute('drop table if exists Movies')
c.execute('create table Movies(movieNumber INT ,movie TEXT, release_date TEXT)')

listofpeople = []
movielist = []

def movieInfo(record, page):
    movie = record.get('title')
    release_date = record.get('release_date')


    # print(movie)
    # print(release_date)

    sqlInsert6p2 = "insert into Movies values({} ,'{}', '{}')".format(page ,movie, release_date)
    c.execute(sqlInsert6p2)
    db.commit()


def filmsPages():
    numberofRecords = 0
    pageNumber = 1  # for part 1
    while (True):
        # the following loop counts the number of pages.
        # it then counts the number of planets on each page
        url = 'https://swapi.co/api/films/?page='
        url += str(pageNumber)

        page = requests.get(url)
        # get number of records

        for record in page.json().get('results'):
            numberofRecords += 1

            # call specific functions here
            movieInfo(record, pageNumber)  # question 6

        next = page.json().get('next')

        message = page.json().get('next')

        if (message == None):
            break

        pageNumber += 1

def people(record):
     name = record.get('name')
     films = record.get('films')
     numoffilms = int(len(films))


     # print(name)
     # print(films)
     # print(numoffilms)

     list1 = [numoffilms,name,films]




     sqlInsert6 = "insert into People values({}, '{}')".format(numoffilms,name)
     c.execute(sqlInsert6)
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
        people(record) #question 6 part 1
        filmsPages() # question 6 part 2

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1



####################
#q6 - name all people and movies
print('part 1')
# returning the data set for diameter
c.execute("SELECT name, numoffilms from People WHERE numoffilms > 6")
result = c.fetchall()
for row in result:
 print(row)


print('part 2')
c.execute("SELECT DISTINCT movie, min(release_date) from Movies UNION SELECT DISTINCT movie, max(release_date) from Movies")
result = c.fetchall()
for row in result:
 print(row)



