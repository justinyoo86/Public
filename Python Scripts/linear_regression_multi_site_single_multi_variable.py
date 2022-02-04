# Author: Justin Yoo
# This script will perform linear regression calculations on a CSV file 
# containing an site ID, site number, month, year, project status column, 
# cooling degree days (CDD), heating degree days (HDD), and total electrical
# usage.  Based on the parameters, it will conduct either single variable 
# (CDD or HDD) or multivariate (CDD and HDD) linear regression analysis.
# The output file contains all of the statistical coefficients for the linear
# regression model.

from scipy import stats
import pandas as pd
from sklearn import linear_model
import getpass

user_name = getpass.getuser()
input_file_path = 'C:/Users/' + user_name + '/Documents/'
input_csv_file_df = pd.read_csv(input_file_path + 'linear_regression_input.csv')
model_results_df = pd.DataFrame(columns = ['Store', 'Coefficient 1', 'Coefficient 2', 'Intercept', 'RSquare', 'PValue', 'StdDev'])

x_variable_count = 'single' # single or multi
x_variable = 'cdd' # cdd or hdd.  If x_variable_count = multi, then ignore

for i in range(1, input_csv_file_df['Site ID'].max() + 1):
    # Select the rows from input_csv_file_df based on the index number 
    # and put the data values into site_data_df
    site_data_df = input_csv_file_df[input_csv_file_df['Site ID'] == i]
    site_data_df = site_data_df[site_data_df['Total E Usage']!= 0].reset_index(drop = True)
    
    # Drop the first and last row from site_data_df because it may have 
    # partial data.  Grab the site_number and find the row where the project
    # was completed.
    try:
        site_data_df = site_data_df.drop(site_data_df.index[0], inplace = False).reset_index(drop = True)
        site_data_df = site_data_df.drop(site_data_df.index[len(site_data_df) - 1]).reset_index(drop = True)
        site_number = site_data_df['Store'].iloc[0]
        for j in range(0,len(site_data_df)):
            if site_data_df.iloc[j, 4] == 'Completed':
                row_completed = j
                row_completed_minus_twelve = row_completed - 12
    except:
        print('Dataframe is non-existent.')

    y_usage = site_data_df.iloc[row_completed_minus_twelve:row_completed, 7]
    
    # Run either a multi-variate linear regression or a standard linear
    # regression model, based on the parameters.  If multi-variate linear
    # regerssion is chosen, scikit-learn's linear regression is used.
    # If single variate linear regression is chosen, stat's linear regression
    # is used.
    if x_variable_count == 'multi':
        x_input = site_data_df.iloc[row_completed_minus_twelve:row_completed, 5:7]
        lin_reg_model = linear_model.LinearRegression().fit(x_input, y_usage)
        r_square = lin_reg_model.score(x_input, y_usage)
        model_results_df.loc[i] = [site_number, lin_reg_model.coef_[0], lin_reg_model.coef_[1], lin_reg_model.intercept_, r_square, 0, 0]
    else:
        if x_variable_count == 'single' and x_variable == 'cdd':
            x_input = site_data_df.iloc[row_completed_minus_twelve:row_completed, 5]
        elif x_variable_count == 'single' and x_variable == 'hdd':
            x_input = site_data_df.iloc[row_completed_minus_twelve:row_completed, 6]    
        lin_reg_model = stats.linregress(x_input, y_usage)
        model_results_df.loc[i] = [site_number, lin_reg_model.slope, 0, lin_reg_model.intercept, lin_reg_model.rvalue, lin_reg_model.pvalue, lin_reg_model.stderr]

if x_variable_count == 'multi':
    model_results_df.rename(columns = {'Coefficient 1': 'CDD Coefficient', 'Coefficient 2': 'HDD Coefficient'}, inplace = True)
    model_results_df.to_csv(input_file_path + 'multi_variable_cdd_hdd_linear_regression_output.csv')
elif x_variable_count == 'single':
    model_results_df.rename(columns = {'Coefficient 1': x_variable.upper() + ' Coefficient', 'Coefficient 2': 'N/A'}, inplace = True)
    model_results_df.to_csv(input_file_path + 'single_variable_' + x_variable + '_linear_regression_output.csv')