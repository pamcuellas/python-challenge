# Import dependencies
import os 
import csv
import operator

# Declare and initialize variables
# List for all votes
votes  = []
# Deduplicated list of candidates
candidates  = []
# String to store the winner
winner = ""
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
        votes.append(row[2])
      
############################## Compute Results ################################
# The total number of votes
total_votes = len(votes)
# Get a deduplicated list of candidates.
candidates = list(set(votes))
# Sort the candidates in descending order by votes number
d = { name: votes.count(name) for name in candidates }
sorted  = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# Get the winner name
winner = list(sorted)[0]

############################## Print Election Results on terminal ################################
print("--------------------")
print("ELECTION RESULTS")
print("--------------------")

print(f"Total Votes: {total_votes}")
print("--------------------")

# Print results for each candidate in ranking order.
[print("{}: {:0.3f}% ({:0,.0f}) ".format( name , sorted[name]/total_votes*100, sorted[name])) for name in sorted.keys()]
print("--------------------")

# Print the winner name.
print(f"Winner: {winner}")
print("--------------------")

############################## Exporting results to CSV File ################################
# Map the output file.
output_file = os.path.join("..","datasource","election_results.csv") 

# Dictionary with description(keys) and values.
dic = {"Total Votes": total_votes}
for name in sorted.keys():
    dic[name] = "{:0.3f}% ({:0,.0f}) ".format(sorted[name]/total_votes*100, sorted[name])
dic["Winner"] = winner

# Use zip to create the columns Description and Values.
content = zip (dic.keys(),dic.values())
# Header for the CSV file
header = ["DESCRIPTION", "VALUE"]
# Open the output file
with open(output_file,"w", newline ="") as datafile:
    writer = csv.writer(datafile)
    # Write the header
    writer.writerow(header)
    # Write the content
    writer.writerows(content)

