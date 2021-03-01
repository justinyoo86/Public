# Author: Justin Yoo
# This script will create multiple folders with the naming convention of 
# client_prefix - site_number.  The multiple folders will be copies of a 
# designated 'Template Folder.'
# The variable site_number is taken from a 'site_list' CSV file.
# This script will also rename a specific file (e.g. Excel) inside the new 
# folder, allowing for customized document naming within the new folder copy.

import os
import pandas as pd
import getpass
import My_Custom_Functions as custom_func

user_name = getpass.user()
output_file_path = 'C:/Users/' + user_name + '/Desktop/App Folders/'
site_list = pd.read_csv('C:/Users/' + user_name + '/Desktop/Site List.csv',header = 0)
client_prefix = input('Please type in the customer prefix.')

for i in range(0,len(site_list.index)):
    template_folder = 'C:/Users/' + user_name + '/Desktop/Template Folder'
    
    # Edit the output naming convention here.
    new_site_folder = output_file_path + client_prefix + str(site_list.iloc[i,0]).zfill(4) + ' - ' + str(site_list.iloc[i,1]) + ', ' + str(site_list.iloc[i,2]) + '/'
    custom_func.copy(template_folder, new_site_folder)
    
    # Rename a file inside the newly copied folder.
    os.rename(new_site_folder + '/Excel File.xls', new_site_folder + '/' + client_prefix + str(site_list.iloc[i,0]).zfill(4) + ' Excel File.xls')
    print("Finished Copying " + str(i) + " out of " + str(len(site_list.index)) + ".")

print("All Done.")