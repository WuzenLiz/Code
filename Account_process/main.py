import json
import pandas as pd
import os
import csv

true_path = os.path.dirname(os.path.realpath(__file__))

tempate_scv = os.path.join(true_path, 'Accounts-2023-07-04.csv')
accounts = []

# open Account_process/Accounts-2023-07-04.csv
## sample 1603,840907131317,1,1 with 1603 is ID, 840907131317 is username, 1 is system, 1 is active
with open(os.path.join(true_path, 'Accounts-2023-07-04.csv'), 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    accounts = list(reader)

# open Account_process\auth2_user_202307041535.csv and convert to tempate_scv
## sample 1 row 47,"84353167258" with 47 is ID and 84353167258 is username
auth2_user = []
with open(os.path.join(true_path, 'auth2_user_202307041535.csv'), 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    auth2_user = list(reader)


# system = 1 as default, active = 1 as default
# remove duplicate accounts, null accounts, and accounts has appeared in tempate_scv
# save as 'accouts.csv'
with open(os.path.join(true_path, 'accouts.csv'), 'w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'username', 'system', 'active'])
    for row in auth2_user:
        if row[1] != '' and row[1] not in accounts:
            writer.writerow([row[0], row[1], 1, 1])