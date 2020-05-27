from MySQLdb import _mysql

def db_sample():
  con = _mysql.connect(
    user='db user',
    passwd='db password',
    host='localhost',
    db='sample',
    charset='utf8'
  )

  cur = con.cursor()

  sql = 'select id, body, post_code, created from posts'
  cur.execute(sql)

  rows = cur.fetchall()

  for row in rows:
    print(row)

  cur.close()
  con.close()

if __name__ == '__main__':
  db_sample()