# Old-Files-Remover
File Cleanup is a Python script that automatically deletes old files and empty directories within a chosen folder path, streamlining file organization and storage efficiency.

## How to use
1. Make sure you have Python installed on your system.
2.Download the file_cleanup.py script and place it in the location where you want to perform file cleanup.
3. Open a terminal or command prompt in the same directory as the script.
4. Run the script by executing the following command:
python file_cleanup.py
5. The script will prompt you to enter the folder path and the number of days before files are considered old. Follow the instructions and provide the required information.
6. The script will then recursively go through the folder structure, identify files that are older than the specified threshold, and delete them. It will also remove any empty directories.
7. The details of the cleanup process will be logged in a file named file_cleanup.log located in the same directory as the script.

## Important Notes
- Please use this script with caution and make sure to verify the folder path and days threshold you enter to avoid accidental data loss.
- The script will permanently delete files, and they cannot be recovered once deleted.
- Double-check the folder path and threshold before proceeding with the cleanup.
- It is recommended to test the script on a small set of sample data before using it on important folders.
- The script will log any errors that occur during the cleanup process in the file_cleanup.log file.
- The script uses the modification time of files to determine their age.

