from filecmp import dircmp
import shutil


# macros
SOURCE = 'C:\Users\dir1'
DESTN = 'D:\Users\dir2'
TARGET = 'D:\Users\dir3'
# "list" to store the required files to be copied to the TARGET folder
files = []


# compares and adds only the updated files in DESTN folder to the list "files" by appending the DESTN path
def copy_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("updated file %s found in %s and %s" % (name, dcmp.left, dcmp.right))  # comment if not needed
        updated_file = DESTN + '\\' + name
        files.append(updated_file)


# ***Actual required process starts from here***
# copy the contents of both SOURCE and DESTN to the variable "dcmp"
dcmp = dircmp(SOURCE, DESTN)

# function call by passing SOURCE and DESTN contents
copy_diff_files(dcmp)


# compares and adds only the latest files in the DESTN folder to the list "files" by appending the DESTN path
for i in range(len(dcmp.right_only)):
    new_file = DESTN + '\\' + dcmp.right_only[i]
    files.append(new_file)


# prints only the required files to be copied [comment the below 'print' if not needed]
print(files)

# copying the required files to the TARGET folder
for f in files:
    shutil.copy(f, TARGET)
