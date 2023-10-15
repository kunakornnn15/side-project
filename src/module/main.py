
import pandas as pd
from google.cloud import bigquery
from reader.read_to_df import read_data_to_dataframe




def import_csv_to_bigquery(project_id, dataset_id, table_id, df):
    # Create a BigQuery client
    client = bigquery.Client(project=project_id)

    # Read the CSV file into a Pandas DataFrame
    # df = pd.read_csv(csv_file_path)

    # Create a BigQuery dataset if it doesn't exist
    dataset_ref = client.dataset(dataset_id)
    client.create_dataset(dataset_ref, exists_ok=True)

    # Define the BigQuery table schema
    job_config = bigquery.LoadJobConfig(schema=df.dtypes.to_dict(), write_disposition='WRITE_TRUNCATE')

    # Load data from the DataFrame into BigQuery
    job = client.load_table_from_dataframe(df, f"{project_id}.{dataset_id}.{table_id}", job_config=job_config)
    job.result()

    return print(f'Data loaded into BigQuery table: {project_id}.{dataset_id}.{table_id}')

# Example usage:
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'
table_id = 'your-table-id'
csv_file_path = 'path/to/your/local.csv'

import_csv_to_bigquery(project_id, dataset_id, table_id, csv_file_path)



