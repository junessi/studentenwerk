import common.heap_sort as hs

class LikedUsers:
    def __init__(self, liked_user = []):
        self.liked_users = liked_users

    def has(self, uid):
        uid = int(uid)

        l = 0                           # left
        r = len(self.liked_users) - 1   # right
        while l < r:
            i = (l + r)/2

            if uid < self.liked_users[i]:
                r = i - 1
            elif uid > self.liked_users[i]:
                l = i + 1
            else:
                return True

        return False

    def add(self, uid):
        self.liked_users.append(int(uid))
        hs.sort(self.liked_users)

    def data(self):
        return self.liked_users

