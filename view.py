from flask import Flask, render_template, json, flash, request
import requests as rq

app = Flask(__name__)


def errorMessage():
    apiKey = json.load(open("credentials.json"))
    get_api_key = apiKey['apikey']
    data = get_api_key.json()

    return data["Response"]


@app.route('/', methods=['GET', 'POST'])
def home():
    apiKey = json.load(open("credentials.json"))
    get_api_key = apiKey['apikey']
    # Retriving the data information from the movie api
    if request.method == "POST":
        movie_title = request.form.get("movie_search")
        api_url = rq.get(f"http://www.omdbapi.com/?apikey={get_api_key}&t={movie_title}")

        # Catching Error based on the wrong movin title name provide
        if api_url.json()['Response'] == "True":
            return render_template('home.html',
                                   title=api_url.json()["Title"],
                                   plot=api_url.json()["Plot"],
                                   # rated=api_url.json()["Rated"],
                                   type=api_url.json()["Type"].capitalize(),
                                   released_date=api_url.json()["Released"],
                                   movie_duration=api_url.json()["Runtime"],
                                   genre=api_url.json()["Genre"],
                                   country=api_url.json()["Country"],
                                   director=api_url.json()["Director"],
                                   writer=api_url.json()["Writer"],
                                   actors=api_url.json()["Actors"],
                                   image=api_url.json()["Poster"],

                                   )
        else:
            return render_template('home.html',
                                   response="The name of the movie you type is not correct, please enter another name")


if __name__ == '__main__':
    app.run(debug=True)
