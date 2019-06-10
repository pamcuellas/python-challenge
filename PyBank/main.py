# Import dependencies
import os 
import csv

# Declare and initialize variables
# List for months
months  = []
# List for month values
values  = []
# List for value change between consecutive months 
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
    csvreader = csv.reader (csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader) 
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
        diffs.append(curr_dif_value)

# Remove the first value because there is no variation for the first month.
diffs.pop(0)

############################## print results on terminal ################################
print("-------------------------------------------------------")
print("Results Financial Analysis:")
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
print("Greatest Decrease in losses:  {} (${:0,.2f})".format(greatest_decrease_month, greatest_decrease_value))
print("-------------------------------------------------------")


# As an.a example, your analysis should look similar to the one below:


#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1,926,159)
#   Greatest Decrease in Profits: Sep-2013 ($-2,196,167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.



# print()
# print(greatest_increase_month)
# print(greatest_decrease_value)
# print(greatest_decrease_month)
# print(greatest_decrease_month)
# print (diffs)



# .aloss.aes = [i for i in values if i < 0]
# profit = [i for i in values if i >= 0]
# print(losses)
# print(profit)

# print("--------------------------")
# print(sum(losses)/len(losses))
# print(sum(profit)/len(profit))
# print("--------------------------")
# print(sum(losses)/len(values))
# print(sum(profit)/len(values))
# print("--------------------------")
# print(sum(losses)/len(profit))
# print(sum(profit)/len(losses))
# print("--------------------------")

# print( sum(profit)/sum(losses) )

    # print("Average Change: {:17,.2f}".format(average))