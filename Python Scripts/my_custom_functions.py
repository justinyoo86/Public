# Author: Justin Yoo
# This script contains all of the custom functions I have written or collected
# from the internet.

import os
import PyPDF2
from PIL import Image
import shutil
from xml.etree.ElementTree import parse

def copy(source_folder, destination_folder):
    # Copy a source_folder to a destination_folder.
    try:
        shutil.copytree(source_folder, destination_folder)
    # Error if the directories are the same.
    except shutil.Error as e:
        print('Directory not copied. Error: %s' %e)
    # Any error saying that the source directory doesn't exist.
    except OSError as e:
        print('Directory not copied. Error: %s' %e)

def left(string, amount):
    # Trim a string down to 'amount' of characters, counting from the left.
    return string[:amount]

def right(string, amount):
    # Trim a string down to 'amount' of characters, counting from the right.
    return string[-amount:]

def mid(string, starting_offset, amount):
    # Trim a string down to 'amount' of characters, counting from left and 
    # starting from starting_offset to 'amount' of characters.
    return string[starting_offset:starting_offset + amount]

def xml_sub_element_array_maker(top_element_name, sub_element_name, xml_file):
    # This function parses FastField survey XML files for forms that 
    # comprise of subforms with multi-photo field form questions.
    # top_element_name is the Excel file tab name of a # standard piece of 
    # equipment (e.g. HVAC_Subform).  
    # sub_element_name is another Excel file tab name of the FastField 
    # multi-photo field (e.g. HVAC_Photos).  
    # xml_file is the FastField survey XML output file.
    # This function iterates through an xml_file looking for elements named
    # top_element_name.  Once a top_element_name is found, then it counts how 
    # many sub_element_names are within that top_element_name in the xml tree.  
    # Then it moves to search for the next top_element_name in the xml_file.  
    # The resulting counting_list is a list where each number represents the 
    # number of sub_element_names for each top_element_name, in sequence.
    # ========================================================================
    # Example top_element_name = HVAC_Subform, 
    # sub_element_name = HVAC_Photos, and counting_list = [2, 5, 3]
    # This means HVAC_Subform has two occurrences of HVAC_Photos in first
    # HVAC_Subform XML element, five occurrences of HVAC_Photos in second 
    # HVAC_Subform XML element, and three occurrences of HVAC_Photos in third
    # HVAC_Subform XML element.  This is useful for matching equipment to 
    # the FastField multi-photo field.
    root = parse(xml_file).getroot()
    top_element_count = 0
    sub_element_count = 0
    counting_list = []
    for i in root.iter(top_element_name):
        if i.tag == top_element_name:
            top_element_count = top_element_count + 1
            elements_list = list(i.iter())
            sub_element_count = 0
            for j in range(0,len(elements_list)):
                if elements_list[j].tag == sub_element_name:
                   sub_element_count = sub_element_count + 1
            counting_list.append(sub_element_count)
    
    return(counting_list)

def list_sequence_generator(counting_list):
    # This function serves to further enhance the function 
    # xml_sub_element_array_maker for FastField survey files with subforms
    # comprising multi-photo fields.
    # This function takes in counting_list and creates a numerical sequence
    # from one to the value of the item in the list.
    # Example counting_list = [2, 5, 3] then 
    # output_list = [1, 2, 1, 2, 3, 4, 5, 1, 2, 3]
    # This functions is useful for matching equipment multi-photo entries to 
    # a sequential number so that the photos can be renamed properly.
    # The eventual goal is to combine this with xml_sub_element_array_maker
    # function, when time permits.  This would have to change all of the 
    # code I've currently written.
    output_list = list()
    for first_counter in range(0,len(counting_list)):
        for second_counter in range(0,counting_list[first_counter]):
            output_list.append(second_counter + 1)
    return output_list

def delete_photos_output_file_path(output_file_path, delete_photo_list):
    # This function will delete the photos inside the output_file_path folder,
    # based on the photo file name within delete_photo_list.
    for i in range(0,len(delete_photo_list)):
        os.remove(output_file_path + delete_photo_list[i])

def resize_photos_save_as_pdf(photo_list, input_file_path, photo_dimension_reduction_factor, output_file_path):
    # This function will resize photos in photo_list in input_file_path.  
    # Each dimension is reduced by 1/photo_dimension_reduction_factor.  
    # If photo_dimension_reduction_factor = 2 then height and width are 
    # reduced by 1/2 each, so the resized photo will be 1/4 size of original.
    # Resized photos are saved in output_file_path as a PDF.
    for i in range(0,len(photo_list)):
        Image1 = Image.open(input_file_path + photo_list[i])
        
        Image_Width = Image1.size[0]
        Image_Height = Image1.size[1]
        
        New_Image_Width = int(Image_Width // photo_dimension_reduction_factor)
        New_Image_Height = int(Image_Height // photo_dimension_reduction_factor)
         
        Image1 = Image1.resize((New_Image_Width, New_Image_Height))
        Image1.save(output_file_path + photo_list[i] + '.pdf')
        print('Resizing is complete for photo ' + str(photo_list[i]))

def merge_pdfs(pdf_file_list, output_file_path, output_file_name, pdf_output_file_path):
    # This function will combine PDF files within pdf_file_list in the folder
    # output_file_path into a single pdf file output_file_name in the folder
    # pdf_output_file_path.
    pdf_merger = PyPDF2.PdfFileMerger()
    for i in range(0,len(pdf_file_list)):
        pdf_merger.append(PyPDF2.PdfFileReader(output_file_path + pdf_file_list[i], 'rb'))
    pdf_merger.write(pdf_output_file_path + output_file_name)
    pdf_merger.close()

def lookup_site_number(data_frame, submission_id_site_dictionary):
    # This function will return a data frame that has the site number within
    # the submission_id_site_dictionary from FastField.
    for i in range(0,len(data_frame)):
        data_frame.at[i,'Submission Id'] = submission_id_site_dictionary[data_frame.iloc[i,0]]
    return data_frame