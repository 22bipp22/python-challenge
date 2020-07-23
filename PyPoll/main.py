#PyPoll Homework
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

candidate_file = []
poll_results = [0,0,0,0,0,0,0,0,0,0,0]
vote_percent = [0,0,0,0,0,0,0,0,0]
election_results = []
total_votes = 0
highest_votes = 0



with open(csvpath) as csvfile:
    polldata = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(polldata)

    for row in polldata:
        
        candidate_file.append(row[2])

#Remove duplicates of candidates fron candidate file by creating a dictionary key for the list.
candidate_list = list(dict.fromkeys(candidate_file))

with open(csvpath) as csvfile:
    polldata = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(polldata)
  
    for row in polldata:
        #Return the position of candidate voted for from the candidate_list then add 1 to the votes for that candidate in the poll results.  Also add 1 to the grand total number of votes.
        for i in [i for i, candidate in enumerate(candidate_list) if candidate == row[2]]:
                    
            poll_results[i] += 1
            total_votes += 1
               
#Final print display to terminal 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#Calculate percentages of votes and determine the winner and print the candidate list
for candidate_index in range(len(candidate_list)):
    
    vote_percent[candidate_index] = round((poll_results[candidate_index]/total_votes) * 100,3)
    print(f"{candidate_list[candidate_index]}: {vote_percent[candidate_index]}% ({poll_results[candidate_index]})")

    if poll_results[candidate_index] > highest_votes:
        highest_votes = poll_results[candidate_index]
        winner = candidate_list[candidate_index]

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Print results to a text file
output_file = os.path.join("Analysis","Poll_Results.txt")

with open(output_file, 'w') as textfile:
    
    textfile.writelines(f'Election Results \n------------------------- \nTotal Votes: {total_votes} \n-------------------------') 
    
    #loop through candidate lists and print to file
    for candidate_index in range(len(candidate_list)):
        textfile.writelines(f"\n{candidate_list[candidate_index]}: {vote_percent[candidate_index]}% ({poll_results[candidate_index]})")
    
    textfile.writelines(f"\n------------------------- \nWinner: {winner} \n-------------------------")
   
   



        


        