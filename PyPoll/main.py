# Import dependencies
import os 
import csv

# Declare and initialize variables
# List for counties
counties_list  = []
# List for all votes
votes_list  = []
# List for distinct candidates
candidates_list  = []

# Map csv file
csvfile = os.path.join("..","datasource","election_data.csv") 

# Open file
with open(csvfile, newline ="") as csvfile:
    # Read file
    csvreader = csv.reader (csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader) 
    # Loop through all rows
    for row in csvreader: 
        counties_list.append(row[1])
        votes_list.append(row[2])
        
      
# The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a 
# Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast
total_votes = len(votes_list)
# A complete list of candidates who received votes
candidates_list = list(set(votes_list))
 
# Create dictionary to store candidate and respective percentage and number of votes.
dictionary = [ {candidate: [votes_list.count(candidate), votes_list.count(candidate)/total_votes * 100]} for candidate in candidates_list ]

print(my_list)
# The total number of votes each candidate won

# The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
