# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
condidates = []  # list that holds the condidate in the election
condidateVotes = {}  # dictionary that will hold the votes each name
# Winning Candidate and Winning Count Tracker
winningCount = 0  # variable to hold winnig count
winningCondidate = ""  # variable to hold the winnig
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # add on to the total votes
        total_votes += 1


        # If the candidate is not already in the candidate list, add them
        if row[2] not in condidates:

           # Add a vote to the candidate's count
           condidates.append(row[2])
           # Add the value to the dictionary as well
           condidateVotes[row[2]] = 1
        else: 
           # the condidate is in the list of condidates
           # add a vote to the condidate's count
            condidateVotes[row[2]] +=1 


voteOutput = ""
 # Loop through the candidates to determine vote percentages and identify the winner
for condidate in condidateVotes:

        # Get the vote count and calculate the percentage
        votes = condidateVotes.get(condidate) 
        votePercentage = (float(votes) / float(total_votes)) * 100.00
        voteOutput += f"{condidate}:  {votePercentage:.3f}%   ({votes})  \n"

        # compare the votes to the winnig count
        if votes > winningCount:
             # update the votes to be the new winning count
             winningCount = votes
             # update the winning condidate
             winningCondidate = condidate 

winningCondidateOutput = f"winner: {winningCondidate}\n"


# creat the output variable to hold the output
output = (
    f"\nElection Results \n\n"
    f"-------------------------------------------\n\n"
    f"Totale votes: {total_votes}\n\n"
    f"-------------------------------------------\n\n"
    f"{voteOutput}\n"
    f"-------------------------------------------\n\n"
    f"{winningCondidateOutput}"
  )
print(output)
        

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    
   # Write the total vote count to the text file
   txt_file.write(output)

    
    
    
    
   
   
        

