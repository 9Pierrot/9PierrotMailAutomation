import mimetypes

def loadfile(file_path):
    # Lecture du fichier à attacher (ex : PDF)
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = f.name.split("/")[-1]  # ou os.path.basename(f.name)
        ctype, encoding = mimetypes.guess_type(file_name)
        file_maintype, file_subtype = ctype.split("/", 1)
    
    return {"data" : file_data, "name" : file_name, "maintype" : file_maintype, "subtype" : file_subtype}