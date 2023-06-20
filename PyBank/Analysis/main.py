#Importing the modules
import os
import csv

#Finding the .csv file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Reading the .csv file
with open(csvpath, encoding="utf8") as csvfile:
    budgetcsv = csv.reader(csvfile, delimiter=",")
    
    #Storing the header row
    csv_header = next(budgetcsv)
    
    #Printing the first lines of the Analysis
    print("Financial Analysis")
    print("----------------------------------")

    #Creating an empty list to store values
    dates = []

    #Determining the count of the date entries in the file
    for row in budgetcsv:
        dates.append(row[0])        

#Printing the month count    
print(f"Total Months: ", len(dates))

#Reading the .csv file
with open(csvpath, encoding="utf8") as csvfile:
    budgetcsv2 = csv.reader(csvfile, delimiter=",")
    
    #Storing the header row
    csv_header = next(budgetcsv2)

    #Setting empty value for total
    total = 0

    #Looping through CSV and adding rows together to find total
    for row in budgetcsv2:
        total = total + int(row[1])

#Printing the total    
print(f"Total: ${total}")

#Reading the .csv file
with open(csvpath, encoding="utf8") as csvfile:
    budgetcsv3 = csv.reader(csvfile, delimiter=",")
    
    #Storing the header row
    csv_header = next(budgetcsv3)

    #Creating empty lists to store values
    pro_los = []
    change = []

    #Looping through CSV to fill pro_los list with column 2 values
    for row in budgetcsv3:
        pro_los.append(float(row[1]))

    #Looping through pro_los list and filling change list with difference values
    for i in range(1, len(pro_los)):
        change.append(pro_los[i] - pro_los[i-1])
        avg_change = sum(change)/len(change)
    
        #Finding the min and max values of the list
        max_change = max(change)
        min_change = min(change)
        
        #Finding the corresponding min and max dates
        max_date = str(dates[change.index(max_change)])
        min_date = str(dates[change.index(min_change)])

#Printing to the rest of the analysis 
print("Average Revenue Change: $", round(avg_change))
print("Greatest Increase in Revenue: ", max_date, "($", max_change, ")") 
print("Greatest Decrease in Revenue: ", min_date, "($", min_change, ")") 

#Finding the file to write to
analysis = os.path.join("analysis.txt")

#Opening the file in write mode
with open(analysis, 'w') as f:

    #Write in lines of analysis, with formatting and spacing added
    f.writelines(f'Financial Analysis')
    f.write('\n')
    f.writelines(f'----------------------------------')
    f.write('\n')
    f.writelines(f"Total: ${total}")
    f.write('\n')
    f.writelines(f'Average Revenue Change: ${round(avg_change)}') 
    f.write('\n')  
    f.writelines(["Greatest Increase in Revenue: ", str(max_date), " ($", str(max_change), ")"]) 
    f.write('\n')
    f.writelines(["Greatest Decrease in Revenue: ", str(min_date), " ($", str(min_change), ")"])
    f.write('\n')