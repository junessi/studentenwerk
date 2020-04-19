class StatusOK:
    def __init__(self):
        self.data = {"status": 200}

    def dict(self):
        return self.data


class StatusError:
    def __init__(self, msg = "Bad request", code = 400):
        self.code = code
        self.msg = msg

    def dict(self):
        return {"status": self.code, "message": self.msg}

    def str(self):
        return "\{\"status\": {0}, \"message\": \"{1}\"\}".format(self.code, self.msg);


class NotFound(StatusError):
    def __init__(self, msg = "Not found"):
        StatusError.__init__(self, msg, 404)


class LoginFail(StatusError):
    def __init__(self, msg = "Login failed"):
        StatusError.__init__(self, msg, 401)

class InvalidToken(StatusError):
    def __init__(self, msg = "Invalid token"):
        StatusError.__init__(self, msg, 401)


