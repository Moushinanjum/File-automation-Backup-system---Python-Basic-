import os##to work with folders path(directory)
import shutil##files manage(copy,delete,update)
from datetime import datetime#to show time

#saving time information
current_time= datetime.now().strftime("%d-%m-%y_%H-%M-%S")

#saving path
source_folder="E:\pythyon(project)\source"
backup_folder="E:\pythyon(project)\\backup"

temp=os.path.join(backup_folder,"backup "+current_time)#destination,name
os.makedirs(backup_folder,exist_ok=True)

#resource file copy backup

for root,dirs,files in os.walk(source_folder):#parent_folder location,directory(Folder list)list,file list
    
    parent_path=os.path.relpath(root,source_folder)#source,name,destination
    target_path=os.path.join(temp,parent_path)
    os.makedirs(target_path,exist_ok=True)

#files
    for f in files:
        source_file=os.path.join(root,f)
        target_file=os.path.join(target_path,f)
        shutil.copy2(source_file,target_file)
    
print("Succesfully created"+temp)
