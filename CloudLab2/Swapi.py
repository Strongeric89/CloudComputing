#The following lab is for cloud computing 2
import requests
import sqlite3

#create database
db = sqlite3.connect('database2.db')
c = db.cursor()
c.execute('drop table if exists FlyingVehicles')
c.execute('create table FlyingVehicles(name TEXT, cargo BIGINT, page int)')

c.execute('drop table if exists Starships')
c.execute('create table Starships(name TEXT, ship TEXT)')



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






def fastestLandSpeeder(record):
    #the following function is used for part 2 to calculate the fastest landspeed vehicle

    # What is the fastest land vehicle part 2
   #get rid of any empty lists
    for v in record.get('vehicles'):
        if str(v) != '[]':

            #get data from the url of land speeders
            landSpeederURL = requests.get(v)

            if landSpeederURL.json().get('vehicle_class') != 'submarine':
                #create a dictionary of name and speed
                d = {landSpeederURL.json().get('name'): landSpeederURL.json().get('max_atmosphering_speed')}
                #add to list
                listOfLandSpeeders.append(d)

numberofRecords = 0
pageNumber = 1 # for part 1
listOfLandSpeeders = []
listOfFlyingVehicles = []
listOfStarships = []

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

        # fastestLandSpeeder(record) #part 1
        # starships(record, pageNumber) #part 2 and 3 and 4
        name(record) # part 4


    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1

    # print(message)
    # print(page)


#part 1
# print('The number of pages is:', pageNumber)
# print('The number of records is:', numberofRecords)
#
#
# #part 2
# max = 0
# for item in listOfLandSpeeders:
#     for key,value in item.items():
#         number = int(value)
#
#         if(number > max):
#             max = number
#             s = 'Vehicle: {},\tSpeed:{}'.format(key, value)
# print('The fastest land vehicle is: ', s)
#
# #part 3
# for dict in listOfFlyingVehicles:
#     for key,value in dict.items():
#       #add to database
#       val = int(value[1])
#       val2 = int(value[2])
#       sqlInsert = "insert into FlyingVehicles values('{}',{},{})".format(value[0], val, val2)
#       c.execute(sqlInsert)
#       #db.commit()
#
#     #returning the data set
#     c.execute("SELECT DISTINCT * from FlyingVehicles ORDER BY page,cargo ASC")
#
#     result = c.fetchall()
#
    # for row in result:
    #     print(row)

#
#
# db.close()

#part 4
# print(listOfStarships)

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















