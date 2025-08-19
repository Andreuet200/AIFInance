
# Importem les classes i funcions necessàries de Flask
from flask import Flask, render_template, request

# Creem una instància de l'aplicació Flask
app = Flask(__name__)

# Definim una ruta per la pàgina principal
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Definim una ruta per la pàgina principal
@app.route("/main", methods=["GET", "POST"])
def main():
    #database 
    return render_template("main.html")

# Definim una ruta per la pàgina principal
@app.route("/dbs", methods=["GET", "POST"])
def dbs():
    
    return render_template("dbs.html")


# Executem l’aplicació si el fitxer és el principal
if __name__ == "__main__":
    app.run()
