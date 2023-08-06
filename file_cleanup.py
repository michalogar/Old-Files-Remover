import os
import datetime
import logging

# Configure logging
logging.basicConfig(filename='file_cleanup.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Input folder_path and days_threshold parameters
folder_path = input("Set folder path\n")
days_threshold = int(input("Set number of days before files are considered old\n"))

# Replace backslashes (\) with forward slashes (/)
folder_path = folder_path.replace("\\", "/")

# Add a forward slash (/) at the end of the string
if folder_path[-1] != '/':
    folder_path += '/'

try:
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Error: Directory {folder_path} not found.")

    # Iterate through the folder structure using os.walk
    # Perform file cleanup
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                try:
                    # Get file creation time
                    creation_time = os.path.getmtime(file_path)
                    creation_date = datetime.datetime.fromtimestamp(creation_time).date()
                    today_date = datetime.date.today()
                    date_difference = today_date - creation_date

                    # Check if file is older than the threshold
                    if date_difference.days > days_threshold:
                        # Delete the file
                        os.remove(file_path)
                        logging.info(f"Deleted file: {file_path} (Age: {date_difference.days} days)")

                except Exception as e:
                    # Log errors that occur while deleting files
                    logging.error(f"Error occurred while deleting file: {file_path} - {str(e)}")

        # Perform directory cleanup
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                try:
                    # Delete empty directories
                    os.rmdir(dir_path)
                    logging.info(f"Deleted empty directory: {dir_path}")
                except Exception as e:
                    # Log errors that occur while deleting directories
                    logging.error(f"Error occurred while deleting directory: {dir_path} - {str(e)}")

except FileNotFoundError as e:
    # Log the directory not found error
    logging.error(str(e))
except Exception as e:
    # Log other unexpected errors
    logging.error(f"An error occurred: {str(e)}")
