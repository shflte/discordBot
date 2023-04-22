import subprocess

def backup(message):
    # Check if message contains spaces
    if ' ' in message:
        print("Error: message cannot contain spaces.")
        return
    # Construct command to execute
    command = "/home/shflte/.klei/DoNotStarveTogether/backup.sh -d {}".format(message)
    # Execute command
    subprocess.run(command, shell=True)