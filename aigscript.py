from genericpath import exists
import os
import shutil
import time
import webbrowser

comFolderPath = "E:\\MSFS\\Community\\Traffic\\aig-aitraffic-oci-beta\\"
githubFolderPath = "E:\\AIG-ModelMatching-For-MSFS\\aig-aitraffic-oci-beta\\"

names = ["Sound", "Texture", "Traffic Files", "layout.json", "manifest.json", "Effects", 'SimObjects', 'BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr']



#######################################

##AIG is adding payware models - obviously these cannot be distributed so we must remove the individual payware models from the folder and back into the main aig folder
def handlePaywareModels(): #move out payware files before commiting/shipping
    paywareModelNames = ["aig 1", "aig 2"]
    for i in range(len(paywareModelNames)):
        if exists(githubFolderPath + "\\simobjects\\airplanes\\" + paywareModelNames[i]):
            print("moving: " + githubFolderPath + "\\simobjects\\airplanes\\" + paywareModelNames[i] + " to " + comFolderPath + "\\simobjects\\airplanes\\" + paywareModelNames[i])
            #shutil.move(githubFolderPath ) 
            print("moved: " + githubFolderPath + "\\simobjects\\airplanes\\" + paywareModelNames[i] + " to " + comFolderPath + "\\simobjects\\airplanes\\" + paywareModelNames[i])
        else:
            print(githubFolderPath + "\\simobjects\\airplanes\\" + paywareModelNames[i] + " does not exist")

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
        handlePaywareModels()
        for name in names:
            print("copying " + comFolderPath + name + " to " + githubFolderPath)
            shutil.move(comFolderPath + name, githubFolderPath)
            print("copied " + comFolderPath + name + " to " + githubFolderPath)

        #very weird random bug where the sound folder would not be fully moved over - only the AI folder inside - fix that
        print((githubFolderPath + "Sound\AI"))
        if not exists(githubFolderPath + "Sound\AI"): #if this folder doesnt exist then the sound folder was not copied properly
            os.mkdir(githubFolderPath + "Sound\\AI")
        
        os.startfile(os.getenv('LOCALAPPDATA') + "\\GitHubDesktop\\GitHubDesktop.exe")
    
        choice = input("Do you want to create a zip file? (y/n)").lower()
        if(choice == "y"):
            print("creating zip folder at: " + githubFolderPath + "aig-aitraffic-oci-beta.zip")
            if(not exists(githubFolderPath + "\\aig-aitraffic-oci-beta.zip")):
                shutil.make_archive(githubFolderPath, 'zip', githubFolderPath)
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