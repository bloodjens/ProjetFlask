from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'studio'
}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/example', methods=['POST'])
def example_post():
    # Accéder aux données envoyées avec la requête POST
    email = request.form.get('email')
    passe = request.form.get('pass')


    mydb = mysql.connector.connect(**db_config)
    # Faire quelque chose avec les données
    
    cursor = mydb.cursor()

    # Exécuter la requête d'insertion
    sql = "INSERT INTO utilisateur (email, pass) VALUES (%s, %s)"
    values = (email, passe)
    d = cursor.execute(sql, values)
    print(str(d)+" valeur")
    

    # Valider la transaction
    mydb.commit()
    
    # Fermer le curseur et la connexion à la base de données
    cursor.close()
    mydb.close()

    
    
    return render_template("index.html", r="1")


if __name__ == '__main__':
    app.run(debug=True)