# -*- coding: UTF-8 -*-
"""PyBank Homework"""

# Import file 
from pathlib import Path
import csv

csvpath = Path("../PyBank/Resources/budget_data.csv")

# Initiate variables 
total_months = 0 
pnl_total = 0
average_change = 0

# Initiate variable to hold data
months = []
profits = []
increases = []

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Read each row and set values 
    for row in csvreader:
        date = str(row[0])
        months.append(date)
            
        pnl = int(row[1])
        profits.append(pnl)
            
# Calculate total pnl
        pnl_total += pnl

# Calculate total months 
        total_months += 1
    
index = 1
changes = 0
change_increases = []
changes_total = 0
average_change = 0 

for row in profits:
    if index < total_months:
        changes = profits[index]- profits[index-1]      
        index += 1    
        change_increases.append(changes)
        changes_total += changes
        
average_change = changes_total / (total_months-1)
average_change = round(average_change,2)

# Identify greates increase and greates decrease 
greatest_decrease_value = 0
greatest_increase_value = 0 

for changes in change_increases:

    if greatest_decrease_value == 0:
        greatest_decrease_value = changes
    elif changes > greatest_increase_value:
        greatest_increase_value = changes
    elif changes < greatest_decrease_value:
        greatest_decrease_value = changes

# Identify greates increase and greates decrease 
index_month_increase = 0
index_month_decrease = 0

index_month_increase = change_increases.index(greatest_increase_value)
index_month_decrease = change_increases.index(greatest_decrease_value)

greatest_increase_month = months[index_month_increase+1]
greatest_decrease_month = months[index_month_decrease+1]

# Print results to the terminal     
print('Financial Analysis')
print('----------------------------')    
print(f'Total Months: {total_months}')
print(f'Total: ${pnl_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase_value}')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease_value}')

# Create header 
header = ["Total Months", "Total", "Average Change","Greatest Increase in Profits Month","Greatest Increase in Profits $","Greatest Decrease in Profits Month", "Greatest Decrease in Profits $"]

# Create values 
metrics = [total_months, pnl_total, average_change, greatest_increase_month,greatest_increase_value,greatest_decrease_month,greatest_decrease_value]

# Create file for csv file 
output_path = Path('PyBank_Financial_Analysis.csv')

# Export file as csv 
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    csvwriter.writerow(metrics)
    
    