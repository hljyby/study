import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from dao.base import BaseDao
from entity import Book

class BookDao(BaseDao):
    def query(self, where=None, whereargs=None):
        ret = super(BookDao, self).query('t_book', "book_id", "name", "cover", "summary", "url","author", "tags", where=where, whereargs=whereargs)
        return [Book(item["book_id"],item["name"],item["cover"],item["summary"],item["url"],item["author"],item["tags"]) for item in ret]

if __name__ == "__main__":

    dao = BookDao()
    print(dao.query(where='where name like %s',whereargs=("%主%",)))
