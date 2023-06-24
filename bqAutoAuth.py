from google.cloud import bigquery
from google.auth.exceptions import DefaultCredentialsError
import os, sys, subprocess



projectname = os.environ.get('GCP_PROJECT')


def bqClient(project: str = projectname) -> bigquery.Client:
    '''
    Runs authentication test query for gcloud CLI and returns bigquery Client Object.\n
    If no default authentication is found, runs 'gcloud auth login --update-adc' for user to set default login credentials.\n
    '''

    while True:
        try:
            test = f'''SELECT 1'''
            client = bigquery.Client(project)
            conn = client.query(test)
            conn.result()
            break
        except DefaultCredentialsError:
            try:
                print('not authenticated, running gcloud authenticator')
                subprocess.getoutput('gcloud auth login --update-adc')
            except FileNotFoundError:
                msg = """
                Google Cloud SDK (gcloud CLI) is not installed, please install the Google Cloud SDK before proceeding. 
                \nFor detailed instructions see https://cloud.google.com/sdk/docs/install
                """
                print(msg)
                sys.exit()
    print('successful gcloud authentication check')
    return client


if __name__ == '__main__':
    bqClient()