#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Modules
import os
import csv

# Lists to store data
change_list = []
months = [] 
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]   
total_change = 0
total_months = 1
net_total= 0

# open the csv file from the local path
csvpath = os.path.join("/Users", "ellenip", "Desktop", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    previous_row = int(first_row[1])
    net_total = int(first_row[1])

# calculate the change in each row
    for row in csvreader:
        net_total +=int (row[1])
        total_months = total_months + 1
        current_value = int(row[1]) 
        change_value = int(current_value - previous_row)
        change_list.append(change_value)
        months.append(row[0])
        previous_row = int(row[1])

# calculate the greatest increase and decrease
        total_change = total_change + change_value 
        if change_value > greatest_increase[1]:
           greatest_increase[0] = str(row[0])
           greatest_increase[1] = change_value

# calculate average change 
        if change_value < greatest_decrease[1]:
           greatest_decrease[0] = str(row[0])
           greatest_decrease[1] = change_value
    
        average_change = total_change/len(months)
   
# create output
analysisSummary = (f"Financial Analysis\n"
                  f"------------------------------\n"
                  f"Total Months: {total_months}\n"
                  f"Total: ${net_total}\n"
                  f"Average Change: ${average_change:.2f}\n"
                  f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
                  f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

                   
# print analysis summary
print(analysisSummary)

# create path to export the analysis summary text file
pathout = os.path.join("/Users", "ellenip", "Desktop", "analysisSummary.txt")
with open(pathout, "w") as txt_file:
    txt_file.write(analysisSummary)


# In[ ]:





# In[ ]:




