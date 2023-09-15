import os
import csv 
# Set paths for input (election_data.csv) and output (analysis.txt)
#election_csv =os.path.join("/Users/rasha/Desktop/Analytics Projects/Module 3/Challenge Files/Starter_Code 6/PyPoll/Resources")
election_csv = os.path.join( "Resources","election_data.csv")
output_file = os.path.join("analysis","analysis.txt")
# Define function to be called to return a candidate stat 
# (total vote/candidate and percent overall from total number of voters)
def get_candidate_stat(search_candidate, iterable):
    candidate_total_vote = 0
    if search_candidate in iterable:
        candidate_total_vote = sum([value for value in iterable[search_candidate].values()])
    return candidate_total_vote
# Set lists to store data
total_Votes = 0
candidates = []
candidateVotes = {} 
# Read the input csv file
with open(election_csv, mode="r") as csvfile: 
    # Split the data columns using "," delmiter
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    next(csvreader)
    # Store the columns into respective list variables
    for row in csvreader: 
       total_Votes +=  1  
       candidate =row[2]
       if row[2] not in candidates: 
           candidates.append(candidate)
           candidateVotes[candidate]=[0,0] 
       # Add the current count for the candidate 
       candidateVotes[candidate][1] += 1 
       # Calulcate the percentage of the vote counts for each candidate from total counts
# and calculate the winner as well
candidate_total_vote = 0
prev_candidate_vote = 0
for candidate in candidateVotes:
    candidate_total_vote = candidateVotes[candidate][1]
    candidateVotes[candidate][0] = round((candidate_total_vote / total_Votes) * 100,3)
    if candidate_total_vote > prev_candidate_vote:
        winner = candidate
    prev_candidate_vote = candidate_total_vote
# Set up message variable to hold the output/printout
message = (("-" * 50) + "\n" +f"Total Voter Counts: {total_Votes:,}\n" +("-" * 50) + "\n")
for candidate in candidateVotes:
    message += f"{candidate}: {candidateVotes[candidate][0]}% ({candidateVotes[candidate][1]:,})\n"
message += (("-" * 50) + "\n" +f"Winner: {winner}\n" +("-" * 50) + "\n")
# Print the message
print(message) 

#write changes to csv
with open(output_file, 'w') as file:
    file.write (message)
