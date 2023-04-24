import subprocess
import os

dst_folder = "/home/shflte/.klei/DoNotStarveTogether"

def back_up(message):
    # Check if message contains spaces
    if ' ' in message:
        print("Error: message cannot contain spaces.")
        return -1
    # Construct command to execute
    command = dst_folder + "/backup.sh -d {}".format(message)
    # Execute command
    subprocess.run(command, shell=True)
    return

def roll_back(save):
    # Check if message contains spaces
    if ' ' in save:
        print("Error: message cannot contain spaces.")
        return -1
    # Construct command to execute
    if save == None:
        command = dst_folder + "/roll_back.sh"
    else:
        if save not in all_save():
            return -1
        command = dst_folder + f'/roll_back.sh -s {save}'
    # Execute command
    subprocess.run(command, shell=True)
    return

def toggle(action):
    if action == "up":
        command = dst_folder + "/toggle_server.sh -u"
    elif action == "down":
        command = dst_folder + "/toggle_server.sh -d"

    # Execute command
    completed_process = subprocess.run(command, shell=True)

    if completed_process.returncode == 0:
        return
    else:
        raise Exception("Command failed with exit code {}".format(completed_process.returncode))

    return

def all_save():
    backup_dir = dst_folder + "/world_backup"
    folders = os.listdir(backup_dir)
    folders.sort(reverse=True)
    result = []
    for folder in folders[:10]:
        result.append(folder)
    return result
