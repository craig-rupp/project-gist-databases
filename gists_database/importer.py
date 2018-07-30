import requests
from pprint import pprint
from datetime import datetime as dt

def import_gists_to_database(db, username, commit=True):
    g_url_response = requests.get('https://api.github.com/users/{}/gists'.format(username))
    if g_url_response.status_code == 404:
        raise requests.exceptions.HTTPError
    for gist in g_url_response.json():
        int_string = '''
                INSERT INTO gists
                    (github_id, html_url, git_pull_url, git_push_url,
                    commits_url, forks_url, public, created_at, updated_at,
                    comments, comments_url)
                VALUES
                    (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, :comments_url)
            '''
        params = {
            "github_id": gist['id'],
            "html_url": gist['html_url'],
            "git_pull_url": gist['git_pull_url'],
            "git_push_url": gist['git_push_url'],
            "commits_url": gist['commits_url'],
            "forks_url": gist['forks_url'],
            "public": gist['public'],
            "created_at": gist['created_at'],
            "updated_at": gist['updated_at'],
            "comments": gist['comments'],
            "comments_url": gist['comments_url'],
        }
        db.execute(int_string, params)
        if commit:
            db.commit()
        
#pprint(import_gists_to_database('craig', 'gvanrossum'))
