# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 # intialize the total months to 0
total_net = 0    # intialize the total profit / losses to 0

# Add more variables to track other necessary financial data
monthlychanges =[] # intialize the list of monthly net changes
months = []  # initialize the list of months


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstRow = next(reader)
    
    # # increment the count of the total months
    total_months += 1
       
    # Track the net total
    total_net += int(firstRow[1])
    
    # Track the total and net change
    previousProfloss = int(firstRow[1])

    # Process each row of data
    for row in reader:

        # Track the total 
        # # increment the count of the total months
        total_months += 1
       
        # Track the net total
        total_net += int(row[1])
        
        # Track the net change
        netChange = int(row[1]) - previousProfloss
        
        # add on to the list of average changes
        monthlychanges.append(netChange)

        # add the first month that a change occurred
        # months is index 0
        months.append(row[0])

        # update the previous profit & losses
        previousProfloss = int(row[1])

# calculate the average net change per month
averageChangePerMonth = sum(monthlychanges) / len(monthlychanges)

greatestIncrease = [months[0], monthlychanges[0]]  # holds the month and the value of the greatest increase
greatestDecrease = [months[0], monthlychanges[0]]  # holds the month and the value of the greatest decrease
# use this loop to calculate yhe index of the greatest and least monthly changes
for m in range(len(monthlychanges)):      
       
        # Calculate the greatest increase in profits (month and amount)
        if (monthlychanges[m] > greatestIncrease[1]):
              # if the value is greater than the greatest increase, that value becomes the greatest increase
              greatestIncrease[1] = monthlychanges[m]
              # update the month
              greatestIncrease[0] = months[m]
        
        # Calculate the greatest decrease in losses (month and amount)
        if (monthlychanges[m] < greatestDecrease[1]):
              # if the value is less than the greatest decrease, that value becomes the greatest decrease
              greatestDecrease[1] = monthlychanges[m]
              # update the month
              greatestDecrease[0] = months[m]


# Generate the output summary
output = (
    f"\nFinancial Analysis\n\n"
    f"---------------------------------- \n \n"
    f"Total Months : {total_months}\n\n"
    f"Total net : ${total_net}\n\n"
    f"Average Change : ${averageChangePerMonth:.2f} \n\n"
    f"Greatest Increase in Profits:  {greatestIncrease[0]}  (${greatestIncrease[1]}) \n\n"
    f"Greatest Decrease in Profits:  {greatestDecrease[0]}  (${greatestDecrease[1]}) \n\n"
    )


# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
