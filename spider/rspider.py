import requests
from bs4 import BeautifulSoup
import pymysql


# 函数：获取页面HTML
def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(e)
        return None


# 函数：解析HTML并提取数据
def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 找到所有的表格行
    table_rows = soup.find_all('tr', {'class': None})

    for row in table_rows:
        cells = row.find_all('td')

        if cells:
            city = cells[1].text.strip()
            location = cells[2].text.strip()
            category = cells[3].text.strip()
            name = cells[4].text.strip()

            yield (city, location, category, name)


# 函数：将数据插入MySQL数据库
def insert_to_mysql(city, location, category, name):
    # 更改这些值以匹配你的MySQL设置
    host = 'localhost'
    user = 'root'
    password = 'mb030127'
    db = 'ich'

    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO app01_lich (city, location, category, name) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (city, location, category, name))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# 主程序
def main():
    url = 'https://www.ihchina.cn/shifanjidi.html'  # 请替换为实际的URL
    html = get_html(url)

    if html:
        data = parse_data(html)
        for item in data:
            insert_to_mysql(*item)


if __name__ == '__main__':
    main()