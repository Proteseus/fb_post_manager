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

post_after = [600, 720, 840, 900]

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

for ip in range(df.shape[0]):
    post = random.randint(0, df.shape[0] - 1)
    message = df.tag[post]+ "\n" + df.description[post] + "\n"
    link = df.tag[post]
    wait_sec = secrets.choice(post_after)
    random_group = secrets.choice(groups)
    print("*****Auto Postin Starts After % Seconds *****" % wait_sec)
    time.sleep(wait_sec)
    print("1111111", random_group, df.link[post])
    graph.put_object(random_group, 'feed', message = message, link = link)
    print('*******Link Posted *******', post)