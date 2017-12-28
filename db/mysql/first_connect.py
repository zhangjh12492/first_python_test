import pymysql

# 打开数据库链接
db = pymysql.connect("192.168.0.253",
                     "root", "admin",
                     "pysql", 3306)

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行SQL查询
cursor.execute("select version()")

# 使用 fetchone()方法 取单条数据
data = cursor.fetchone()

print("Database version :%s" % data)

# 关闭数据库
db.close()

# 创建数据库链接
db = pymysql.connect("192.168.0.253",
                     "root", "admin",
                     "pysql", 3306)

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用execute()方法执行sql，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS employee")

# 使用预处理语句创建表
sql = """CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""

cursor.execute(sql)
# 关闭数据库链接
db.close()


