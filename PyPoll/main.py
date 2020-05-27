import csv
import os

#Change into the directory where this file resides
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print(os.getcwd())

#read the csv file
with open('Resources/PyPoll_Resources_election_data.csv') as input_file:
    reader = csv.reader(input_file, delimiter=',')
    # the file is large; It has print(sum((1 for row in reader))) = 3521002 rows
    #capture header
    header = next(reader, next)
    #['Voter ID', 'County', 'Candidate']
    #Total Counties: {'Raffah', 'Marsh', 'Bamoo', 'Queen', 'Trandee'}
    #Total Candidates: {'Correy', "O'Tooley", 'Li', 'Khan'}

    #Initialize the required variables
    Total_Votes = 0
    Candidate_Votes = dict() 
    #Keys: Candidates, Values: Votes
    #Instead of dictionary, we can use 2 synchronized lists also
    
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
-------------------------"
    
    '''
    Another method (for my future reference):
    Candidate_Perc_Votes = {key:round((Candidate_Votes[key]/Total_Votes)*100,3) for key in Candidate_Votes}
    winner = max(Candidate_Perc_Votes, key=lambda x: Candidate_Perc_Votes[x])
    print(Total_Votes)
    print(Candidate_Votes)
    print(Candidate_Perc_Votes)
    print(winner)
    '''

    #Now we have the right content to print inside print_output
    #print to the terminal
    print(print_output)
    #Write to the file
    with open('analysis/PyPoll_Analysis.txt', 'w') as output_file:
        output_file.write(print_output)



