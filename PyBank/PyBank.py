import os
import csv

#Create path to data in SAME PARENT DIRECTORY
csvpath = os.path.join("budget_data.csv")

export_bank_file = open("export_file.txt", "w")

#Initialize Variables
Tot_Months = 0
Total_Dollars = 0
Increase_Amt = 0
Increase_Month = ""
Decrease_Amt = 0
Decrease_Month = ""
Prev_Day = 0
Average_Change = 0
First = True



#Open and read data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    #Set values as first row to initialize
    Tot_Months = 0

    for row in csvreader:
        #Ignore first row for averaging
        if First:
            First = False
        else:
            Average_Change = Average_Change + (int(row[1]) - Prev_Day)

        Tot_Months = Tot_Months + 1
        Total_Dollars = Total_Dollars + int(row[1])
        #Average_Change = Average_Change + (int(row[1]) - Prev_Day)
        if (int(row[1]) - Prev_Day) >= Increase_Amt:
            Increase_Amt = (int(row[1]) - Prev_Day)
            Increase_Month = row[0]
        if (int(row[1]) - Prev_Day) <= Decrease_Amt:
            Decrease_Amt = (int(row[1]) - Prev_Day)
            Decrease_Month = row[0]
        Prev_Day = int(row[1])

#print info!
print("")        
print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total Months: {Tot_Months}")
print(f"Total: ${Total_Dollars}")
print(f"Average Change: ${round(Average_Change/(Tot_Months-1),2)}")
print(f"Greatest Increase in Profits: {Increase_Month} (${Increase_Amt})")
print(f"Greatest Decrease in Profits: {Decrease_Month} (${Decrease_Amt})")
print("--------------------------------------------------------")

export_bank_file.write("Financial Analysis\n")
export_bank_file.write("--------------------------------------------------------\n")
export_bank_file.write("Total Months: " + str(Tot_Months) + "\n")
export_bank_file.write("Total: $" + str(Total_Dollars) + "\n")
export_bank_file.write("Average Change: $" + str(round(Average_Change/(Tot_Months-1),2)) + "\n")
export_bank_file.write("Greatest Increase in Profits: " + str(Increase_Month) + " ($" + str(Increase_Amt) + ")\n")
export_bank_file.write("Greatest Increase in Profits: " + str(Decrease_Month) + " ($" + str(Decrease_Amt) + ")\n")
export_bank_file.write("--------------------------------------------------------\n")
