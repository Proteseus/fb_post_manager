from facebook import GraphAPI


token = 'EAAHw7DJOnAkBAGgrG52sjZB5E5PhipYib1KQjPdSp5kR4UeMjJ59ZC2P4VKuYBfknRGZB1UpooDse5JkaSeHZBdzK4GBednrrJtsKN3rybgashxCX0ubR447jwK29t4T8hr0lWK6s9jQjllEw46yIOg2V4hqZBgZCESLNWSDWQWwgbxmtnFHZAy8Q0Lcp7jkSGpZATeVc4zYVqlMol5gXMtSDnxhpJPwRubzkKoz2mMLoYO13vcdmkaZA'
groups = ['744128789503859']
message = "Hello from the other side"

graph = GraphAPI(access_token = token)

def posser():
    for group in groups:
        graph.put_object(group, 'feed', message = message)
        print(graph.get_connections(group, 'feed'))

posser()