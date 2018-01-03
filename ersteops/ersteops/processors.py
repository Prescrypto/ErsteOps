''' Custom variables send to templates context '''

def add_url_protocol(request):
    ''' add url protocol to context '''
    uri = request.build_absolute_uri('/')[:-1]
    protocol = uri.split("://")[0]
    return {
        "HTTP_ABSOLUTE_URI" : uri,
        "HTTP_PROTOCOL" : protocol,
    }
