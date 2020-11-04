import os
import csv

poll_csv = "election_data.csv"

# Open and read csv
with open(poll_csv, "r") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")

  # Read the header row first (skip this part if there is no header)
  csv_header = next(csv_reader)
  #print(f"Header: {csv_header}")

  
  #Define lists and dictionary required for coding
  vote_id = []
  candidates = []
  votes_by_candidate = {}
  
  # Unique candidate and votes for each candidate
  for row in csv_reader:
    vote_id.append(row[0])
    
    candidates.append(row[2])
    
    candidate_name = row[2]
    
    if candidate_name not in votes_by_candidate:
      
      votes_by_candidate[candidate_name] = 0
    
    votes_by_candidate[candidate_name] += 1
    
    #count total votes cast
    Total_Votes = len(vote_id)

  print("Election Results")
  print("------------------")
  print("Total Votes:", Total_Votes)
  print("------------------")

  # Calculating winner and % votes by candidate       
  winner = 0
  winner_name = ""
  
  for x in votes_by_candidate:
        
        if votes_by_candidate[x] > winner:
              
              winner = votes_by_candidate[x]
              
              winner_name = x
        
        percent = round((votes_by_candidate[x] / Total_Votes * 100), 2)
        
        print(f"Candidate: {x} ({votes_by_candidate[x]:,.0f}) {percent}")
  print("------------------------------")
  print(f"Winner is: {winner_name} ({winner})")
  print("------------------------------")