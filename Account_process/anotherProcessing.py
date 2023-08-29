import pandas
import os

trurpath = os.path.dirname(os.path.realpath(__file__))

accounts_sample = pandas.read_csv(os.path.join(trurpath, 'Accounts-2023-07-04.csv'), header=None)

accounts_list = pandas.read_csv(os.path.join(trurpath, 'auth2_user_202307041535.csv'), header=None)

print(accounts_sample)
print(accounts_list)


# create a csv file with the accounts that are not in the accounts_sample file
accounts_list[~accounts_list[0].isin(accounts_sample[0])].to_csv(os.path.join(trurpath, 'accounts_not_in_sample.csv'), index=False, header=False)

# add system = 1 and active = 1 columns to accounts_not_in_sample.csv
accounts_not_in_sample = pandas.read_csv(os.path.join(trurpath, 'accounts_not_in_sample.csv'), header=None)
accounts_not_in_sample['system'] = 1
accounts_not_in_sample['active'] = 1
accounts_not_in_sample.to_csv(os.path.join(trurpath, 'accounts_not_in_sample.csv'), index=False, header=False)

# create a file with 2500 accounts from accounts_not_in_sample.csv
accounts_not_in_sample = pandas.read_csv(os.path.join(trurpath, 'accounts_not_in_sample.csv'), header=None)
accounts_not_in_sample = accounts_not_in_sample.sample(n=2500)
accounts_not_in_sample.to_csv(os.path.join(trurpath, '2500_accounts_not_in_sample.csv'), index=False, header=False)