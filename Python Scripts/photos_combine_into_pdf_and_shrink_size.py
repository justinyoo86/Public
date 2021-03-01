# Author: Justin Yoo
# This script will resize the photos inside input_file_path 
# by 1/photo_dimension_reduction_factor 
# (e.g. photo_dimension_reduction_factor = 2, then height and width of photo
# will be reduced by 1/2).  The photos will then be saved as PDFs and then 
# merged together into one PDF file, according to output_file_name.
# The output_file_name file size will be checked against file_size_limit (KB)
# and the process will repeat itself until output_file_name file size is less
# than file_size_limit.  The process will repeat itself by ticking up
# photo_dimension_reduction_factor by photo_dimension_reduction_factor_increment
# until the resulting file size is less than file_size_limit.

import os
import getpass
import my_custom_functions as mcf

user_name = getpass.getuser()
input_file_path = 'C:/Users/' + user_name + '/Pictures/1 - Resize/'
output_file_path = 'C:/Users/' + user_name + '/Pictures/2 - Resized Photos/'
pdf_output_file_path = 'C:/Users/' + user_name + '/Pictures/'

#Configure script variables here
photo_dimension_reduction_factor = 4
photo_dimension_reduction_factor_increment = 0.5
client_prefix = 'ABC'
site_number = '12345'
file_size_limit = 742 # This value is in KB

output_file_name = client_prefix + ' ' + site_number + ' Installation Photos.pdf'

# Delete any existing files within output_file_path
delete_photo_list = os.listdir(output_file_path)
mcf.delete_photos_output_file_path(output_file_path, delete_photo_list)

# Resize photos in input_file_path into PDFs and merge PDFs
photo_list = os.listdir(input_file_path)
mcf.resize_photos_save_as_pdf(photo_list, input_file_path, photo_dimension_reduction_factor, output_file_path)
mcf.merge_pdfs(os.listdir(output_file_path), output_file_path, output_file_name, pdf_output_file_path)

# Obtains the size of the resulting PDF file in KB.  st_size originally
# outputs in bytes, so dividing by 1000 will give KB.
pdf_file_size = os.stat(pdf_output_file_path + output_file_name).st_size / 1000
print('The first PDF file size is ' + str(pdf_file_size) + ' KB')

pdf_compression_count = 1

while pdf_file_size >= file_size_limit:
    # This checks to see if the resulting filesize is less than the 
    # variable file_size_limit.  If not, then tick up 
    # photo_dimension_reduction_factor by photo_dimension_reduction_factor_increment
    # and continue resize the photos.  Also tick up pdf_compression_count.
    photo_dimension_reduction_factor = photo_dimension_reduction_factor + photo_dimension_reduction_factor_increment
    pdf_compression_count = pdf_compression_count + 1
    
    # Delete any existing files within output_file_path
    delete_photo_list = os.listdir(output_file_path)
    mcf.delete_photos_output_file_path(output_file_path, delete_photo_list)    
    
    # Resize photos in input_file_path into PDFs and merge PDFs
    mcf.resize_photos_save_as_pdf(photo_list, input_file_path, photo_dimension_reduction_factor, output_file_path)
    mcf.merge_pdfs(os.listdir(output_file_path), output_file_path, output_file_name, pdf_output_file_path)

    # Obtains the size of the resulting PDF file in KB.  st_size originally
    # outputs in bytes, so dividing by 1000 will give KB.    
    pdf_file_size = os.stat(pdf_output_file_path + output_file_name).st_size / 1000
    print('The Dimension Reduction Factor is = ' + str(photo_dimension_reduction_factor))
    print('The PDF file size is ' + str(pdf_file_size) + ' KB')
    print('Number of times the file has been compressed = ' + str(pdf_compression_count))