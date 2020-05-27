import csv
import os



#Change the current working directory to the location of the file main.py
#print(os.path.abspath(__file__))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print(os. getcwd())


with open("Resources/budget_data.csv", 'r') as input_file:
    reader = csv.reader(input_file, delimiter=',')
    header = next(reader, None) #reader is an iterator, next returns next value, if no next value, then None is returned
    
    
    #Initialize the required variables and update as we iterate through the rows
    Total_Months=0
    Total = 0
    GreatestProfit_WorstLoss = [None]*4 #Placeholder for [The month for Greatest Profit, Greatest Profit, The month for Worst Loss, Worst Loss]
    for row in reader:
        #Update Total Months
        Total_Months+=1
        #Update Total
        Total+=int(row[1])

        if GreatestProfit_WorstLoss[0] == None:  #First row values are placed as Greatest Profit and Worst Loss
            #This condition is met only for the first row
            GreatestProfit_WorstLoss = [row[0], int(row[1])]*2
            first = int(row[1]) #First row profit/loss
        else:
            if int(row[1])-prev>GreatestProfit_WorstLoss[1]:
                GreatestProfit_WorstLoss[1] = int(row[1])-prev #If the current increase in profit is > than the greatest profit change being traced, update the greatest profit change with the current increase in profit
                GreatestProfit_WorstLoss[0] = row[0]
            if int(row[1])-prev<GreatestProfit_WorstLoss[3]:
                GreatestProfit_WorstLoss[3] = int(row[1])-prev #If the current increase in profit is < than the worst loss change being traced, update the worst loss change with the current increase in profit
                GreatestProfit_WorstLoss[2] = row[0]
        prev = int(row[1]) #To keep track of the previous row profit/loss

    #Once the loop exits, the prev contains the last value and first contains the first value
    Average_Change = (prev-first)/(Total_Months-1) #Average of Total Changes
    
    #Time for print
    print(f"\
Financial Analysis\n\
----------------------------\n\
Total Months: {Total_Months}\n\
Total: ${Total}\n\
Average  Change: ${round(Average_Change, 2)}\n\
Greatest Increase in Profits: {GreatestProfit_WorstLoss[0]} (${GreatestProfit_WorstLoss[1]})\n\
Greatest Decrease in Profits: {GreatestProfit_WorstLoss[2]} (${GreatestProfit_WorstLoss[3]}")

    #Time to store
    with open("analysis/PyBank_Analysis.txt", "w") as output_file:
        output_file.write(f"\
Financial Analysis\n\
----------------------------\n\
Total Months: {Total_Months}\n\
Total: ${Total}\n\
Average  Change: ${round(Average_Change, 2)}\n\
Greatest Increase in Profits: {GreatestProfit_WorstLoss[0]} (${GreatestProfit_WorstLoss[1]})\n\
Greatest Decrease in Profits: {GreatestProfit_WorstLoss[2]} (${GreatestProfit_WorstLoss[3]}")