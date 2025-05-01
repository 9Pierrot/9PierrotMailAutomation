"""
This file contains a function to load a file for attachment.
The `loadfile` function takes a `file_path` as input and reads the file to attach. It returns a dictionary with the following keys:
- `data`: the file data as bytes
- `name`: the name of the file
- `maintype`: the main type of the file
- `subtype`: the subtype of the file
"""

import mimetypes


def loadfile(file_path):
    # read the file to attach
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = f.name.split("/")[-1]  
        ctype, encoding = mimetypes.guess_type(file_name)
        file_maintype, file_subtype = ctype.split("/", 1)
    
    # return the file data, name, maintype and subtype
    return {"data" : file_data, "name" : file_name, "maintype" : file_maintype, "subtype" : file_subtype}