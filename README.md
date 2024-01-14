# file_loader
This module helps to load the data into Pandas data frame, checks dimension, size, and has error handling too, all from one function call. 


# Key Features:

Support for Multiple File Formats: Easily load data from CSV, Excel (.xlsx), and JSON files.
Error Handling: Robust error handling for file-not-found, permission issues, empty data, format errors, and unexpected issues.
Data Inspection: On loading a file, the utility displays the size and dimensions (rows and columns) of the DataFrame, giving immediate insights into the loaded data.
Simple and User-Friendly: Designed with simplicity in mind, this tool is perfect for both beginners and experienced Python users.
How to Use data_loader:

Import the Utility: First, import the data_loader.py function into your Python script.
Load a File: Call load_file(file_path) with the path to your data file. The function returns a Pandas DataFrame if successful or None in case of an error.
Inspect Your Data: After loading, the utility automatically prints the size and dimensions of the DataFrame.

Requirements:

Python 3.x
Pandas library
Getting Started:

Clone the repository and incorporate the load_file function into your Python projects to streamline data loading and initial inspection.
