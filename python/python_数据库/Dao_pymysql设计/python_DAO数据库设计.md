# DAO 数据库操作设计

DAO(Data Access Object) 数据访问对象只是一种设计思想，目的是简化对数据库的操作，针对实体类对象（数据模型类），封装一套与数据库操作的SDK(Software Develope Kit) 软件开发环境

```python
- dao (基础数据库操作模块)
	|- __init__.py
	|- base.py
- entity (实体类的模块)
	|- user
	|- order
- db (具体的数据操作)
	|- user_db.py
    |- order_db.py
```

# 

 