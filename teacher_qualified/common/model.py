import pymysql
from . import config


class Model:
    """单表信息操作类"""
    # 表名
    tab_name = None
    # 数据库连接对象
    link = None
    # 游标对象
    cursor = None
    # 表的主键名
    pk = None
    # 当前表的字段名列表
    fields = []

    def __init__(self, table, config=config):
        """构造方法：初始化表名，连接数据库"""
        try:
            self.tab_name = table
            self.link = pymysql.connect(host=config.HOST, user=config.USER, password=config.PASSSWD, db=config.DBNAME,
                                        port=config.PORT, charset='utf8')
            # 让返回结果为字典模式
            self.cursor = self.link.cursor(pymysql.cursors.DictCursor)
            # 调用内部方法，加载当前表的字段信息
            self.__loadFields()
        except Exception as err:
            print("数据操作对象初始化失败，原因：%s" % err)

    def __del__(self):
        """关闭对象和连接对象"""
        if self.cursor is not None:
            self.cursor.close()
        if self.link is not None:
            self.link.close()

    def __loadFields(self):
        """加载当前的表的字段信息，内部私有方法"""
        sql = "show columns from %s" % self.tab_name
        self.cursor.execute(sql)
        dlist = self.cursor.fetchall()
        # 遍历所有字段信息
        for v in dlist:
            # 收集每个字段名称
            self.fields.append(v['Field'])
            # 判断并收集表的主键名称
            if v['Key'] == 'PRI':
                self.pk = v['Field']
                print(self.pk)

    def exeSQL(self, sql):
        """执行给定的sql语句"""
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print("SQL查询错误,原因: %s" % err)

    def find(self, no):
        """获取当前表的所有信息，没有信息返回[]"""
        try:
            sql = 'select * from %s where no= %s' % (self.tab_name, no)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print("SQL查询错误,原因: %s" % err)

    def findAll(self):
        """获取当前表的所有信息，没有信息返回[]"""
        try:
            sql = 'select * from %s' % self.tab_name
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print("SQL查询错误,原因: %s" % err)

    def save(self, data={}):
        """信息添加方法"""
        # SQL语句：insert into 表名（字段列表） values（值列表）
        try:
            # 组装SQL语句
            keys = []
            values = []
            for k, v in data.items():
                # 获取有效字段
                if k in self.fields:
                    keys.append(k)
                    values.append(v)
            sql = "insert into %s(%s) values(%s)" % (self.tab_name, ','.join(keys), ','.join(['%s'] * len(values)))
            self.cursor.execute(sql, tuple(values))
            # 提交事务
            self.link.commit()
            # 返回行的自增id号
            return self.cursor.rowcount
        except Exception as err:
            print("SQL执行错误,原因: %s" % err)
            return 0

    def update(self, data={}):
        """信息修改方法"""
        # SQL语句：insert into 表名（字段列表） values（值列表）
        try:
            # 组装SQL语句
            values = []
            for k, v in data.items():
                # 获取有效字段
                if (k in self.fields) and (k != self.pk):
                    # 判断其不是主键
                    values.append("%s='%s'" % (k, v))
            sql = "update %s set %s where %s = '%s'" % (self.tab_name, ','.join(values), self.pk, data.get(self.pk))
            print(sql)
            self.cursor.execute(sql)
            # 提交事务
            self.link.commit()
            # 返回影响行数
            return self.cursor.rowcount
        except Exception as err:
            print("SQL执行错误,原因: %s" % err)
            return 0

    def delete(self, id=0):
        """信息删除方法"""
        try:
            sql = "delete from %s where %s = %s" % (self.tab_name, self.pk, id)
            self.cursor.execute(sql)
            self.link.commit()
            return self.cursor.rowcount
        except Exception as err:
            print("SQL删除错误: %s" % err)
            return 0

    def count(self, attribute, data):
        """信息查询方法"""
        try:
            sql = "select count(*) num from %s where %s = '%s'" % (self.tab_name, attribute, data)
            print(sql)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print("SQL查询错误: %s" % err)
            return 0
