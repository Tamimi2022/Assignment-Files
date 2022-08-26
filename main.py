__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile

# Point 1
directory = os.getcwd()
cachePath = os.path.join(directory, 'cache')
def clean_cache():
    if os.path.exists(cachePath):
        print(cachePath)
        shutil.rmtree(cachePath)  # Deletes everything cache
    os.mkdir(cachePath) # Creates cache an empty folder in Current Dir
    
# Point 2
def cache_zip(zip_path: str, cache_path: str):  # With 2 arguments
    with ZipFile(zip_path, "r") as zip:
        zip.extractall(cache_path)
    
# Point 3
def cached_files():
    files_list = []
    cachePath = os.path.join(directory, 'cache') 
    for file in os.listdir(cachePath):
        filePath = os.path.join(cachePath, file)
        files_list.append(filePath)
        #print(files_list)  # will show all of files when run
    return files_list
    
# Point 4
def find_password(files_list):
    for file in files_list:
        with open(file, "r") as f:
            for text in f.readlines():
                if 'password' in text:
                    return str(text.split(": ")[1]).strip()
    print(str(text.split(": ")[1]).strip())
    
    
if __name__ == '__main__':
    pass
