from facebook import GraphAPI


token = ''
groups = ['744128789503859']
message = "Hello from the other side"

graph = GraphAPI(access_token = token)

def posser():
    for group in groups:
        graph.put_object(group, 'feed', message = message)
        print(graph.get_connections(group, 'feed'))

posser()
