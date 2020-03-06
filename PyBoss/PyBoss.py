import os
import csv

#Create path to data in SAME PARENT DIRECTORY
csvpath = os.path.join("employee_data.csv ")

#open export file
emp_file = open("export_file.txt", "w")

#write header line
emp_file.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")

#State Dictionary from web 
#https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
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

#open read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #for each row analyze data
    for row in csvreader:
        #pull out data into managable strings
        Name = row[1]
        DOB = row[2]
        SSN = row[3]
        State = row[4]

        #Split name string into two element list by space delimeter
        #save data in new string
        Name_List = Name.split(" ")
        First_Name = Name_List[0]
        Last_Name = Name_List[1]

        #split DOB into list by dash delimeter
        #write new DOB in correct for
        DOB_List = DOB.split("-")
        DOB = DOB_List[1] + "/" + DOB_List[2] + "/" + DOB_List[0]
        
        #split SSN into list by dash delim
        #save data in correct form
        SSN_List = SSN.split("-")
        SSN = "***-**-" + SSN_List[2]

        #change full state name to abbrev. using dictionary decalared earlier
        State = us_state_abbrev.get(State)

        #write each line into export file in correct form
        emp_file.write(row[0]+","+First_Name+","+Last_Name+","+DOB+","+SSN+","+State+"\n")

#print comeplete message to ensure you don't check file too early
print("Task Completed")
        
        



