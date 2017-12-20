### An Abstract class to create a contract for DB implementations
### At the very least child classese must implement _connect method
class DB:
    def __init__(self, host=None, port=None, db=None):
        self._connect()

    # connect to database
    def _connect(self):
        raise Exception("Setup Database Connection Details")

    # save entity into database 
    def _save(self):
        pass

    # get single from database
    def _get(self):
        pass

    # get many from database
    def _get_many(self):
        pass

    # update database entry
    def _update(self):
        pass

    # delete from database
    def _delete(self):
        pass
        

