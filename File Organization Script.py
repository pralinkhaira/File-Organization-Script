import os
import shutil
import argparse
import logging
from datetime import datetime

def organize_files(directory, criteria):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                # Extract file information based on criteria
                file_info = get_file_info(file_path, criteria)
                if file_info:
                    # Create a directory hierarchy based on criteria
                    target_directory = create_directory_hierarchy(directory, file_info)
                    if target_directory:
                        # Move the file to the corresponding directory
                        move_file(file_path, target_directory)

def get_file_info(file_path, criteria):
    file_info = {}
    for criterion in criteria:
        if criterion == 'extension':
            file_info['extension'] = os.path.splitext(file_path)[1][1:].lower()
        elif criterion == 'creation_date':
            file_info['creation_date'] = datetime.fromtimestamp(os.path.getctime(file_path))
        elif criterion == 'modification_date':
            file_info['modification_date'] = datetime.fromtimestamp(os.path.getmtime(file_path))
        # Add more criteria handling as needed
    return file_info

def create_directory_hierarchy(directory, file_info):
    target_directory = directory
    for key, value in file_info.items():
        target_directory = os.path.join(target_directory, str(value))
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
    return target_directory

def move_file(source_path, target_directory):
    filename = os.path.basename(source_path)
    target_path = os.path.join(target_directory, filename)
    if not os.path.exists(target_path):
        shutil.move(source_path, target_path)
        logging.info(f"Moved '{filename}' to '{target_directory}'")
    else:
        logging.warning(f"File '{filename}' already exists in '{target_directory}'. Skipped.")

def setup_logging(log_file):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        filename=log_file, filemode='a')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

def main():
    parser = argparse.ArgumentParser(description='File Organization Script')
    parser.add_argument('directory', type=str, help='Target directory to organize')
    parser.add_argument('-c', '--criteria', nargs='+', default=['extension'],
                        choices=['extension', 'creation_date', 'modification_date'],
                        help='Criteria for organizing files (extension, creation_date, modification_date)')
    parser.add_argument('-l', '--log_file', type=str, default='file_organization.log',
                        help='Path to the log file')
    args = parser.parse_args()

    directory = args.directory
    criteria = args.criteria
    log_file = args.log_file

    setup_logging(log_file)
    logging.info('Starting file organization...')

    organize_files(directory, criteria)

    logging.info('File organization completed.')

if __name__ == '__main__':
    main()
