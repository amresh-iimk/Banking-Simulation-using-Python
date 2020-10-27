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