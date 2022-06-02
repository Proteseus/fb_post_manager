from facebook import GraphAPI


token = 'EAAF2WTxlbp0BAAQ3MB1UWgYTTtOBz9vgJPnUUEOzygf0zMXQ9pm9I1KdrL68xSLrShKIKhZBzp7e0HUf2TlrGF0YSCZAmQwVAlKqOLLpYOQ6bQwVYogCJZBvSju1scNlvbkUSzHvrLN4HZBc7CT8BY3GQbQrFZCZCu1ULdThX79pxCBneOx06Cizgu1pQodyfC24gqqmuGQq8FzZCBsqsp5'
groups = ['744128789503859']
message = "Hello from the other side"

graph = GraphAPI(access_token = token)

def posser():
    for group in groups:
        graph.put_object(group, 'feed', message = message)
        print(graph.get_connections(group, 'feed'))

posser()