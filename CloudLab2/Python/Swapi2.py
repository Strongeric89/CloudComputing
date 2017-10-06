#The following lab is for cloud computing 2 - q2
import requests

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

        fastestLandSpeeder(record) #part 2

    next = page.json().get('next')

    message = page.json().get('next')

    if (message == None):
        break

    pageNumber +=1


#part 2
max = 0
for item in listOfLandSpeeders:
    for key,value in item.items():
        number = int(value)

        if(number > max):
            max = number
            s = 'Vehicle: {},\tSpeed:{}'.format(key, value)
print('The fastest land vehicle is: ', s)













