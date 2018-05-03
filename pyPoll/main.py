# This is the main of pyBank project

import os

# Module for reading CSV's
import csv

votorRecords = []
countyRecords = []
candidateRecords = []

csv_path = os.path.join('Resources', 'election_data_1.csv')

with open(csv_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    another_line_after_header = next(csvreader)
    for row in csvreader:
        votorRecords.append(row[0])
        countyRecords.append(row[1])
        candidateRecords.append(row[2])

candidates = list(set(candidateRecords))
# print(candidates)   
votes = []
for candidate in candidates:
    votes.append(0)
# print(votes)

# for vote in candidateRecords
for vote in candidateRecords:
    # import pdb; pdb.set_trace()
    votes[candidates.index(vote)] += 1

# print(votes)

print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {len(candidateRecords)}")
print(f"----------------------")
for candidate in candidates:
    print(f"{candidate}: {round(votes[candidates.index(candidate)] * 100 /len(candidateRecords),2)}% ({votes[candidates.index(candidate)]})")

print(f"----------------------")
print(f"Winner: {candidates[votes.index(max(votes))]}")
print(f"----------------------")

results = []

results.append(f"Election Results")
results.append(f"----------------------")
results.append(f"Total Votes: {len(candidateRecords)}")
results.append(f"----------------------")
for candidate in candidates:
    results.append(f"{candidate}: {round(votes[candidates.index(candidate)] * 100 /len(candidateRecords),2)}% ({votes[candidates.index(candidate)]})")

results.append(f"----------------------")
results.append(f"Winner: {candidates[votes.index(max(votes))]}")
results.append(f"----------------------")



# print(results)

outfile = os.path.join('output', 'PollResults.txt')

with open(outfile,"w") as txtfile:
    for line in results:
        txtfile.write("\n" + line)
    
    
 