class Adapter:
    
    def __init__(self, process) -> None:
        self.process = process
    
    def handle(self, request):
        message = {
        "method": request["HTTP_method"],
        "header": {
            "token": request["HTTP_header"]['token'],
            "origin": request["HTTP_header"]['origin']
        },
        "body": {
            "name": request["HTTP_body"]['name'],
            "message": request["HTTP_body"]['message']
        }
    }
        response = self.process.handle(message)
        return response
        