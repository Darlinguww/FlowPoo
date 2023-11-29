from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

# Lógica para crear la tabla en la base de datos
def create_table():
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")

        
        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Crear la tabla si no existe
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                          Name TEXT,
                          Salary INTEGER)""")
        
        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()
        
        print("Tabla creada correctamente.")
    except sql.Error as e:
        print("Error en la base de datos:", e)

# Llamada a la función para crear la tabla
create_table()

# Lógica para actualizar la base de datos
def update_database(supervisor_name, new_salary):
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")

        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Ejecutar la actualización
        cursor.execute("UPDATE usuarios SET Salary = ? WHERE Name = ?", (new_salary, supervisor_name))

        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()

        print("Salario actualizado correctamente.")
    except sql.Error as e:
        print("Error en la base de datos:", e)

# Lógica para agregar un supervisor a la base de datos
def add_supervisor(name, salary):
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")

        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Ejecutar la inserción
        cursor.execute("INSERT INTO usuarios (Name, Salary) VALUES (?, ?)", (name, salary))

        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()

        print("Supervisor agregado correctamente.")
    except sql.Error as e:
        print("Error en la base de datos:", e)

# Lógica para eliminar un supervisor de la base de datos
def delete_supervisor(name):
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")

        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Ejecutar la eliminación
        cursor.execute("DELETE FROM usuarios WHERE Name = ?", (name,))

        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()

        print("Supervisor eliminado correctamente.")
    except sql.Error as e:
        print("Error en la base de datos:", e)

# Ruta para la página principal
@app.route('/')
def index():
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")

        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Obtener los datos de los supervisores
        cursor.execute("SELECT Name, Salary FROM usuarios")
        supervisors_data = cursor.fetchall()

        # Cerrar la conexión
        con.close()

        return render_template('Salarios.html', supervisors=supervisors_data)



    except sql.Error as e:
        print("Error en la base de datos:", e)
        return "Error en la base de datos"


# Ruta para la actualización de salario
@app.route('/update_salary', methods=['POST'])
def update_salary():
    supervisor_name = request.form.get('name')
    new_salary = request.form.get('new_salary')

    # Llamada a la función para actualizar la base de datos
    update_database(supervisor_name, new_salary)

    return redirect(url_for('index'))

# Ruta para agregar un supervisor
@app.route('/add_supervisor', methods=['POST'])
def add_supervisor_route():
    name = request.form.get('name')
    salary = request.form.get('salary')

    # Llamada a la función para agregar un supervisor a la base de datos
    add_supervisor(name, salary)

    return redirect(url_for('index'))

# Ruta para eliminar un supervisor
@app.route('/delete_supervisor', methods=['POST'])
def delete_supervisor_route():
    supervisor_name = request.form.get('name')

    # Llamada a la función para eliminar un supervisor de la base de datos
    delete_supervisor(supervisor_name)

    return redirect(url_for('index'))

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
