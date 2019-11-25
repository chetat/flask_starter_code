from app.api import api

@api.route('/hello')
def users():
    return "hello" 