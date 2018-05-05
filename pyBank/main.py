# This is the main of pyBank project

import os

# Module for reading CSV's
import csv

monthRecords = []
revenueRecords = []
changeRevenue = []

dir_path = os.path.join('Resources')
dirList = os.listdir(dir_path)
for f in dirList:
    print(f"\t{dirList.index(f)}  : {f}")

loop = True

while loop:    
    fileChoice = int(input(f"\tPick a file number from above:=> ")  )  
    if fileChoice >=0 and fileChoice < len(dirList):
        csv_path = os.path.join('Resources',dirList[fileChoice])
        loop = False

with open(csv_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    another_line_after_header = next(csvreader)
    for row in csvreader:
        monthRecords.append(row[0])
        revenueRecords.append(float(row[1]))

# build a list with revenue difference to prior month
for i in range(len(revenueRecords)):
    if i > 0:
        changeRevenue.append(revenueRecords[i] - revenueRecords[i -1])
    else:
        changeRevenue.append(0)

print("\n--------------------------")
print(f"Financial Analysis - {dirList[fileChoice]}")
print("--------------------------")
print(f"Total Months: {len(monthRecords)} " )    
print(f"Total Revenue: {sum(revenueRecords)} ")
print(f"Average revenue change: {round(sum(changeRevenue)/len(changeRevenue),2)}")
print(f"Greatest Increase in Revenue: {monthRecords[changeRevenue.index(max(changeRevenue))]} {max(changeRevenue)}") 
print(f"Greatest Decrease in Revenue: {monthRecords[changeRevenue.index(min(changeRevenue))]} {min(changeRevenue)}\n")

# txtfile.write(changeRevenue)

# Specify the file to write to
output_path = os.path.join( "output", "Budget_Financial_Anaysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Months: {len(monthRecords)} \n" )    
    txtfile.write(f"Total Revenue: {sum(revenueRecords)} \n")
    txtfile.write(f"Average revenue change: {round(sum(changeRevenue)/len(changeRevenue),2)}\n")
    txtfile.write(f"Greatest Increase in Revenue: {monthRecords[changeRevenue.index(max(changeRevenue))]} ( {max(changeRevenue)} )\n") 
    txtfile.write(f"Greatest Decrease in Revenue: {monthRecords[changeRevenue.index(min(changeRevenue))]} ( {min(changeRevenue)} )\n")
    
 