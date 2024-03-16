import requests
import json
import pymysql.cursors
#问题：爬虫requests请求时发生如下错误  0 bytes read
#1.修改python源码，把报错去掉（去掉后如果你的代码没有问题，就可以传输了）
#2.使用http1.0来进行request
#3.不用requests，用python curl等等。
#4.也许更新python的requests库会有用。
#5.加版本声明：
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

# MySQL连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mb030127',
    'database': 'ich',
}

# 连接数据库
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# SQL插入语句
insert_sql = """
INSERT INTO app01_pich ( id,name,gender,nation,category,bid,pname,region)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# 请求头
h = {
    "Host": "www.ihchina.cn",
    "Referer": "http://www.ihchina.cn/project",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.159 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def get_info(num):
    url = f"https://www.ihchina.cn/art/representative.html?province=&rx_time=&type=&sex=&keywords=&limit=10&p={num}"
    resp = requests.get(url, headers=h)

    JsonObj = json.loads(resp.text)

    try:
        for item in JsonObj["list"]:
            #序号
            #id = item["auto_id"]
            # 编号
            id = item["num"]
            # 名称
            name = item["title"]
            # 性别
            gender = item["sex"]
            # 民族
            nation = item["nation"]
            # 类别
            category = item["type"]
            # 编号
            bid = item["project_num"]
            # 项目名称
            pname = item["project"]
            # 省份
            region = item["province"]


            # 插入数据到MySQL
            cursor.execute(insert_sql, ( id,name,gender,nation,category,bid,pname,region))

        # 提交事务
        connection.commit()

    except KeyError as e:
        print(f"发生错误: {e}")
        return 'error'


if __name__ == '__main__':
    i = 1
    while True:
        if get_info(i) != 'error':
            print(i, 'ok')
        else:
            break
        i += 1

    # 关闭数据库连接
    cursor.close()
    connection.close()

    print('全部ok')