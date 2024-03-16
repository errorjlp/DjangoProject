import requests
import json
import pymysql.cursors

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
INSERT INTO app01_cich ( bid, name, cate, year, region, institution)
VALUES (%s, %s, %s, %s, %s, %s)
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
    url = f"http://www.ihchina.cn/Article/Index/getProject.html?category_id=16&limit=10&p={num}"
    resp = requests.get(url, headers=h)

    JsonObj = json.loads(resp.text)

    try:
        for item in JsonObj["list"]:
            #序号
            #id = item["auto_id"]
            # 编号
            bid = item["num"]
            # 名称
            name = item["title"]
            #类别
            cate = item["type"]
            # 公布时间
            year = item["rx_time"].replace('</br>', '')
            # 申报地区或单位
            region = item["province"]
            # 机构
            institution = item["protect_unit"]


            # 插入数据到MySQL
            cursor.execute(insert_sql, ( bid, name, cate, year, region, institution))

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