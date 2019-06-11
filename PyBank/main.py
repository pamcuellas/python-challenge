# Import dependencies
import os 
import csv

# Declare and initialize variables
# List for months
months  = []
# List for month values
values  = []
# List for the value change between consecutive months 
diffs   = []
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_increase_value = 0
greatest_decrease_value = 0
prev_value  = 0
curr_value  = 0
curr_dif_value = 0 

# Map csv file
csvfile = os.path.join("..","datasource","budget_data.csv") 

# Open file
with open(csvfile, newline ="") as csvfile:
    # Read file
    csvreader = csv.reader (csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader) 
    # Loop through all rows
    for row in csvreader: 
        months.append(row[0])
        curr_value = float(row[1])
        values.append(curr_value)
        curr_dif_value = curr_value - prev_value 
        # Operation to find out the greatest increase and related month.
        if (curr_dif_value > greatest_increase_value):
            greatest_increase_value = curr_dif_value
            greatest_increase_month = row[0]
        # Operation to find out the greatest decrease and related month.
        elif (curr_dif_value < greatest_decrease_value):
            greatest_decrease_value = curr_dif_value
            greatest_decrease_month = row[0]
        # Store the month value for next iteration.
        prev_value = curr_value
        # Store the value change for the current month
        diffs.append(curr_dif_value)

# Remove the first value because there is no variation for the first month.
diffs.pop(0)

############################## printing results on terminal ################################
print("-------------------------------------------------------")
print("Financial Analysis Results:")
print("-------------------------------------------------------")

# The total number of months included in the dataset
total_months = len(months)
print("Total Months: {}".format(total_months))

# The net total amount of "Profit/Losses" over the entire period
total_value = sum(values)
print("Total Value: ${:13,.2f}".format(total_value))

# The average of the changes in "Profit/Losses" over the entire period
average_change = sum(diffs)/len(diffs)
print("Average Change: ${:10,.2f}".format(average_change))

# The greatest increase in profits (monthsnd amount) over the entire period
print("Greatest Increase in Profits: {} (${:13,.2f})".format(greatest_increase_month, greatest_increase_value))

# The greatest decrease in losses (monthsnd amount) over the entire period
print("Greatest Decrease in Losses:  {} (${:0,.2f})".format(greatest_decrease_month, greatest_decrease_value))
print("-------------------------------------------------------")


############################## Exporting results to CSV File ################################
# Map the output file.
output_file = os.path.join("..","datasource","financial_analysis_results.csv") 
# Dictionary with description(keys) and values.
dic = {
    "Total Months": total_months,
    "Total Value": total_value,
    "Average Change": average_change,
    "Month - Greatest Increase in Profits": greatest_increase_month,
    "Value - Greatest Increase in Profits": greatest_increase_value,
    "Month - Greatest Increase in Losses": greatest_decrease_month,
    "Value - Greatest Increase in Losses": greatest_decrease_value
}
# Header for the CSV file
header = ["DESCRIPTION", "VALUE"]
# Use zip to create the columns Description and Values.
content = zip (dic.keys(),dic.values())
# Open the output file
with open(output_file,"w", newline ="") as datafile:
    writer = csv.writer(datafile)
    # Write the header
    writer.writerow(header)
    # Write the content
    writer.writerows(content)
