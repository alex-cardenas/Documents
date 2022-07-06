"""
Creator: Alex Cardenas
Date: July 06, 2022

Purpose -
    This script walks through a folder to find a subtitle file and make it Plex-compliant.
    Before the script, subtitles are found in a subfolder "Subs".
    After the script, the subtitles will be copied and renamed in the main folder.

Limitations -
    The subtitle folder must be called "Subs".
    Only the first subtitle file will be taken (whether it's English or not)
        A future version could check for "en" or "english" in the file name.

Issues -
    Line 31 (x = line[:-1]) currently removes the last letter of the last entry
        This makes that file re-checked (since it doesn't match anymore because of that missing last letter)
"""

from pathlib import Path
import shutil
import os
import pickle
import time

def open_list(working_list):
    # open disk file and read the contents to working_list[]
    with open(r"C:\Users\Wan\Documents\Python Scripts\sub_file_rename_data\folders_already_done.txt", "r") as file_obj:
        for line in file_obj:
        # remove linebreak from a current line
        # linebreak is the last character of each line
            x = line[:-1]

            # add current items to the list
            working_list.append(x)
    return working_list

def write_list_to_file(working_list):
    # open disk file and writes the contents of working_list[] to file
    with open(r"C:\Users\Wan\Documents\Python Scripts\sub_file_rename_data\folders_already_done.txt", "w") as file_obj:
        file_obj.write('\n'.join(working_list))


def subtitles(parent_str, working_list):
    #Change working directory to user input path
    os.chdir(parent_str)
    #Set path_file to the new working directory
    path_file = os.getcwd()
    working_directory = Path(path_file)

    for folder_path in working_directory.iterdir():
        if folder_path.name not in working_list:
            for sub_folder_path in folder_path.iterdir():
                if sub_folder_path.name == "Subs":
                    #initialises variable for later use
                    old_sub_name = ""
                    for sub_file in sub_folder_path.iterdir():
                        # print("subtitle file path is: ", sub_file,"\n")
                        # print("subtitle file name is: ", sub_file.name,"\n")
                        # print("folder name is: ", folder_path.name,"\n")
                        shutil.copy2(sub_file, folder_path)
                        #Allows os.rename to find the newly copied file
                        old_sub_name = sub_file.name
                        break
                    # print("old sub name is: ", old_sub_name, "\n")
                    # print("2 folder path is: ", folder_path,"\n")
                    try:
                        os.rename(os.path.join(folder_path,old_sub_name),os.path.join(folder_path,folder_path.name + ".srt"))
                    except:
                        os.remove(os.path.join(folder_path, old_sub_name))
            working_list.append(folder_path.name)

    return working_list

if __name__ == "__main__":
        working_list = []
        init_list_len = len(working_list)
        working_list = open_list(working_list)

        parent_str = input("Enter path:\n")
        working_list = subtitles(parent_str, working_list)
        completed_list_len = len(working_list)
        print("Files added: \n", completed_list_len - init_list_len)
        write_list_to_file(working_list)
