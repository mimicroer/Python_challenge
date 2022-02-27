#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Modules
import os
import csv

# Lists to store data
candidates = {}

# open the csv file from the local path
csvpath = os.path.join("/Users", "ellenip", "Desktop", "election_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# find out how many votes for each candidate
    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        total = candidates.values()
        total_votes = sum(total)
    
        list_candidates = candidates.keys()

        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
            
# find out who is the winner
        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        
# create path to export the output text file
f = open("output.txt", "a")
f.write("Election results\n")
f.write("---------------------------------\n")
f.write(f"Total votes: {int(total_votes)}\n")
f.write("---------------------------------\n")
i = 0
for candidate, vote in candidates.items():
    f.write(f"{candidate}: {votes_per[i]} ({vote}) \n") 
    i+=1
f.write("---------------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("---------------------------------\n")
f.close()

