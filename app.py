from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bd1inf132'
conexion = MySQL(app)
@app.route("/", methods=['GET', 'POST'])
def consulta_sql():
    consulta = ""
    columnas = []
    resultados = []
    mensaje = ""

    if request.method == "POST":
        consulta = request.form['consulta']
        cursor = conexion.connection.cursor()
        try:
            cursor.execute(consulta)

            if consulta.upper().startswith("SELECT"):
                resultados = cursor.fetchall()
                columnas = [col[0] for col in cursor.description]

            else:
                conexion.connection.commit()
                mensaje = "Consulta ejecutada correctamente."

        except Exception as e:

            mensaje = str(e)

        cursor.close()

    return render_template(
        "index.html",
        consulta=consulta,
        columnas=columnas,
        resultados=resultados,
        mensaje=mensaje
    )

if __name__ == "__main__":
    app.run(debug=True)

