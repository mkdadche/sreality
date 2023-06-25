# import subprocess
# from flask import Flask, render_template
# import psycopg2
# app = Flask(__name__)

# def run_command(cmd):
#     project_path = "C:\\Users\\mkalshibani\\Documents\\srealtyscraptask\\src\\scarpper\\sreality"
#     return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, cwd=project_path)

# @app.route("/")
# def home():
#     hostname = '127.0.0.1'
#     port = '5432'
#     database = 'sreality'
#     username = 'postgres'
#     password = ''

#     connection = psycopg2.connect(
#         host=hostname,
#         port=port,
#         dbname=database,
#         user=username,
#         password=password
#     )
#     cursor = connection.cursor()

#     cursor.execute("SELECT title, locality, images FROM offers")
#     items = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return render_template('home.html', offers=items)

# @app.route("/refresh-offers")
# def refresh_offers():
#     x = run_command("scrapy crawl sreality_spider")
#     return "currently scrapping"
#     # return "scrrap data"

# if __name__ == "__main__" : 
#     #Remove this
#     #app.run()
#     app.run(host='0.0.0.0', port=8080)




import subprocess
from flask import Flask, render_template, redirect, url_for
import psycopg2
import threading
app = Flask(__name__)

def run_command(cmd):
    project_path = "C:\\Users\\mkalshibani\\Documents\\srealtyscraptask\\src\\scarpper\\sreality"
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, cwd=project_path)

@app.route("/")
def home():
    hostname = '127.0.0.1'
    port = '5432'
    database = 'sreality'
    username = 'postgres'
    password = ''

    connection = psycopg2.connect(
        host=hostname,
        port=port,
        dbname=database,
        user=username,
        password=password
    )
    cursor = connection.cursor()

    cursor.execute("SELECT title, locality, images FROM offers")
    items = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('home.html', offers=items)

@app.route("/refresh-offers")
def refresh_offers():
    print("hello")
    x = run_command("scrapy crawl sreality_spider")
    return redirect(url_for('home'))
     
    # return "scrrap data"

if __name__ == "__main__" : 
    #Remove this
    #app.run()
    app.run(host='0.0.0.0', port=8080)