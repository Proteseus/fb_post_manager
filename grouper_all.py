import json
from facebook import GraphAPI
import pandas as pd
import time
import secrets
import random

def read_cred(filename):
    with open(filename) as f:
        credentials = json.load(f)
    return credentials


credentials = read_cred('credentials.json')
graph = GraphAPI(access_token = credentials['access_token'])
message = ''
post = graph.get_object(id='me', fields='groups')
my_group = post['groups']['data']

print('--------------', post['groups']['data'])

post_after = [10, 22, 34, 46]

groups = []
for mg in my_group:
    if 'privacy' in mg:
        if mg['privacy'] != 'CLOSED':
            groups.append(mg['id'])
    else:
        continue
        
print('\n \n \n \n \n \n \n \n \n ')
print(groups)

df = pd.read_excel('posts.xlsx', sheet_name = 0)

for idx, group in enumerate(groups):
    if idx < df.shape[0]:
        message = df.tag[idx]+ "\n" + df.description[idx] + "\n"
        link = df.tag[idx]
        wait_sec = secrets.choice(post_after)
        print("*****Auto Posting Starts After %s Seconds *****" % wait_sec)
        time.sleep(wait_sec)
        graph.put_object(group, 'feed', message = message, link = link)
        print('*******Link Posted *******')