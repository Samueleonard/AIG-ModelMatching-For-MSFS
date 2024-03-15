from genericpath import exists
import os
import shutil
import time
import webbrowser

githubFolderPath = "C:\\Users\\samue\\Documents\\GitHub\\AIG-ModelMatching-For-MSFS\\Community\\"
comFolderPathMain = "F:\\MSFS Addons\\AI Traffic\\Air Traffic\\"
#names of the folders/files inside the aig main folder that we will copy
componentFolderNames = ["Effects", "SimObjects", "Sound", "Texture", "Traffic Files", "BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr", "layout.json", "manifest.json"]

def clearGithubDir(): #clears the github folder of all files and remakes it empty
    print("Clearing Github Folder")
    if exists(githubFolderPath):
        shutil.rmtree(githubFolderPath)
        print("Github Folder Cleared")
    os.makedirs(githubFolderPath) #folder doesnt already exist - make it 
    os.mkdir(githubFolderPath + "aig-aitraffic-oci-beta")
    print("Blank Community Folder Made At " + githubFolderPath)
    print("#############################################################################")

def copyFiles():
    #copy to github
    shutil.move(comFolderPathMain + "aig-aitraffic-effects\\", githubFolderPath) #copy aig-aitraffic-effects
    shutil.move(comFolderPathMain + "aig-aitraffic-modelbehavior\\", githubFolderPath) #copy aig-aitraffic-modelbehavior

    for name in componentFolderNames:
        shutil.move(comFolderPathMain + "aig-aitraffic-oci-beta\\" + name, githubFolderPath + "aig-aitraffic-oci-beta")
        print("moved " + comFolderPathMain + "aig-aitraffic-oci-beta\\" + name + " to " + githubFolderPath + "aig-aitraffic-oci-beta\\" + name )

    time.sleep(10)
    #copy back to commnunity
    #shutil.move(githubFolderPath + "aig-aitraffic-effects\\", comFolderPathMain) #copy aig-aitraffic-effects
    #shutil.move(githubFolderPath + "aig-aitraffic-modelbehavior\\", comFolderPathMain) #copy aig-aitraffic-modelbehavior
    print("#############################################################################")
    
    '''
    if(not toGithub): #we are moving files back to the community folder after zipping
        for name in names:
            print("copying " + githubFolderPath + "\\Community" + name + " to " + comFolderPath)
            shutil.move(githubFolderPath + "Community\\" + name, comFolderPathMain)
            print("copied " + githubFolderPath + "Community\\" + name + " to " + comFolderPath)
        shutil.rmtree(githubFolderPath) #clear github folder after moving everything back to community
    else: #we are moving files into the github folder for zipping
        for name in names:
            print("copying " + comFolderPath + name + " to " + githubFolderPath)
            shutil.move(comFolderPath + name, githubFolderPath)
            print("copied " + comFolderPath + name + " to " + githubFolderPath)
        '''



    '''
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

        #very weird random bug where the sound folder would not be fully moved over - only the AI folder inside - fix that
        if not exists(githubFolderPath + "Sound"): #if this folder doesnt exist then the sound folder was not copied properly
            os.mkdir(githubFolderPath + "Sound")
            shutil.move(githubFolderPath + "AI", githubFolderPath + "Sound")
            print("moved " + githubFolderPath + "AI" + " to " + githubFolderPath + "Sound")
        
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
    '''

def start(): #main function
    clearGithubDir()
    copyFiles()

#######################################

start()