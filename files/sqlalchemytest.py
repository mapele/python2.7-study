#!\usr\bin\python
#-*-coding:utf-8-*-
import sqlalchemy

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://xwy:594120@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建新User对象:
#new_user = User(id='7', name='Bob')

# 添加到session:
#session.add(new_user)

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.name=='Bob').all()

# 打印类型和对象的name属性:
print 'type:', type(user)
print 'type:', type(user[0])
print 'type:', user[0]
print 'type:', user[0].id
for i in range(len(user)):
    u =user[i]
    print u.id, u.name

# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()