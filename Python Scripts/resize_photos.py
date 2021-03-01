# Author: Justin Yoo
# This script will read a set of photos in input_file_path folder and resize
# them all by 1/photo_reduction_factor for both height and width 
# (e.g. if photo_reduction_factor = 2, then photos will be reduced by 1/2 in 
# both height and width, or by 1/4 total).
# The resized photos will be saved in output_file_path.

import os
from PIL import Image
import getpass

user_name = getpass.getuser()
input_file_path = 'C:/Users/' + user_name + '/Pictures/1 - Resize/'
output_file_path = 'C:/Users/' + user_name + '/Pictures/2 - Resized Photos/'

photo_list = os.listdir(input_file_path)
photo_reduction_factor = 2
photo_list_delete = os.listdir(output_file_path)

# For any existing photos in output_file_path, delete them.
for i in range(0,len(photo_list_delete)):
    print('Removing file ' + photo_list_delete[i] + '.')
    os.remove(output_file_path + photo_list_delete[i])

# For any photos in input_file_path, resize them and reduce them by 
# 1/photo_reduction_factor by both height and width.
for i in range(0,len(photo_list)):
    image_1 = Image.open(input_file_path + photo_list[i])
    image_1 = image_1.resize((int(round(image_1.size[0]/photo_reduction_factor, 0)), int(round(image_1.size[1]/photo_reduction_factor, 0))))
    image_1.save(output_file_path + photo_list[i])
        
print('Photo resizing is complete for ' + str(len(photo_list)) + ' photos in ' + input_file_path + '.')