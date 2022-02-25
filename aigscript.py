from genericpath import exists
import os
import shutil

comFolderPath = "E:\\MSFS\\Community\\Traffic\\aig-aitraffic-oci-beta"
githubFolderPath = "E:\\AIG-ModelMatching-For-MSFS\\aig-aitraffic-oci-beta"

def remove(name):
    if exists(name):
        os.remove(name)
    else:
        print(name + " does not exist")

def move(src, dest, name):
    if exists(name):
        shutil.copy(name + "\\path")
    else:
        print(name + " does not exist")

remove(githubFolderPath + "\manifest.json")
move(comFolderPath + "\manifest.json", githubFolderPath + "\manifest.json")


#delete the old files
#move new files and folder into dir
#open github desktop and commit
#zip aig folder