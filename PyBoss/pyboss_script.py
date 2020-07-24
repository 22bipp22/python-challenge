#PyBoss Homework
import os
import csv

csvpath = os.path.join("Resources","employee_data.csv")

emp_id = []
emp_first_name = []
emp_last_name = []
new_dob = []
new_ssn = []
emp_state = []


with open(csvpath) as csvfile:
    empdata = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(empdata)

    for row in empdata:

        emp_id.append(row[0])
                
        #Split the name into first and last name fields
        name_split = row[1].split(" ", 1)
        emp_first_name.append(name_split[0]) 
        emp_last_name.append(name_split[1])

        ####Need to concatenate into a new DOB field with MM/DD/YYYY
        dob_split = row[2].split("-", 2)
        new_dob.append(f"{dob_split[1]}/{dob_split[2]}/{dob_split[0]}")
        

        #####need to figure out how to hide first five digits of SSN
        emp_ssn_split = row[3].split("-", 2)
        new_ssn.append(f"***-**-{emp_ssn_split[2]}")

        #######need to shorten date to 2 digit abbreviation
        us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }
        emp_state.append(us_state_abbrev[row[4]])

employee_zip = zip(emp_id,emp_first_name,emp_last_name,new_dob,new_ssn,emp_state)

output_file = os.path.join("Analysis","employee_dataout.csv")

with open(output_file, 'w', newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN","State"])

    writer.writerows(employee_zip)