import httplib2 as http

def fuckOff(args): # foaas functionality
    def mkPath(args): # creates REST path from arguments
        s=""
        for i in range (1,len(args)):
            s+="/%s"%args[i]
        s+="/"
        return s
    if(len(args) == 1 or args[1] == "help"):
        return("Usage: !fuckoff $args - For info visit http://www.foaas.com")
    else:
            try:
                from urlparse import urlparse
            except ImportError:
                from urllib.parse import urlparse
            headers={
                'Accept':'text/plain'
            }
            uri='http://www.foaas.com'
            path=mkPath(args)
            target=urlparse(uri+path)
            method='GET'
            body=''
            h=http.Http()
            response,content=h.request(
                    target.geturl(),
                    method,
                    body,
                    headers)
            return(content.decode('utf-8'))
