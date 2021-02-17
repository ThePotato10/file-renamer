import os
from os.path import isfile, join


# Gets the directory you invoked the script from and saves it as the variable 'directory'
# Saves a list of all files in the directory as the variable 'files'
# Does not access folders in the directory

directory = os.getcwd()
files = [f for f in os.listdir(directory) if isfile(join(directory, f))]

# Maps over the files we got and replaces any space with an underscore
# Additionally, it converts the result back to a list

edited_files = map(lambda file: file.replace(" ", "_"), files)
edited_files = list(edited_files)

# Renames the files according to their new name

for i in range(len(edited_files)):
    old_file = join(directory, files[i])
    new_file = join(directory, edited_files[i])
    os.rename(old_file, new_file)