import tushare as ts
import pymysql
token = '39eb03a5cc204699bd6338d9ae4cd1d11289f653ddfe4dd061c5c363'
pro = ts.pro_api(token)

stock_exchange = ['SSE', 'SZSE']
data = []
for exchange in stock_exchange:
    df = pro.trade_cal(exchange=exchange, start_date='2020101', end_date='20210101')
    data.append(df)

conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql@1803', charset='gbk')
cur = conn.cursor()
SQL1 = '''
CREATE DATABASE tushare charset='gbk';
'''

SQL2 = '''
CREATE table tushare.trade_cal(
`exchange` varchar(100),
`cal_date` date,
`is_open` bit,
`pretrade_date` date
);
'''

for df in data:
    for index, row in df.iterrows():
        row = list(row)
        SQL3 = '''
        INSERT INTO tushare.trade_cal (exchange, cal_date, is_open) VALUES (%s, %s, %s);
        '''
        cur.execute(SQL3, row)

conn.commit()
cur.close()
conn.close()
# cur.execute(SQL1)
# cur.execute(SQL2)
