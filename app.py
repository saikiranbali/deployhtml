# create a flask application to show all data from database in html table




from flask import Flask, render_template
import psycopg2
app = Flask(__name__)
@app.route('/')
def index():
    conn = psycopg2.connect(
    host="database-crm.cazl4vulkacd.ap-south-1.rds.amazonaws.com",
    database="database_crm",
    user="database_gg_crm",
    password="Crmpostgres123")
    # create a cursor

    cur = conn.cursor()
    cur.execute("select * from inventory WHERE sku LIKE 'BLR%'")
    data = cur.fetchall()

    cur1 = conn.cursor()
    cur1.execute("select * from inventory WHERE sku LIKE 'MUM%'")
    data1 = cur1.fetchall()

    cur2 = conn.cursor()
    cur2.execute("select * from inventory WHERE sku LIKE 'HYD%'")
    data2 = cur2.fetchall()

    cur3 = conn.cursor()
    cur3.execute("select * from inventory WHERE sku LIKE 'CHN%'")
    data3 = cur3.fetchall()
    print(data)
    return render_template('index.html', data=data, data1=data1, data2=data2, data3=data3)
if __name__ == '__main__':
    app.run(debug=True)

# Path: templates/index.html
# create a html table to show all data from database





