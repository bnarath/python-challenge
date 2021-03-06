import csv
import os
import sys
from datetime import datetime

#change the working directory to the directory of this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#We need to temporarily change sys.path to load us_state_abbrev.py where the dictionary is stored
#Steps
#Modify sys.path to add new path
#Import module (us_state_abbrev.py)
#Delete the new path from sys.path
new_path = os.path.join(os.path.dirname(__file__), 'Resources', '')
sys.path.append(new_path)
import us_state_abbrev as helper
sys.path.remove(new_path)
#Now, we can use helper.us_state_abbrev dictionary


#Read and write simultaneously
with open('Resources/PyBoss_employee_data.csv') as input_file, open('analysis/PyBoss_Analysis.csv', 'w') as output_file:
    reader = csv.reader(input_file , delimiter=',')
    writer = csv.writer(output_file, delimiter=',')
    #capture header
    header_input = next(reader, None)
    #['Emp ID', 'Name', 'DOB', 'SSN', 'State']

    header_output = ['Emp ID','First Name','Last Name','DOB','SSN','State']
    writer.writerow(header_output)
    
    #Iterate through the input file, make the necessary changes and write to the output file row by row
    for row in reader:
        #Split name and take the first and last piece (Assuming people have atleast two names)
        First_Name = row[1].split()[0] 
        Last_Name = row[1].split()[-1]

        #DOB
        #Parse the string to date and format back to string again (in a different format)
        DOB = datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')

        #SSN Masking
        #Take the last digits and append that with '***-**-'
        SSN = '***-**-'+row[3][-4:]

        #State
        #Use the dictionary to map the state to two-letter abbreviations
        State = helper.us_state_abbrev[row[4]]

        #Now, it's the  time to write!!
        writer.writerow([row[0], First_Name, Last_Name, DOB, SSN, State])