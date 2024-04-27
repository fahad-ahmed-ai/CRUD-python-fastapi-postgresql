def success_response(msg, data=""):
    return {
        "error": "",
        "msg": msg,
        "data": data,
        "status_code": 200
    }

def not_found_response(msg):
    return {
        "error": "",
        "msg": msg,
        "data": "",
        "status_code": 404
    }

def unauthorized_response(msg):
    return {
        "error": "",
        "msg": msg,
        "data": "",
        "status_code": 401
    }

def error_response(msg, exception=None):
    return {
        "error": repr(exception) if exception else "",
        "msg": msg,
        "data": "",
        "status_code": 500
    }
