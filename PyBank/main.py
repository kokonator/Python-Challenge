import os
import csv

bud_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(bud_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

   
    # Convert dates and Profit/Loss into a list

    Months = []
    Profit_Loss = []
    for row in csv_reader:
        Months.append(row[0])   
        Profit_Loss.append(int(row[1]))

    # Calculate total months 
    Total_Months = len(Months)

    # Calculate Net Profit
    Net_Profit = sum(Profit_Loss)

    # Calculate and create a list for row to row difference in Profit Loss
    Diff = []
    for i in range (1, len(Profit_Loss)):
        Diff.append(Profit_Loss[i] - Profit_Loss[i-1]) 


    #Calculate avg monthly change in profits
    Avg_Monthly_Change = sum(Diff) / len(Diff)


    #Calcuate Greatest_Increase of month to month change
    Greatest_Inc = max(Diff)
    Greatest_Inc_Date = str(Months[Diff.index(max(Diff))])

    #Calcuate Greatest_Decrease of month to month change
    Greatest_Dec = min(Diff)
    Greatest_Dec_Date = str(Months[Diff.index(min(Diff))])

    #Print Stuff
    print("Financial_Analysis")
    print("-------------------")
    print("Total Months:", Total_Months)
    print("Net_Profit:", "$", Net_Profit)
    print("Average Change:", Avg_Monthly_Change)
    print("Greatest Increase: ", Greatest_Inc_Date, "$", Greatest_Inc)
    print("Greatest Decrease: ", Greatest_Dec_Date, "$", Greatest_Dec)



    
    

    

    
    
      
    
    