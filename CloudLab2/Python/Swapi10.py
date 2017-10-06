#the following script is for cloud computing lab 2 - question 10
"""What   what   is   the   producer’s   name
who   has   been   involved   the   greatest number   of   films?"""
import requests
import sqlite3


#create database
db = sqlite3.connect('database2.db')
c = db.cursor()
c.execute('drop table if exists producers')
c.execute('create table producers(producername TEXT)')

listofproducers = []

def producersnames(record):
    producers = record.get('producer')

    title = record.get('title')
    p = producers.split(",")

    for i in p:
        # print(i)
        sqlInsert10 = "insert into producers values('{}')".format(i)
        c.execute(sqlInsert10)
        db.commit()


    t = (producers, title)
    listofproducers.append(t)

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
        producersnames(record)

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1
################################
print(listofproducers)


# returning the data set for number of producers that meet the requirment
c.execute("SELECT  producername, count(producername) from producers group by producername  ORDER BY count(producername) DESC" )
result = c.fetchall()
topProducer = result[0]

print('producer associated with the most movies is:', topProducer[0])

