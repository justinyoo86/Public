# Author: Justin Yoo
# This script will quickly unzip .ZIP files that are located within a 
# file_path directory folder.  The contents of the ZIP files can be extracted
# into single folders for each ZIP file, or all in a single folder.

import zipfile
import os
import my_custom_functions as mcf
import getpass

user_name = getpass.user()

file_path = 'C:/Users/' + user_name + '/Downloads/'
zip_extract_file_path = 'C:/Users/' + user_name + '/Desktop/Extraction/'

for i in os.listdir(file_path):
    if i == "desktop.ini":
        continue
    
    # Remove the ".ZIP" extension from the file name
    zip_file_name_length = len(i) - 4
    
    file_name = mcf.left(i, zip_file_name_length)
    zip_file_current = zipfile.ZipFile(file_path + i, 'r')
    
    # Extract all the files into their own folders in the zip_extract_file_path
    # directory.
    zip_file_current.extractall(zip_extract_file_path + "/" + file_name)
    
    # Extract all the files into the zip_extract_file_path directory.
    #zip_file_current.extractall(zip_extract_file_path + "/")
    
    zip_file_current.close()