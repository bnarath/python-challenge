import csv
import os

#Change into the directory where this file resides
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#read the csv file
with open('Resources/PyPoll_Resources_election_data.csv') as input_file:
    reader = csv.reader(input_file, delimiter=',')

    #capture header
    header = next(reader, next)
    #['Voter ID', 'County', 'Candidate']
    

    #Initialize the required variables
    Total_Votes = 0
    Candidate_Votes = dict() 
    #Keys: Candidates, Values: Votes
    
    for row in reader:
        Candidate_Votes[row[2]]=Candidate_Votes.get(row[2],0)+1 #Each time a candidate vote is seen, the number of votes are incremented \
        #for that candidate in the dictionary. If the candidate is not present, then the key is added as candidate with a value of 0
        Total_Votes+=1 #Increment Total votes

    #Now we have candidates and total no of votes for each and Total votes = 3521001
    #{'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}
    

    #Create a new dictionary of percentage votes from candidate votes and Total votes
    #Simultaneously create a string variable - print_output, which can be printed later as analysis
    print_output = f"Election Results\n\
-------------------------\n\
Total Votes: {Total_Votes}\n\
-------------------------\n"
    
    winner = None
    Candidate_Perc_Votes = dict()
    for candidate in Candidate_Votes:
        if (not winner) or (winner and Candidate_Votes[candidate]>winner[1]): 
            #If there is no winner tracked yet, temporarily assume 1st candidate is the winner !!
            #If the candidate has more votes than the tracked best, update the best with this value
            winner = [candidate, Candidate_Votes[candidate]]
        Candidate_Perc_Votes[candidate] = round((Candidate_Votes[candidate]/Total_Votes)*100,3)
        print_output+="{}: {:.3f}% ({})\n".format(candidate, Candidate_Perc_Votes[candidate], Candidate_Votes[candidate])
    
    print_output+=f"-------------------------\n\
Winner:{winner[0]}\n\
-------------------------\n"
  
#Now we have the right content to print inside print_output
#print to the terminal
print(print_output)
#Write to the file
with open('analysis/PyPoll_Analysis.txt', 'w') as output_file:
    output_file.write(print_output)


