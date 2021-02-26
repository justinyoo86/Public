import os
import pandas as pd
import getpass
import My_Custom_Functions as custom_func

#Create multiple folders with the structure of "client_prefix - site_number" from a designated "Template Folder"
#site_number is taken from a CSV file containing site numbers

user_name = getpass.user()
file_path = 'C:/Users/' + user_name + '/Desktop/App Folders/'
site_list = pd.read_csv('C:/Users/' + user_name + '/Desktop/Site List.csv',header = 0)
client_prefix = input('Please type in the customer prefix.')

for i in range(0,len(site_list.index)):
    src = 'C:/Users/' + user_name + '/Desktop/Template Folder'
    dest = file_path + client_prefix + str(site_list.iloc[i,0]).zfill(4) + ' - ' + str(site_list.iloc[i,1]) + ', ' + str(site_list.iloc[i,2]) + '/'
    custom_func.copy(src, dest)
    os.rename(dest + '/Excel File.xls', dest + '/' + client_prefix + str(site_list.iloc[i,0]).zfill(4) + ' Excel File.xls')
    print("Finished Copying " + str(i) + " out of " + str(len(site_list.index)) + ".")

print("All Done.")