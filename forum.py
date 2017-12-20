# Users
import pdb
from pymongo_db import PyMongoDB as db
class User(db):
    def __init__(self, fname = None, lname = None, username = None):
        self.collection_name = "users"
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.username = username
        self.doc = {"fname": fname, "lname":lname, "username":username}


class Posts(db):
    def __init__(self, uid = None, topic = None, msg = None):
        self.collection_name = "posts"
        self.uid = uid # user id
        self.topic = topic
        self.msg = msg
        self.doc = {"uid":uid, "topic":topic, "msg":msg}

class Topics(db):
    def __init__(self, title):
        self.collection = "topics"
        super().__init__()
        self.title = title
