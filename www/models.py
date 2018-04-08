# -*- coding:utf-8 -*-

__author__ = 'HeZhao'

'''
实体类
'''

import logging
import time, uuid
from www.orm import Model, StringField, IntegerField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


# 测试代码
if __name__ == '__main__':
    from www.orm import create_pool, close_pool
    import asyncio

    async def test(loop):
        # 创建连接池
        db_dict = {'user': 'www-data', 'passwd': 'www-data', 'db': 'awesome'}
        await create_pool(loop=loop, **db_dict)
        u = User(name='Test', email='test@example.com', passwd='12345', image='about:blank', id='123')
        await u.save()
        users = await u.findAll()
        print('list -> %s' % users)
        # 关闭连接池
        await close_pool()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
