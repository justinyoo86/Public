# Author: Justin Yoo
# This script will consolidate data from multiple XML files.  When setting up
# the DataFrame of all_xml_file_data_dataframe, the column names can be 
# renamed to match the XML files being analyzed.

import xml.etree.ElementTree as ET
import pandas as pd
import os
import datetime
import getpass
import my_custom_functions as mcf

user_name = getpass.user()

time_right_now = datetime.datetime.now()
time_stamp = str(time_right_now.month) + "-" + str(time_right_now.day) + "-" + str(time_right_now.year) + " " + str(time_right_now.hour) + "-" + str(time_right_now.minute) 

input_xml_file_path = 'C:/Users/' + user_name + '/Desktop/XML Files/'

xml_file_list = os.listdir(input_xml_file_path)

all_xml_file_data_dataframe = pd.DataFrame(index = range(0,len(xml_file_list)),
        columns = ['Customer ID', 'Account Number','Business Name', 'Business Address', 'City', 'State', 'ZIP Code', 'Telephone Number', 'Annual kWh', 'Annual Therms'])

for i in range(0,len(xml_file_list)):
    xml_file_current = ET.parse(input_xml_file_path + xml_file_list[i])
    xml_root = xml_file_current.getroot()
    
    # The first column of the DataFrame row will contain the xml file name.
    all_xml_file_data_dataframe.iloc[i,0] = mcf.left(xml_file_list[i], len(xml_file_list[i])-4)
    
    
    for j in range(0,9):
        # For all columns in a specific row i of xml_root, copy over the data
        # to the all_xml_file_data_dataframe DataFrame, column by column.
        all_xml_file_data_dataframe.iloc[i, j+1] = xml_root[0][j+1].text

all_xml_file_data_dataframe.to_csv('C:/Users/' + user_name + '/Desktop/XML Consolidated Data File ' + time_stamp + '.csv',sep = ',')
