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
    cur.execute("select * from inventory")
    data = cur.fetchall()
    print(data)
    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)

# Path: templates/index.html
# create a html table to show all data from database





