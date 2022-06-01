import datetime

def app(environ, start_response):
    now = datetime.datetime.now()
    data = "It's backend server!\nToday is %d.%d.%d" % (now.day, now.month, now.year)
    data = data.encode("ascii")
        
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])