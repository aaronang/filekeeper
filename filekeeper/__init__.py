import os
import requests

from operator import itemgetter

token = os.environ['FILEKEEPER_TOKEN']

def get_pages():
    payload = {
        'token': token,
    }
    response = requests.get('https://slack.com/api/files.list', params=payload).json()
    return response['paging']['pages']

def get_files(sort_by='created', reverse=False):
    files = []
    for page in range(1, get_pages() + 1):
        payload = {
            'token': token,
            'page': page,
        }
        response = requests.get('https://slack.com/api/files.list', params=payload).json()
        files += response['files']

    return sorted(files, key=itemgetter(sort_by), reverse=reverse)

def delete_files(ids):
    """Delete the n oldest files."""
    for id in ids:
        data = {
            'token': token,
            'file': id,
        }
        requests.post('https://slack.com/api/files.delete', data=data)

