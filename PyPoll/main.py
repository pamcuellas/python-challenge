# Import dependencies
import os 
import csv

# Declare and initialize variables
# List for all votes
votes  = []
# List for distinct candidates
candidates  = []

# Map csv file
csvfile = os.path.join("..","datasource","election_data_tst.csv") 

# Open file
with open(csvfile, newline ="") as csvfile:
    # Read file
    csvreader = csv.reader (csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader) 
    # Loop through all rows
    for row in csvreader: 
        votes.append(row[2])
        
      
# The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a 
# Python script that analyzes the votes and calculates each of the following:

############################## Printing Election Results on terminal ################################
print("-------------------------------------------------------")
print("{}".format("ELECTION RESULTS:"))
print("-------------------------------------------------------")

# The total number of votes cast
total_votes = len(votes)
print("Total Votes: {}".format(total_votes))
print("-------------------------------------------------------")

# Get a list of distinct candidates
candidates = list(set(votes))

# Create a list of candidate dicionary to store his/her respective percentage and number of votes.
ldict = [ {name: {"percent": votes.count(name)/total_votes * 100, "votes": votes.count(name)}} for name in candidates ]
# Print results for each candidate.
# [ print("{}: {:0.3f}% ({:0,.0f}) ".format(str(candidates[i]), 
#                               ldict[i][candidates[i]]["percent"], 
#                               ldict[i][candidates[i]]["votes"]
#                               )
#         ) for i in range(len(candidates)) 
# ]



[ print("{}: {:0.3f}% ({:0,.0f}) ".format(str(candidates[i]), 
                              ldict[i][candidates[i]]["percent"], 
                              ldict[i][candidates[i]]["votes"]
                              )
        ) for i in range(len(candidates)) 
]
inverse = [(value, key) for key, value in ldict.items()]
print (max(inverse)[1])

# The winner of the election based on popular vote.

print("-------------------------------------------------------")


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
