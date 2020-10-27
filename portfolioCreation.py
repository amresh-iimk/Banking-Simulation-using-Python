#7477
#Amresh Kumar

import calendar
import datetime
import random
import string

import pandas as pd
import numpy as np

YTD = datetime.date.today().year
MTD = datetime.date.today().month

start_Year  = int(input("Enter the Starting Year"))
start_Month = int(input("Enter the Starting Month"))

book_month_range = ((YTD-start_Year)*12)+(MTD-start_Month)

print(f"The portfolio will be constructed for {book_month_range} months")

applicant_Fname = ["Amresh", "Mamta", "Ayansh", "Magic", "Nick"]
applicant_Sname = ["Kumar", "Mandal", "Yadav", "Sharma", "Pandey"]

total_appl_num = 0
app_data_df = pd.DataFrame()
for i in range(1, book_month_range+1):
    print(i)
    count_daily_Apple = random.randrange(10, 20)
    total_appl_num += count_daily_Apple
    print(total_appl_num), print(count_daily_Apple)
    for j in range(1, count_daily_Apple):
        app_Id = str(start_Year) + str(start_Month) +  ("000" + str(i))[-3:] + ("000" + str(j))[-3:]
        rand_Seq = random.randrange(1,5,1)
        first_name = applicant_Fname[rand_Seq]
        rand_Seq2 = random.randrange(1, 5, 1)
        second_name = applicant_Sname[rand_Seq2]
        salary_dec = random.randrange(30000,100000,1000)
        appln_amount = random.randrange(50000,1000000,10000)
        num_dependent = random.randrange(1, 5, 1)
        total_experience = random.randrange(1, 35, 1)
        current_job_exp = random.randrange(1, 10, 1)
        app_data = pd.DataFrame({"app_Id"           : [app_Id],
                                 "first_name"       : [first_name],
                                 "second_name"      : [second_name],
                                 "salary_dec"       : [salary_dec],
                                 "appln_amount"     : [appln_amount],
                                 "num_dependent"    : [num_dependent],
                                 "total_experience" : [total_experience],
                                 "current_job_exp"  : [current_job_exp]
                                 })
        app_data_df = app_data_df.append(app_data)

 print(app_data_df)
 print(f"Total applications received is {total_appl_num}")

app_data_df.to_csv('app_data_df.csv', sep=',')


#############################################################################################
        app_data = pd.DataFrame(app_data)

app_data_df = pd.DataFrame(app_data)


app_data = (app_Id, first_name, salary_dec)
app_data = {"app_Id": app_Id,
            "first_name": first_name,
            "salary_dec": salary_dec}


#############################################################################################################
months = []
for i in range(1,13):
    months.append((i, calendar.month_name[i]))
print(months)

for mnth in months:
    x = calendar._monthlen(2019,1)
    for y in range(x+1):
        print(y)

var = calendar.month_name[3]

for month in calendar.month_name[1:]:
    print(month)



def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.sample(letters, length))
    print("Random String is:", result_str)