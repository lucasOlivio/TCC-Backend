import sys
sys.path.insert(0, './db_conf')

from postgres import PostDB

if __name__ == "__main__":
    db = PostDB()

    if not db.checkDB():
        if db.createDB():
            if not db.importSQL('./db_conf/invest.sql'):
                db.dropDB()

