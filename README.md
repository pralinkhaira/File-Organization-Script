# File Organization Script

The File Organization Script is a Python program that automates the process of organizing files in a directory based on specific criteria. It helps in managing cluttered folders or large datasets by sorting files into appropriate subdirectories.

## Features

- Organize files based on criteria such as file extension, creation date, or modification date.
- Supports recursive directory scanning for organizing files in subdirectories.
- Handles existing files in target directories to avoid overwriting or duplicate file names.
- Logging mechanism to keep a record of the file organization process.
- Command-line interface for easy usage and configuration.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

```shell
git clone https://github.com/PralinKhaira/File-Organization-Script.git
```

2. Change to the project directory:

```shell
cd file-organization-script
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

### Usage

```shell
python file_organization_script.py <target_directory> [-c <criteria> ...] [-l <log_file>]
```

- `<target_directory>`: The directory to organize.
- `<criteria>` (optional): Criteria for organizing files. Multiple criteria can be provided.
- `<log_file>` (optional): Path to the log file.

### Examples

Organize files in the current directory based on their extension:

```shell
python file_organization.py . -c extension
```

Organize files in the "documents" directory based on both extension and creation date:

```shell
python file_organization.py documents -c extension creation_date
```

### Logging

The script logs information and warnings to a log file. By default, the log file is named `file_organization.log` in the project directory. You can specify a different log file using the `-l` or `--log_file` option.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
