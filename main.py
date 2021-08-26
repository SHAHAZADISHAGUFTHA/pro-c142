from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv')  as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
unliked_movies = []
unwatched_movies = []
app = Flask(__name__)

@app.route('/get-movie')
def get_movies():
    return jsonify({
        "data":all_movies[0],
        "message": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "message":"success"
    }),201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unwatched_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()