import shutil
import errno


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