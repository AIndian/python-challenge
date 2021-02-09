import csv
import os

#Start by creating arrays to store data form file


candidates = []
Votes = []

# Seting the data path for election data
datapath = os.path.join('Resources','election_data.csv')
with open(datapath) as csvfile:
    electionData = csv.reader(csvfile)
    
    #Skip headers
    next(electionData)
  
    #reading each row
    for row in electionData:
        #if candidate is not already named, it will be moved to the list of candidates that were voted for
        if row[2] not in candidates:
            #adds the new candidate
            candidates.append(row[2])
            #adds a voting count for them
            Votes.append(1)
        else:
            #if a candidate is named, the index in Votes is the same index in Candidates, so adds 1 vote for that candidate
            Votes[candidates.index(row[2])] += 1


#total Vote Count for calculations
VoteCount = 0
for i in Votes:
    VoteCount = i + VoteCount


    #Creating the final election results

output_file= os.path.join('Analysis','electionResults.txt')
with open(output_file, 'w', newline = '') as datafile:
    spacer = "-------------------------\n"  
    datafile.write("Election Results\n")
    datafile.write(spacer)
    datafile.write("Total Votes: " + str(VoteCount)+"\n")
    datafile.write(spacer)
    for c in candidates:
        datafile.write(c + ": " + "{:.3%}".format(Votes[candidates.index(c)]/VoteCount) + " ("+ str(Votes[candidates.index(c)])+ ")\n")
    datafile.write(spacer)
    datafile.write("Winner: " + candidates[Votes.index(max(Votes))]+"\n")  
    datafile.write(spacer)

with open(output_file) as resultsfile:
    print(resultsfile.read())    