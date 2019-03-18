
#!/usr/bin/env python

from flask import Flask, render_template, request, flash
import sqlite3
import folium
import Facade
from Place import Place
from Recherches import Recherche
from Carte import Carte

conn = sqlite3.connect(Facade.get_data_DB(),check_same_thread=False)

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('index.html',name=Facade.get_name())

@app.route("/places")

def places():
    return render_template('place.html', resto_list=Place.get_places(conn))

@app.route("/reservations")

def reservations():
    return render_template('search.html')


@app.route("/find_place", methods=['GET', 'POST'])

def find_a_place():
	cp = request.args.get('dept')


	is_find = Recherche.find_place(conn,cp)

	if is_find is  None:
		return render_template("no_place_found.html",zone=cp)

	Carte(cp).sauve(conn)

	return render_template("map.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
