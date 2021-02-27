import os
from PIL import Image
import getpass

user_name = getpass.getuser()
input_file_path = 'C:/Users/' + user_name + '/Pictures/1 - Resize/'
output_file_path = 'C:/Users/' + user_name + '/Pictures/2 - Resized Photos/'

photo_list = os.listdir(input_file_path)

photo_reduction_factor = 2

photo_list_delete = os.listdir(output_file_path)

#Delete any photos in the output file path.
for i in range(0,len(photo_list_delete)):
    print('removing file ' + photo_list_delete[i])
    print(i)
    os.remove(output_file_path + photo_list_delete[i])
   
for i in range(0,len(photo_list)):
    image_1 = Image.open(input_file_path + photo_list[i])
    
    image_1 = image_1.resize((int(round(image_1.size[0]/photo_reduction_factor, 0)), int(round(image_1.size[1]/photo_reduction_factor, 0))))
    image_1.save(output_file_path + photo_list[i])
        
print("Photo resizing is complete.")