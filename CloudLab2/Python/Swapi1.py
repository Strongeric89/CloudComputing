#The following lab is for cloud computing 2 - q1
import requests


numberofRecords = 0
pageNumber = 1 # for part 1


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


    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1

    # print(message)
    # print(page)

#part 1
print('The number of pages is:', pageNumber)
print('The number of records is:', numberofRecords)

