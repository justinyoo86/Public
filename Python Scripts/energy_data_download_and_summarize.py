# Author: Justin Yoo
# This script will automaticaly download and analyze energy data files from
# energy utilities.  It can be modified for downloading files from a utility
# that allows for CSV downloads of account data.  The CSV account data is 
# downloaded, unzipped, and analyzed.

import os
import pandas as pd
import time
import zipfile
import datetime
from selenium import webdriver
import getpass
import my_custom_functions as mcf

user_name = getpass.getuser()
file_path = 'C:/Users/' + user_name + '/Documents/'
date_time_right_now = datetime.datetime.now()
date_time_right_now_string = str(date_time_right_now.month) + "-" + str(date_time_right_now.day) + "-" + str(date_time_right_now.year) + " " + str(date_time_right_now.hour) + "-" + str(date_time_right_now.minute)
date_right_now_string = str(date_time_right_now.month) + "-" + str(date_time_right_now.day) + "-" + str(date_time_right_now.year)
account_list = pd.read_csv(file_path + 'accounts_to_download.csv', header = 0)

prompt_download_files = input("Download the account data files? (Yes/No)")
prompt_zip_file_extract = input("Unzip files in the Downloads folder? (Yes/No)")

# If the prompt was answered yes, this block of code will load up a Google 
# Chrome web browser, clear of any cookies or history, and download account 
# data files by inserting in account numbers and downloading them.  
# This is the only code that relates to a software-driven browser.
#
# time.sleep(3) is inserted throughout this block of code to pause the script 
# and give the webpage time to respond to button clicks and load.
if prompt_download_files == "Yes":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path = 'C:/Users/' + user_name + '/Documents/chromedriver', chrome_options=chrome_options)
    browser.delete_all_cookies()
    browser.get('https://secure.comed.com/MyAccount/MyService/Pages/UsageDataTool.aspx')
    time.sleep(3)
    view_summary_data_online_radio_button = browser.find_element_by_id("ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_RequestOption_0")
    view_summary_data_online_radio_button.click()
    print('View Summary Data Online radio button has been selected.')
    time.sleep(5)
    counter = 0 
    for i in range(0,len(account_list)):
        try:
            account_number_field = browser.find_element_by_id('AccountNumber')
        except:
            Prompt = input('Please clear the popup')
            account_number_field = browser.find_element_by_id('AccountNumber')
        print('All buttons and fields found.')
        account_number = account_list.iloc[i,0]
        account_number = str(account_number).zfill(10)
        print('Sending the following Account Number:' + str(account_number))
        account_number_field.send_keys(account_number)
        time.sleep(3)
        AddButton = browser.find_element_by_id("ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Addbtn")
        time.sleep(3)
        AddButton.click()
        time.sleep(3)
        counter = counter + 1
        print('Counter is at: ' + str(counter))
        time.sleep(3)
        download_button = browser.find_element_by_xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_Downloadbtn"]')
        remove_all_accounts_button = browser.find_element_by_xpath('//*[@id="ctl00_ctl00_ContentPlaceHolderMain_FeaturedContentZone_ctl00_ctl00_btnRemoveAll"]')               
        
        # The maximum number of accounts that can be batched is 10, so the 
        # counter will count to 10 and then initiate a batch download.  Once
        # the batch file has been downloaded, it will clear the account field.
        if counter == 10:
            time.sleep(5)
            browser.execute_script('arguments[0].click();', download_button)
            print('Downloading data batch.')
            time.sleep(5)
            browser.execute_script('arguments[0].click();', remove_all_accounts_button)
            counter = 0
            time.sleep(10)
        else:
            if i == len(account_list)-1:    
                time.sleep(5)
                browser.execute_script('arguments[0].click();', download_button)
                print('Downloading data batch.')
                time.sleep(5)
                browser.execute_script('arguments[0].click();', remove_all_accounts_button)
        print('Total accounts downloaded = ' + str(i+1))

# If the prompt was answered yes, this block of code will unzip the ZIP files 
# located in the Downloads folder.
if prompt_zip_file_extract == "Yes":
    zip_files_file_path = "C:/Users/" + user_name + "/Downloads/"
    zip_files_extraction_file_path = file_path + "CSV Files/"
    for i in os.listdir(zip_files_file_path):
        print(i)
        if i == "desktop.ini":
            continue
        FolderNameLength = len(i) - 4
        FileName = mcf.left(i, FolderNameLength)
        ZIPFileReference = zipfile.ZipFile(zip_files_file_path + i, 'r')
        ZIPFileReference.extractall(zip_files_extraction_file_path + "/")
        ZIPFileReference.close()
    
# Create a DataFrame to summarize the data from the CSV files.
csv_files_file_path = file_path + 'CSV Files/'
datalist = os.listdir(csv_files_file_path)
csv_summary_data_frame = pd.DataFrame(index = range(0,len(datalist)), columns=['AcctNumber','Status','12 Month Usage (kWh)','12 Month Peak Demand (kW)','Number of Data Rows','12 Month Average Load Factor'])
csv_summary_data_frame = csv_summary_data_frame.fillna(0)

# This block of code will analyze the CSV files in the 'CSV Files' folder.  
for i in range(0,len(datalist)):
    annual_usage = 0    
    monthly_average_load_factor = 0
    csv_summary_data_frame.iloc[i,0] = mcf.left(datalist[i],10)
    print('Reading ' + str(datalist[i]))
    RowFinderFrame = pd.read_csv(csv_files_file_path + datalist[i], error_bad_lines = False, warn_bad_lines = False, header = 0)
    
    for k in range(0,len(RowFinderFrame.index)):
        if RowFinderFrame.iloc[k,0] == '**Rate Legend':
            HeaderRow = k + 1
            print('Found Header Row.')
    try:
        account_csv_analysis = pd.read_csv(csv_files_file_path + datalist[i], header = HeaderRow)
    except ValueError:
        print('Parser Error for ' + datalist[i] + ".")
        continue
    
    try:
        account_csv_analysis.drop('On-Peak KWH Usage', axis = 1, inplace=True)
        account_csv_analysis.drop('Off-Peak KWH Usage', axis = 1, inplace=True)
    except ValueError:
        print('Headers do not match finding for ' + datalist[i] + ".")
        continue
    except KeyError:
        print('Could not find columns to drop.')
    
    # Trim the end of the CSV file where the data table ends.
    for j in range(0,len(account_csv_analysis.index)):
        if account_csv_analysis.iloc[j, 0] == '**Rate Legend':
            account_csv_analysis.drop(account_csv_analysis.index[j:], inplace=True)
            existing_rows = j
            account_csv_analysis.drop(account_csv_analysis.index[12:], inplace=True)
            break
    
    # Check the peak demand.
    try:
        if account_csv_analysis['Monthly Peak Demand (KW)'].max() <= 200:
            csv_summary_data_frame.iloc[i,1] = "Yes - Checked On " + date_right_now_string
        else:
            csv_summary_data_frame.iloc[i,1] = "No - Checked On " + date_right_now_string
    except ValueError:
        print("Resolve error code manually for " + datalist[i])
        continue
    except KeyError:
        print("Resolve error code manually for " + datalist[i])
    
    # Calculate 12 month sum of energy usage.
    if existing_rows >= 12:
        for k in range(0,12):
            try:
                annual_usage = account_csv_analysis.iloc[k,3] + annual_usage
                monthly_average_load_factor = account_csv_analysis.iloc[k,3] / (account_csv_analysis.loc[k,'Monthly Peak Demand (KW)'] * account_csv_analysis.iloc[k,2] * 24) + monthly_average_load_factor
            except IndexError:
                print("Resolve error code manually for " + datalist[i])
        monthly_average_load_factor = monthly_average_load_factor/12
    else:
        for k in range(0,existing_rows):
            annual_usage = account_csv_analysis.iloc[k,3] + annual_usage
            monthly_average_load_factor = account_csv_analysis.iloc[k,3] / (account_csv_analysis.loc[k,'Monthly Peak Demand (KW)'] * account_csv_analysis.iloc[k,2] * 24) + monthly_average_load_factor
        monthly_average_load_factor = monthly_average_load_factor/existing_rows
        annual_usage = annual_usage / (12/existing_rows)
    
    try:
        csv_summary_data_frame.iloc[i,2] = annual_usage
        csv_summary_data_frame.iloc[i,3] = account_csv_analysis['Monthly Peak Demand (KW)'].max()
        csv_summary_data_frame.iloc[i,4] = existing_rows
        csv_summary_data_frame.iloc[i,5] = monthly_average_load_factor
    except:
        print("Resolve error code manually for " + datalist[i])

csv_summary_data_frame.to_csv(file_path + 'Account Summary ' + date_time_right_now_string + '.csv',sep = ',')    