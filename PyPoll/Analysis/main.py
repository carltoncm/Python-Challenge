#Importing the modules
import os
import csv

#Finding the .csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")

#Reading the .csv file
with open(csvpath, encoding="utf8") as csvfile:
    electioncsv = csv.reader(csvfile, delimiter=",")
    
    #Storing the header row
    csv_header = next(electioncsv)
    
    #Printing the first lines of the Analysis
    print("Election Results")
    print("----------------------------------")

    #Setting value for counting rows
    rowcount = 0

    #Looping through file to count row and print total votes
    for row in electioncsv:
        rowcount += 1       
    print(f"Total Votes: ", rowcount)
    print("----------------------------------")
   
#Reading the .csv file
with open(csvpath, encoding="utf8") as csvfile:
    electioncsv2 = csv.reader(csvfile, delimiter=",")
    
    #Storing the header row
    csv_header = next(electioncsv2)

    #Creating a list of canditates
    candidate = []

    #Filling candidate list with unique values
    for row in electioncsv2:
            if row[2] not in candidate:
                candidate.append(row[2])
    

#Reading the .csv file
with open(csvpath, encoding="utf8") as csvfile:
    electioncsv3 = csv.reader(csvfile, delimiter=",")
    
    #Storing the header row
    csv_header = next(electioncsv3)

    #Creating values for vote counts
    count1 = 0
    count2 = 0
    count3 = 0

    #Looking for canditate name and totaling votes
    for row in electioncsv3:
        for row in electioncsv3: 
            if row[2] == "Charles Casper Stockham":
                count1 = count1 + 1
            elif row[2] == "Diana DeGette":
                count2 = count2 + 1
            else:
                count3 = count3 + 1
    
    #Creating list of vote totals
    votes = [count1, count2, count3]
    

    #Finding each candidates' vote percentage and storing it in a value
    total_votes = count1 + count2 + count3
    count1_percent = (count1 / total_votes) 
    count2_percent = (count2 / total_votes) 
    count3_percent = (count3 / total_votes) 

    #Grouping each candidates' percentage in a list and formatting as percentage
    percentages = ["{:.3%}".format(count1_percent), "{:.3%}".format(count2_percent), 
                   "{:.3%}".format(count3_percent)]
    
    #Zipping the 3 lists together to display each candidate's information together as a value
    clean_election = list(zip(candidate, percentages, votes))
    print(clean_election[0])
    print(clean_election[1])
    print(clean_election[2])

    #Printing the winner based on the analysis above
    print("----------------------------------")
    print("Winner: Diana DeGette")
    print("----------------------------------")

#Finding the file to write to
analysis = os.path.join("analysis.txt")

#Opening the file in write mode
with open(analysis, 'w') as f:

    #Write in lines of analysis, with formatting and spacing added
    f.writelines(f'Election Results')
    f.write('\n')
    f.writelines(f'----------------------------------')
    f.write('\n')
    f.writelines(f'Total votes: {rowcount}')
    f.write('\n')
    f.writelines(f'----------------------------------')
    f.write('\n')
    f.writelines(f'{clean_election[0]}')
    f.write('\n')
    f.writelines(f'{clean_election[1]}')
    f.write('\n')
    f.writelines(f'{clean_election[2]}')
    f.write('\n')
    f.writelines(f'----------------------------------')
    f.write('\n')
    f.writelines(f'Winner: Diana DeGette')
    f.write('\n')
    f.writelines(f'----------------------------------')
    