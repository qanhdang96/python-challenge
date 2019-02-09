import os 
import csv

# Path to collect data from the folder 
csvpath = os.path.join('budget_data.csv')

# Define the variables 
months = []
total = [] 
average_change = []

# Read in the CSV file
with open(csvpath, newline='') as budgetdata:

    # Split the data on commas
    csvbudget = csv.reader(budgetdata, delimiter=',')
    next(csvbudget)

    # Loop through the data 
    for row in csvbudget:

        #Append the total months and total net profits to their lists 
        months.append(row[0])
        total.append(int(row[1]))
    
    # Loop through each month to find the monthly average, then add it all up and divide by total months with average
    for i in range (len(total) - 1):
        average_change.append(total[i + 1] - total[i])
        total_average = sum(average_change)/len(average_change)
        
# Find greatest increase and decrease value of average change using max and min 
max_increase = max(average_change)
max_decrease = min(average_change)

# Put the values according to their dates, since the average change value is of the next month we plus one
max_month = average_change.index(max_increase) + 1
min_month = average_change.index(max_decrease) + 1

# Print out stats for budget data 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total)}")
print(f"Average Change: ${round((total_average), 2)}")
print(f"Greatest Increase in Profits: {months[max_month]} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {months[min_month]} (${str(max_decrease)})")

# Export a text file with the results 
file = open('Financial_Analysis.txt','w')
file.write("Financial Analysis" + "\n")
file.write("----------------------------" + "\n")
file.write(f"Total Months: {len(months)}" + "\n")
file.write(f"Total: ${sum(total)}" + "\n")
file.write(f"Average change: ${round(total_average, 2)}" + "\n")
file.write(f"Greatest Increase in Profits: {months[max_month]} (${str(max_increase)})" + "\n")
file.write(f"Greatest Decrease in Profits: {months[min_month]} (${str(max_decrease)})" + "\n")
