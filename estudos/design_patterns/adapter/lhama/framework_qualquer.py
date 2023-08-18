from src.routes import route1

def post_http():
    http_message = {
        "method": "POST",
        "header": {
            "token": "Bearer weirhweirowehrwerew",
            "origin": "http://something.other.org"
        },
        "body": {
            "name": "Lhama",
            "message": "Hello Word"
        }
    }
    
    route1(http_message)