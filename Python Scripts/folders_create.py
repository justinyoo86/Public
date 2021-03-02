# Author: Justin Yoo
# This script will automatically create folders based on the entries inside
# site_list.csv.  This script can be expanded to accomodate more folders within
# columns inside site_list.csv

import os
import pandas as pd
import getpass

user_name = getpass.user()

file_path = 'C:/Users/' + user_name + '/Desktop/'
site_list = pd.read_csv('C:/Users/' + user_name + '/Desktop/site_list.csv',header = 0)

for i in range(0,len(site_list.index)):
    # Check to see if site_list.iloc[i,0] folder exists.  If not, create it.
    if not os.path.exists(file_path + str(site_list.iloc[i,0]) + '/' ):
            os.mkdir(file_path + str(site_list.iloc[i,0]) + '/' )
    # Check to see if site_list.iloc[i,1] folder exists within 
    # file_path/site_list.iloc[i,0] folder.  If not, create it.
    if not os.path.exists(file_path + str(site_list.iloc[i,0]) + '/' + str(site_list.iloc[i,1]) + '/'):
            os.mkdir(file_path + str(site_list.iloc[i,0]) + '/' + str(site_list.iloc[i,1]) + '/')