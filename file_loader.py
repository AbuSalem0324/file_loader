import pandas as pd


def load_file(file_path):

    """Load a file into a pandas dataframe and display its size and dimensions.

    Args:
    file_path (str): The path to the file to be loaded.

    Returns:
    pandas.DataFrame or None: The loaded data or None if an error occurs.
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format")

        # Display the size and dimensions of the DataFrame
        print(f"Successfully loaded: {file_path}")
        print(f"Dimensions (Rows, Columns): {df.shape}")
        print(f"Size (Total Elements): {df.size}")

        return df

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"No data: {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Parse error: {file_path} may be incorrectly formatted.")
    except IOError as io_err:
        print(f"I/O error: {io_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None