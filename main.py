from flask import Flask, request, redirect, url_for, render_template

from data import data 

app = Flask(__name__)
DEPARTURES = data.departures

@app.route('/')
def index():
    return render_template('index.html',departures = DEPARTURES,tours = data.tours)


@app.route('/tour/<int:index>')
def tour(index):
    tour = data.tours.get(index)
    return render_template('tour.html',departures = DEPARTURES , tour=tour)


@app.route('/departure/<dep>/')
def departure(dep):
    tours={index:tour for index ,tour in data.tours.items() if tour["departure"] == dep}
    #tours = {}

    #for index ,tour in data.tours.items():
        #if tour["departure"] == dep:
            #tours.update({index:tour})

    return render_template('departure.html',departures = DEPARTURES,tours=tours)


if __name__ == '__main__':
    app.run(debug=True)
