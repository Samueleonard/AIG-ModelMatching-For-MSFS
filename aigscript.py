from genericpath import exists
import os
import shutil
import time
import webbrowser

comFolderPath = "E:\\MSFS\\Community\\Traffic\\aig-aitraffic-oci-beta\\"
githubFolderPath = "E:\\AIG-ModelMatching-For-MSFS\\aig-aitraffic-oci-beta\\"

names = ["Sound", "Texture", "Traffic Files", "layout.json", "manifest.json", "Effects", 'SimObjects', 'BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr']

#######################################


def clearGithubDir(): #clears the github folder of all files and remakes it empty
    print("clearing github folder")
    if exists(githubFolderPath):
        shutil.rmtree(githubFolderPath)
        os.makedirs(githubFolderPath)
    print("github folder cleared")
        
def copyFiles(toGithub):
    if(not toGithub): #we are moving files back to the community folder after zipping
        for name in names:
            print("copying " + githubFolderPath + name + " to " + comFolderPath)
            shutil.move(githubFolderPath + name, comFolderPath)
            print("copied " + githubFolderPath + name + " to " + comFolderPath)
        shutil.rmtree(githubFolderPath) #clear github folder after moving everything back to community
    else: #we are moving files into the github folder for zipping
        for name in names:
            print("copying " + comFolderPath + name + " to " + githubFolderPath)
            shutil.move(comFolderPath + name, githubFolderPath)
            print("copied " + comFolderPath + name + " to " + githubFolderPath)
        
        os.startfile("C:\\Users\\samue\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
    
        choice = input("Do you want to create a zip file? (y/n)").lower()
        if(choice == "y"):
            print("creating zip folder at: " + githubFolderPath + "aig-aitraffic-oci-beta.zip")
            if(not exists(githubFolderPath + "\\aig-aitraffic-oci-beta.zip")):
                shutil.make_archive(githubFolderPath, 'zip', githubFolderPath+"\\aig-aitraffic-oci-beta")
            print("zip folder created at: " + githubFolderPath + "aig-aitraffic-oci-beta.zip")
            webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
            webbrowser.open("https://github.com/Samueleonard/AIG-ModelMatching-For-MSFS/releases/new")
            wait = input("commit your changes and press enter to continue")
        else:
            print("skipping zip creation")
            push = input("push changes to github then press enter to continue")

def start(): #main function
    clearGithubDir()
    copyFiles(True)
    copyFiles(False)


#######################################

start()
