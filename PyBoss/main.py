import os
import csv

eID = []
fName = []
lName = []
DOB = []
SSN = []
state=[]

#US state abbrev for calling
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open file to read
data = os.path.join('Resources','employee_data.csv')
with open(data) as csvfile:
    empData =csv.reader(csvfile)
    next (empData)
    for row in empData:
        
        #re organizing data into lists
        eID.append(int(row[0]))
        
        #splitting names into two lists
        name = row[1].split(" ")
        fName.append(name[0])
        lName.append(name[1])
        
        #reformatting date
        date = row[2].split("-")
        DOB.append(f'{date[1]}/{date[2]}/{date[0]}')
        
        #reformating Social to be private
        social = row[3].split("-")
        SSN.append("***-**-"+str(social[2]))
        
        #shortening state using dictionary
        state.append(us_state_abbrev[row[4]])

#creating employee dictionary by eID (repeated eID so it can be written into csv)
empDict = {z[0]:list(z[1:]) for z in zip(eID,eID,fName,lName,DOB,SSN,state)}
        
#writing info to a csv file 
outputFile = os.path.join('cleanEmployeeData.csv')
with open(outputFile, 'w', newline = '') as res: 
    empWriter = csv.writer(res, delimiter = ',')
    #header
    empWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    
    #info
    for dat in empDict:
        empWriter.writerow(empDict[dat])

        