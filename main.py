from flask import Flask, request, jsonify, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style, ticker
import os
from LineChart import graph
#https://www.youtube.com/watch?v=XTiM6HU0x9k

###Creamos instancia"
app = Flask(__name__)

picFodler = os.path.join("static","pics")

app.config["UPLOAD_FOLDER"] = picFodler

##primera funcion
@app.route("/", methods={"GET","POST"}) ###Es un decorador, te dice la ruta donde se quiere ejecutar la funcion
def hello():
    request_type_str = request.method 
    if request_type_str == "GET":
        # graph(ticker="AAPL")
        # picture = "static/" + "AAPL" + ".png"
        return render_template("hello.html", href = "static/AAPL.png")        
    else:
        #if is post
        tickerweb = str(request.form["text1"])
        graph(ticker=tickerweb)
        plt.switch_backend('agg')
        picture = "static/" + tickerweb + ".png"
        return render_template("hello.html", href = picture)
        # graph(ticker=ticker)
        # pic1= os.path.join(app.config["UPLOAD_FOLDER"], "pics.png")
        # return render_template("hello.html", user_image=pic1)


if __name__ =="__main__":
    app.run(debug=True)