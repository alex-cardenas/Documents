from pathlib import Path
import shutil
import os

def subtitles(path_str):
    #Change working directory to user input path
    os.chdir(path_str)
    #Set path_file to the new working directory
    path_file = os.getcwd()
    path = Path(path_file)
    print("working directory name is: ", path)
    print("file name should be: ", path.name)
    #initialises variable for later use
    old_sub_name = ""

    for file_path in path.iterdir():
        if file_path.name == "Subs":
            for sub_file in file_path.iterdir():
                print("subtitle file path is: ", sub_file)
                print("subtitle file name is: ", sub_file.name)
                shutil.copy2(sub_file, path)
                #Allows os.rename to find the newly copied file
                old_sub_name = sub_file.name

    os.rename(old_sub_name, path.name + ".srt")

if __name__ == "__main__":
    path_str = input("Enter path:\n")
    subtitles(path_str)
