from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_supervisors():
    supervisors = []
    with open('supervisores.txt', 'r') as file:
        for line in file:
            data = line.split('/')
            supervisors.append([data[0], data[1], data[3], data[4]])
    return supervisors

@app.route('/')
def index():
    return render_template('index_Gerente.html')

@app.route('/delete_super', methods=['GET', 'POST'])
def delete_super():
    if request.method == 'POST':
        name = request.form['name']
        with open('supervisores.txt', 'r') as file:
            lines = file.readlines()
        with open('supervisores.txt', 'w') as file:
            for line in lines:
                if not line.startswith(f"{name}/"):
                    file.write(line)
        # Redirige nuevamente a la página de eliminación después de la operación
        return redirect(url_for('index'))

    # Si la solicitud es GET, simplemente renderiza la plantilla de eliminación
    return render_template('Delete_Super.html')

@app.route('/add_super', methods=['GET', 'POST'])
def add_super():
    if request.method == 'POST':
        name = request.form['name']
        salary = request.form['salary']
        with open('supervisores.txt', 'a') as file:
            file.write(f"\n{name}/{name}@example.com/contraseña/{salary}/Supervisor")
        return redirect(url_for('index'))

    return render_template('Add_Super.html')

@app.route('/salaries', methods=['GET', 'POST'])
def manage_salaries():
    if request.method == 'POST':
        name_to_update = request.form.get('name_to_update')
        new_salary = request.form.get('new_salary')
        with open('supervisores.txt', 'r') as file:
            lines = file.readlines()
        with open('supervisores.txt', 'w') as file:
            for line in lines:
                if line.startswith(f"{name_to_update}/"):
                    updated_line = f"{name_to_update}/{line.split('/')[1]}/{line.split('/')[2]}/{new_salary}/{line.split('/')[4]}"
                    file.write(updated_line)
                else:
                    file.write(line)
        return redirect(url_for('manage_salaries'))

    supervisors = get_supervisors()
    return render_template('Salarios.html', supervisors=supervisors)

if __name__ == '__main__':
    app.run(debug=True)
