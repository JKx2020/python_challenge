## PyPoll

#import CSV module
import csv


#create and open txt file we want to write to
pypolloutput = open("pypollsummary.txt", 'w')

#Print the title of the analysis to gitbash and txt file
pypolloutput.write("Election Results\n")
pypolloutput.write("--------------------------------\n")

print("Election Results")
print("--------------------------------")

#create variables for the calculations
votes = 0
candidates = []
totalvotes = []
candidate0 = 0
candidate1 = 0
candidate2 = 0
candidate3 = 0
candidatevotes = []
candidatepercents = []


##count total number of votes cast and create list of candidates
#open the CSV file
with open("election_data.csv","r") as pollresults:

    #read the csv file
    pollreader = csv.reader(pollresults, delimiter=",")
    
    #exclude the header row in count
    pollheader = next(pollreader)
    
    #read through the lines of the csv
    for row in pollreader:  
    
        #count the total votes cast
        votes = votes + 1
        
        #list out the candidates that won votes
        if row[2] not in candidates:
            candidates.append(row[2]) 


#Total up the votes per candidate into their own variables
with open("election_data.csv","r") as pollresults:

    #read the csv file
    pollreader = csv.reader(pollresults, delimiter=",")
    
    #exclude the header row in count
    pollheader = next(pollreader)
    
    #read through the lines of the csv
    for row in pollreader:  

        if row[2] == candidates[0]:
            candidate0 += 1
            
        if row[2] == candidates[1]:
            candidate1 += 1
           
        if row[2] == candidates[2]:
            candidate2 += 1
            
        if row[2] == candidates[3]:
            candidate3 += 1
            
#combine the votes per candidate into a single list
candidatevotes.extend([candidate0, candidate1, candidate2, candidate3])


#calculate the %s and add to it's own %s list
for i in candidatevotes:
        
    candidatepercents.append(round((int(i)/votes)*100))
 
print(f'Total Votes: {votes}')
print("--------------------------------")

pypolloutput.write(f'Total Votes: {votes}\n')
pypolloutput.write("--------------------------------\n")


#print the candidate results 
i=0

for name in candidates:
    
    print(f'{name}: {candidatepercents[i]}.000% ({candidatevotes[i]})')
    pypolloutput.write(f'{name}: {candidatepercents[i]}.000% ({candidatevotes[i]})\n')
        
    i += 1

print("--------------------------------")
pypolloutput.write("--------------------------------\n")

#find the winner of the election
candidatelist = dict(zip(candidatevotes,candidates))

winningvotes = max(candidatevotes)

winner = candidatelist.get(winningvotes)

print(f'Winner: {winner}')
pypolloutput.write(f'Winner: {winner}\n')

print("--------------------------------")
pypolloutput.write("--------------------------------\n")
