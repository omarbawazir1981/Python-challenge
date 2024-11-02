# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File. """

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0  # Track the total number of months
total_net = 0  # Track the net total amount of "Profit/Losses"

# Add more variables to track other necessary financial data
net_change_list = []  # Track changes in "Profit/Losses"
months = []  # Track each month
greatest_increase = ["", 0]  # Track the greatest increase in profits (month and amount)
greatest_decrease = ["", 0]  # Track the greatest decrease in profits (month and amount)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total number of months
        total_months += 1

        # Track the net total amount of "Profit/Losses"
        total_net += int(row[1])

        # Calculate the monthly change and add it to the list of changes
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        months.append(row[0])
        prev_net = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Calculate the greatest decrease in profits (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
