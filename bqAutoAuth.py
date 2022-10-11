from google.cloud import bigquery
from google.auth.exceptions import DefaultCredentialsError, RefreshError
import subprocess



def bqClient(project: str = 'portfolio-project-353016') -> bigquery.Client:
    '''
    Runs authentication test query for gcloud CLI and returns bigquery Client Object.\n
    If no default authentication is found, runs 'gcloud auth login --update-adc' for user to set default login credentials.\n
    '''

    while True:
        # try:
        test = f'''SELECT EXISTS(SELECT schema_name FROM {project}.INFORMATION_SCHEMA.SCHEMATA)'''
        client = bigquery.Client(project)
        conn = client.query(test)
        conn.result()
        break
    #     except DefaultCredentialsError:
    #         print('not authenticated, running gcloud authenticator')
    #         subprocess.getoutput('gcloud auth login --update-adc')
    # print('successful gcloud authentication check')
    return client


if __name__ == '__main__':
    bqClient()