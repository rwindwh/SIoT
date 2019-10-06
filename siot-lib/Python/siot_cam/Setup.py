import sqlite3
import datetime
DATABASE = 'data/data.db'
def setup_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sensorlog(logid INTEGER PRIMARY KEY autoincrement,sensor1 float,base64 varchar,datatime varchar)")
    db.commit()
    cur.execute("SELECT COUNT(*) FROM sensorlog")
    if cur.fetchall()[0][0] == 0:
        cur.execute("INSERT INTO sensorlog(logid,sensor1,base64,datatime) VALUES(1,21,'/base64','2019-05-25 24:00:00')")
        db.commit()
if __name__ == "__main__":
  setup_db()
