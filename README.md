# PyBank

Analyze the financial records of your company using Python Scripting

<div style="text-align:center"><img src="images/Revenue-per-lead.png"></div>

## Dataset
<a href=PyBank/Resources/Python_Homework_Instructions_PyBank_Resources_budget_data.csv>Budget Data containg Date and Profit/Loss</a>


## <span id=task_pybank>Tasks</span>

Create a Python script that analyzes the records to calculate each of the following:


  - The total number of months included in the dataset


  - The net total amount of "Profit/Losses" over the entire period


  - The average of the changes in "Profit/Losses" over the entire period


  - The greatest increase in profits (date and amount) over the entire period


  - The greatest decrease in losses (date and amount) over the entire period
  
In addition, script should both print the analysis to the terminal and export a text file with the results.

## Solution

### <a href=PyBank/main.py>Python code</a>:
It performs all the tasks in [the above section](#task_pybank) and outputs the analysis on terminal and to the <a href=PyBank/analysis/PyBank_Analysis.txt> analysis file</a> 



# PyPoll

<div style="text-align:center"><img src="images/Vote_counting.png"></div>


## Dataset
<a href=PyPoll/Resources/PyPoll_Resources_election_data.csv>Election  Data containg Voter ID, County, and Candidate</a>


## <span id = task_pypoll>Tasks</span>

Create a Python script that analyzes the votes and calculates each of the following:


  - The total number of votes cast


  - A complete list of candidates who received votes


  - The percentage of votes each candidate won


  - The total number of votes each candidate won


  - The winner of the election based on popular vote.

In addition, script should both print the analysis to the terminal and export a text file with the results.

## Solution

### <a href=PyPoll/main.py>Python code</a>:
It performs all the tasks in [the above section](#task_pypoll) and outputs the analysis on terminal and to the <a href=PyPoll/analysis/PyPoll_Analysis.txt> analysis file</a> 

# PyBoss
You get to be the boss !
<div style="text-align:center"><img src="images/PyBoss_Images_boss.jpg"></div>

You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. The company recently decided to purchase a new HR system, and the new system requires employee records be stored completely differently.

## Dataset
<a href=PyBoss/Resources/PyBoss_employee_data.csv>Employee data file holding employee records</a>

## <span id = task_pyboss>Tasks</span>

The required conversions are as follows:

- The Name column should be split into separate First Name and Last Name columns.
- The DOB data should be re-written into MM/DD/YYYY format.
- The SSN data should be re-written such that the first five numbers are hidden from view.
- The State data should be re-written as simple two-letter abbreviations.

### <a href=PyBoss/main.py>Python code</a>:
It performs all the tasks in [the above section](#task_pyboss) and outputs the analysis to the <a href=PyPoll/analysis/PyBoss_Analysis.csv> csv file</a> 

# PyParagraph

You get to play the role of chief linguist at a local learning academy
<div style="text-align:center"><img src="images/PyParagraph_Images_language.png"></div>

As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.


## Tasks

Create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:


- Import a text file filled with a paragraph of your choosing.
- Assess the passage for each of the following:
  - Approximate word count
  - Approximate sentence count
  - Approximate letter count (per word)
  - Average sentence length (in words)
