import pymysql
from pymysql.cursors import DictCursor


class Connection():
    def __init__(self):
        self.conn = pymysql.Connection(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            charset="utf8",
            db='qidian'
        )

    def __enter__(self):
        # DictCursor 把查询结果集进行dict化
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type:
            self.conn.rollback() # 回滚事务
            # 日志收集异常信息，上报给服务器
        else:
            self.conn.commit() # 提交事务
    def close(self):
        try:
            slef.conn.close()
        except:
            pass