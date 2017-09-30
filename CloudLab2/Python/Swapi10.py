#the following script is for cloud computing lab 2 - question 10
"""What   what   is   the   producer’s   name
who   has   been   involved   the   greatest number   of   films?"""
import requests

listofproducers = []

def producersnames(record):
    producers = record.get('producer')
    title = record.get('title')
    # print(producers)
    # print(title)

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