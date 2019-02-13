import os 
import csv 

#Path to collect data from the folder 
csvpath = os.path.join('election_data.csv')

#Define the variables 
total = 0
candidate_list = []
khan_votes = 0 
correy_votes = 0 
li_votes = 0 
tooley_votes = 0 

# Read in the CSV file
with open(csvpath, newline='') as electiondata:

    # Split the data on commas
    csvreader = csv.reader(electiondata, delimiter=',')
    next(csvreader)
    
    # Loop through the data 
    for row in csvreader:

        #Count the total votes  
        total += 1

        #Append the candidate to their list, we will need this list later to match the election winner
        candidate_list.append(row[2])
        
        # Use Conditionals to find percentage and total votes of each candidate 
        if ("Khan" == row[2]):
            khan_votes += 1
            khan_percent = (khan_votes/total)*100
        elif ("Correy" == row[2]):
            correy_votes += 1
            correy_percent = (correy_votes/total)*100
        elif ("Li" == row[2]):
            li_votes += 1
            li_percent = (li_votes/total)*100
        elif ("O'Tooley" == row[2]): 
            tooley_votes += 1
            tooley_percent = (tooley_votes/total)*100

# Create a list to store all of the candidates' total votes             
candidate_votes = [khan_votes, correy_votes, li_votes, tooley_votes]

# Using max function, we can find the greatest number of votes within candidate votes list 
winner = max(candidate_votes)

# Print out stats for Election data
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total}")
print("----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {tooley_percent:.3f}% ({tooley_votes})")
print("----------------------------")
print(f"Winner: {candidate_list[winner]}")
print("----------------------------")

#Export a text file with the results 
output_path = os.path.join('Election_Result')
with open(output_path, "w", newline="") as txtfile:
    csvwriter = csv.writer(txtfile,delimiter=',')
    csvwriter.writerows([
            ["Election Result"],
            ["----------------------------"],
            [f"Total Votes: {total}"],
            ["----------------------------"],
            [f"Khan: {khan_percent:.3f}% ({khan_votes})"],
            [f"Correy: {correy_percent:.3f}% ({correy_votes})"],
            [f"Li: {li_percent:.3f}% ({li_votes})"],
            [f"O'Tooley: {tooley_percent:.3f}% ({tooley_votes})"],
            ["----------------------------"],
            [f"Winner: {candidate_list[winner]}"],
            ["----------------------------"]])