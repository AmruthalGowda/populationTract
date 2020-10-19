# Census population tract

# Table of contents

1. [Problem](README.md#Problem)
2. [Input](README.md#Input)
3. [Approach & Algorithm](README.md#Approach)
4. [Output](README.md#Output)
5. [Test-cases](README.md#Test-cases)
5. [Run Instructions](README.md#Run-Instructions)
6. [Contact](README.md#Contact)

# Problem

The federal Census datasets for census tracts, including relatively small areas that average 4,000 inhabitants are considered. Data at that detailed level is useful, but sometimes it's also helpful to roll up some of the information.

As a data engineer, handle/clean the data by handling missing values and create a platform to analyze the population tract from 2000 to 2010 Core Based Statistical Area wise by calculating: *total number of census tracts*, *total popluation in 2000*, *total population in 2010* and *average population percentage change for census tract*

# Input
Dataset is available in [path](https://github.com/InsightDataScience/population-rollup) in readme 'censustract-00-10.csv' file is provided
Particular data in data sets have been choosen to perform certain test cases and the input snippets are found in Test_cases tab

# Approach
Steps followed to resolve this problem is- <br>
Read file contents line by line <br>
Clean data as necessary <br>
Insert required data into dictionary <br>
Sort data in the dictionary <br>
Write data to output file <br>

###Algorithm

Step 1: Create result dictionary
Step 2: Open file in read mode
Step 3: Set pop2000,pop2010 and perchange variables to 0
Step 4: Extracting pop2000, pop2010 and pchange from data 
step 5: Convert step4 data into respective format. For ex: population to int and pchange to float
step 6: Removing common from numerical values 
step 7: Handle missing/garbage value from pop and pchange data
step 8: Read CSBAcode and CSBA title from data 
step 9: Check for each row: 
	If CSBA code is empty in result dictionary add required data into result dictionary
step 10: If CSBA code exists in dictionary:
	Check for CSBA title - if empty then add title in the dictionary 
	Add new row data(pop2000, pop2010, pchange) into existing dictionary 
step 11: Open 'report.csv' into writing mode
step 12: Find average of pchange by diving with tract
step 13: Sort result dictionary and write 

# Output

Program creates a report.csv output file and it holds below data respectively:
*total number of census tracts*, *total popluation in 2000*, *total population in 2010*, *average population percentage change for census tract* grouped by CSBA

# Run Instructions
Python version : 3.8.1 
Inlcuded I/O libraries alone
Test cases can be run by moving each input file from testsuite to input file and check output<br>

# Contact
Email Address : alakshmanegowda@hawk.iit.edu
[LinkedIn](https://www.linkedin.com/in/amruthagowda/)

