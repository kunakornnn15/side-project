import pandas as pd

def read_data_to_dataframe(file_path, file_format):
    """
    Reads data from different file formats into a Pandas DataFrame.

    Parameters:
    - file_path (str): The path to the input file.
    - file_format (str): The format of the input file ('csv', 'excel', 'json', 'parquet').

    Returns:
    - pd.DataFrame: A Pandas DataFrame containing the data from the input file.
    """
    if file_format.lower() == 'csv':
        return pd.read_csv(file_path)
    elif file_format.lower() == 'excel':
        return pd.read_excel(file_path)
    elif file_format.lower() == 'json':
        return pd.read_json(file_path)
    elif file_format.lower() == 'parquet':
        return pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format. Supported formats: 'csv', 'excel', 'json', 'parquet'.")
