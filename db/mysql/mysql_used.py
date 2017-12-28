import pymysql


# 创建数据库链接
def conn():
    return pymysql.connect("192.168.0.253", "root", "admin", "pysql", 3306)


def insert():
    # 创建数据库链接
    db = conn()
    # 使用cursor() 方法获取操作游标
    cursor = db.cursor()

    # SQL插入语句
    sql = "insert into employee(first_name, last_name, age )  \
          values('Mac_1', 'Mohan_1', 16)  \
          "
    print(sql)
    # 执行SQL语句
    cursor.execute(sql)
    # 执行SQL语句
    db.commit()
    # try:
    #     # 执行SQL语句
    #     cursor.execute(sql)
    #     # 执行SQL语句
    #     db.commit()
    # except:
    #     # 发生错误时回滚
    #     db.rollback()
    db.close()


# 执行修改操作
def update():
    # 获取数据库链接
    db = conn()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 更新语句
    sql = "update employee set age = age +1 where first_name = '%s'" %('Mac')

    try:
        # 执行sql 语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print("执行sql异常，回滚数据")
        db.rollback()
    # 关闭数据库链接
    db.close()


# 删除
def delete():
    # 获取数据库链接
    db = conn()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 更新语句
    sql = "delete from employee where first_name = '{0}'".format('Mac')
    try:
        # 执行sql 语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

    except:
        print("执行sql异常，回滚数据")
        db.rollback()

    # 关闭数据库链接
    db.close()


# insert()
# insert()
# update()
delete()
