import shutil
import errno
from xml.etree.ElementTree import parse


def copyDirectory(src,dest):
    try:
        shutil.copytree(src, dest)
    #Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    #Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' %e)

def copy(src,dest):
    try:
        shutil.copytree(src, dest)
    #Any error saying that the directory doesn't exist
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src,dest)
        else:
            print('Directory not copied. Error: %s' %e)


def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def List_Sequence_Generator(Input_List):
    Output_List = list()
    for First_Counter in range(0,len(Input_List)):
        for Second_Counter in range(0,Input_List[First_Counter]):
            Output_List.append(Second_Counter + 1)
    return Output_List

def XML_Sub_Element_Array_Maker(Top_Element, Sub_Element, XML_Data_File):
    Root = parse(XML_Data_File).getroot()
    Top_Element_Count = 0
    Sub_Element_Count = 0
    Sub_Element_List = []
    for i in Root.iter(Top_Element):
        if i.tag == Top_Element:
            Top_Element_Count = Top_Element_Count + 1
            Elements_List = list(i.iter())
            Sub_Element_Count = 0
            for j in range(0,len(Elements_List)):
                if Elements_List[j].tag == Sub_Element:
                   Sub_Element_Count = Sub_Element_Count + 1
            Sub_Element_List.append(Sub_Element_Count)
            
    print(Sub_Element_List)
    return(Sub_Element_List)
    

