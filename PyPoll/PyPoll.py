import os
import csv

#Create path to data in SAME PARENT DIRECTORY
csvpath = os.path.join("election_data.csv ")

#Initialize Variables
Total_Votes = 0
Voter_List = []
Vote_Count = []
Index = 0

#open export file
export_poll_file = open("export_file.txt", "w")

#open inport file and read rows
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # This code assumes there are no repeat voters
    for row in csvreader:
        #increase total vote count
        Total_Votes += 1

        #Test if Candidate is in list
            #if in list, update their index with plus one vote
        if row[2] in Voter_List:
            
           Index = Voter_List.index(row[2])
           Vote_Count[Index] = Vote_Count[Index] + 1

            #if not in the list, add name to end of name list
            #update count list with 1 vote at the end
        else:
            Voter_List.append(str(row[2]))
            Index = Voter_List.index(row[2])
            Vote_Count.append(0)
            Vote_Count[Index] = Vote_Count[Index] + 1

#print text and total vote amount
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------")
export_poll_file.write("Election Results\n")
export_poll_file.write("-------------------------\n")
export_poll_file.write("Total Votes: " + str(Total_Votes) +"\n")
export_poll_file.write("-------------------------\n")

#initialize winner variables
Winner = Voter_List[0]
Winner_Votes = Vote_Count[0]

#loop through lists created above to print find winner
for each_element in Voter_List: 
    #find index of current element
    Index = Voter_List.index(each_element)

    #print candidate name, percentage, and total votes recieved
    print(f"{each_element}: {round((100*Vote_Count[Index])/Total_Votes,3)}% {Vote_Count[Index]}")
    export_poll_file.write(str(each_element) + ": " + str(round((100*Vote_Count[Index])/Total_Votes,3)) + "% " +str(Vote_Count[Index]) + "\n")

    #update winner name and votes if array element has more votes 
    if Vote_Count[Index] > Winner_Votes:
        Winner_Votes = Vote_Count[Index] 
        Winner = Voter_List[Index]


#print winner info
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

export_poll_file.write("-------------------------\n")
export_poll_file.write("Winner: " + str(Winner) +"\n")
export_poll_file.write("-------------------------\n")

