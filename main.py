from asyncio import events
import requests
import urllib
import json
import facebook

TOKEN = 'EAAL1XD2G1YcBANay2iG7M40qXZCepmZBGmK8rutlHH7Q7a0VgsFO9Yk5q7uRpqEavSGrzS32ogtrXelpx3e01ICb9CnnEa92V3OaoZC2JFgLuVZBq2CoVIZAl9SCOpPEf8YOPrAqZBypwHORBWVdUDjT50Mk1SlZBGxPzbUEehvAIKbLL2t3ZCoLuZAI9p7bakDtRKz1iUnB164EKkXPVHdAx86GlIRquyT2FDOi3oEjVN6NZA5OT7C9R2'

# graph = facebook.GraphAPI(access_token = TOKEN)
# events = graph.request('/me?fields=name,age_range')

# print (events)

url = 'https://graph.facebook.com/'
query_string = "name,age_range,email"

response = requests.request("GET", url, access_token = TOKEN, fields = query_string)

print (response)