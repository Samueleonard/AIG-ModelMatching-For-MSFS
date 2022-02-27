from genericpath import exists
from operator import truediv
import os
import shutil
import time
import webbrowser

comFolderPath = "E:\\MSFS\\Community\\Traffic\\aig-aitraffic-oci-beta\\"
githubFolderPath = "E:\\AIG-ModelMatching-For-MSFS\\aig-aitraffic-oci-beta\\"

names = ["Effects", "Sound", "Texture", "Traffic Files", "layout.json", "manifest.json", "SimObjects"]

#######################################


def clearGithubDir():
    print("clearing github folder")
    if exists(githubFolderPath):
        shutil.rmtree(githubFolderPath)
    print("github folder cleared")
    if not os.path.exists(githubFolderPath):
        os.makedirs(githubFolderPath)
    
def copyFiles(toGithub):
    if(not toGithub):
        for name in names:
            print("copying " + githubFolderPath + name + " to " + comFolderPath)
            shutil.move(githubFolderPath + name, comFolderPath)
            print("copied " + githubFolderPath + name + " to " + comFolderPath)
        shutil.move(githubFolderPath + "BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr", "C:\\Users\\samue\\Documents\\vPilot Files\\BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr")
        shutil.rmtree(githubFolderPath)
    else:
        for name in names:
            print("copying " + comFolderPath + name + " to " + githubFolderPath)
            shutil.move(comFolderPath + name, githubFolderPath)
            print("copied " + comFolderPath + name + " to " + githubFolderPath)
        shutil.move("C:\\Users\\samue\\Documents\\vPilot Files\\BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr", githubFolderPath)

def openGithub():
    os.startfile("C:\\Users\\samue\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")

def createZip():
    print("creating zip folder at: " + githubFolderPath + ".zip")
    if(not exists(githubFolderPath + "\\aig-aitraffic-oci-beta.zip")):
        shutil.make_archive(githubFolderPath, 'zip', "E:\\AIG-ModelMatching-For-MSFS\\aig-aitraffic-oci-beta")
    print("zip folder created")
    webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
    wait = input("commit your changes and press enter to continue")

def start():
    clearGithubDir()
    copyFiles(True)
    openGithub()
    createZip()
    copyFiles(False)


#######################################

start()

#delete the old files
#move new files and folder into dir
#open github desktop and commit
#zip aig folder