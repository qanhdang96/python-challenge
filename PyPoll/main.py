import os 
import csv 

#Path to collect data from the Resources folder 
csvpath = os.path.join('election_data.csv')

#Define the variables 
total = 0
candidate = []
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
        #Append the candidate to their list 
        candidate.append(row[2])
        
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
            
candidate_votes = [khan_votes, correy_votes, li_votes, tooley_votes]

winner = max(candidate_votes)

# Print out stats for budget data 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total}")
print("----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {tooley_percent:.3f}% ({tooley_votes})")
print("----------------------------")
print(f"Winner: {candidate[winner]}")
print("----------------------------")