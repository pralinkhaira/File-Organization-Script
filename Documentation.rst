File Organization Script Documentation
=====================================

.. contents::
   :depth: 2

Introduction
------------

The File Organization Script is a powerful automation tool designed to simplify and streamline the process of organizing files within a directory. It aims to help users efficiently manage cluttered folders and large datasets by automatically sorting files into appropriate subdirectories based on specific criteria.

Usage
-----

To use the File Organization Script, follow these steps:

1. Install the required dependencies:

   - Python 3.x
   - `shutil` library

2. Run the script with the following command:

   .. code-block:: bash

      python file_organization_script.py <directory> [-c <criteria> ...] [-l <log_file>]

   - Replace `<directory>` with the path to the target directory you want to organize.
   - Use the optional `-c` flag to specify the criteria for file organization. Multiple criteria can be provided, such as `extension`, `creation_date`, and `modification_date`.
   - Use the optional `-l` flag to specify the path to the log file. If not provided, the default log file `file_organization.log` will be used.

Features
--------

The File Organization Script offers several key features:

- **Automated File Organization**: The script automatically scans the specified directory and organizes files into subdirectories based on the specified criteria.
- **Flexible Criteria**: Users can choose from various criteria to organize files, including file extension, creation date, and modification date. This allows for customizable organization strategies.
- **Recursive Directory Scanning**: The script can perform recursive scanning of the target directory, organizing files in subdirectories as well. This ensures a comprehensive and thorough organization process.
- **Error Handling and Logging**: The script provides error handling to gracefully handle exceptions and log detailed information about the file organization process. This allows users to troubleshoot any issues encountered.

Example
-------

To illustrate the usage of the File Organization Script, consider the following example:

Suppose you have a directory called `documents` that contains various files. To organize the files based on their file extensions, run the following command:

.. code-block:: bash

   python file_organization.py documents -c extension

This command will create subdirectories for each unique file extension within the `documents` directory and move the corresponding files into their respective directories. For instance, all PDF files will be moved to a `pdf` directory, while all image files will be moved to an `images` directory.

Customization
-------------

The File Organization Script can be customized and extended to suit specific requirements. Here are some possible customization options:

- **Additional Criteria**: You can extend the script to support additional criteria for file organization, such as file size, specific keywords, or custom metadata.
- **File Renaming**: Implementing file renaming functionality can provide more control over the organization process. For example, you could prepend a timestamp to the file name or rename files based on specific patterns.
- **User Interface**: Consider building a graphical user interface (GUI) or a web interface to enhance the user experience and simplify the process of specifying criteria and selecting directories.
- **Integration with Cloud Storage**: Integrating the script with cloud storage platforms, such as Google Drive or Dropbox, would enable seamless organization of files stored in the cloud.

Ensure that you thoroughly test any customizations and have proper backups of your files before running the script.

Troubleshooting
---------------

If you encounter any issues while using the File Organization Script, consider the following troubleshooting steps:

- **Check the Log File**: If the script fails to organize files or encounters errors, check the log file (`file_organization.log` by default) for detailed information about the issues encountered. The log file will provide insights into any exceptions or warnings encountered during the organization process.
- **File and Directory Permissions**: Ensure that you have the necessary permissions to access and modify the target directory and files. If you encounter permission errors, make sure you have the required access rights.
- **Dependency Check**: Verify that you have the required dependencies installed, specifically Python 3.x and the `shutil` library. Ensure that you are using compatible versions of these dependencies.

Contributing
------------

If you would like to contribute to the File Organization Script project, you can follow these steps:

1. Fork the project repository on GitHub.
2. Make the desired changes and enhancements to the script.
3. Submit a pull request to the original repository, providing a detailed description of your changes, improvements, or new features.

License
-------

The File Organization Script is released under the MIT License. See the `LICENSE` file for more information.

