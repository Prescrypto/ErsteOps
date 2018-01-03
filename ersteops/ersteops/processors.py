''' Custom variables send to templates context '''

def add_url_protocol(request):
    ''' add url protocol to context '''
    return {
        "HTTP_PROTOCOL" : 'https' if request.is_secure() else 'http',
    }
