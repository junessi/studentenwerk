class StatusOK:
    def __init__(self):
        self.obj = {"status": 200}

    def dict(self):
        return self.obj


class NotFound:
    def __init__(self, msg = "Not found"):
        self.obj = {"status": 404, "message": msg}

    def dict(self):
        return self.obj

    def str(self):
        return "\{\"status\": 404, \"message\": \"{0}\"\}".format(self.msg);


class LoginFail:
    def __init__(self, msg = "Login failed"):
        self.obj = {"status": 401, "message": msg}

    def dict(self):
        return self.obj

    def str(self):
        return "\{\"status\": 401, \"message\": \"{0}\"\}".format(self.msg);
