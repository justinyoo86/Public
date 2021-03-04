# Author: Justin Yoo
# This script will read a set of photos in input_file_path folder and rotate
# them all by photo_rotation_angle (degrees counterclockwise).
# The rotated photos will be saved in output_file_path.

import os
from PIL import Image
import getpass

user_name = getpass.getuser()

input_file_path = 'C:/Users/' + user_name + '/Pictures/B 1 - Rotate/'
output_file_path = 'C:/Users/' + user_name + '/Pictures/B 2 - Rotated Photos/'

photo_list = os.listdir(input_file_path)
photo_rotation_angle = 270
photo_list_delete = os.listdir(output_file_path)

# For any existing photos in output_file_path, delete them.
for i in range(0,len(photo_list_delete)):
    print('Removing file ' + photo_list_delete[i] + '.')
    os.remove(output_file_path + photo_list_delete[i])

# For any photos in input_file_path, rotate them by photo_rotation_angle
# (degrees counterclockwise) and save rotated photos in output_file_path.

for i in range(0,len(photo_list)):
    if photo_list[i] == 'desktop.ini':
        continue
    image_1 = Image.open(input_file_path + photo_list[i])
    image_1 = image_1.rotate(photo_rotation_angle, expand = 1)
    image_1.save(output_file_path + photo_list[i])
    
print('Photo rotating is complete for ' + str(len(photo_list)) + ' photos in ' + input_file_path + '.')