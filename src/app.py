from flask import Flask, render_template, request, redirect, url_for
import os
import db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder= template_dir)

#rutas de la app
@app.route('/')
def Home():
    cursor = db.database.cursor(dictionary=True)
    cursor.execute("select * from users")
    result = cursor.fetchall()
    cursor.close()
    print(result)
    return render_template('index.html', data=result)

#ruta para guardar usuarios en la db
@app.route('/user', methods=['POST'])
def add_user():
    username = request.form['usuario']
    password = request.form['password']
    nombre = request.form['nombre']

    if username and nombre and password:
        cursor = db.database.cursor()
        sql = "insert into users (ID, username, Nombre, password)  values(null, %s, %s, %s);"
        data = (username, password, nombre)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('Home'))

@app.route('/delete/<string:id>')
def delete_user(id):
    cursor = db.database.cursor()
    sql = "delete from users where id=%s;"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('Home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit_user(id):
    username = request.form['usuario']
    password = request.form['password']
    nombre = request.form['nombre']

    if username and nombre and password:
        cursor = db.database.cursor()
        sql = "update users set username = %s, Nombre = %s, password = %s where id = %s;"
        data = (username, password, nombre, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('Home'))

#database password: federico546
if __name__ == '__main__':
    app.run(debug=True, port=4000)
