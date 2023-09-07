import requests, json

apiKey = "1d1f006b"

title = "luca"
year = "2009"
search = "adam"
url = requests.get(f"http://www.omdbapi.com/?apikey=1d1f006b&t={title}")
img = requests.get("http://img.omdbapi.com/?apikey={apiKey}&t={title}")

data = url.json()  # return files a dictionary
print(data["Response"])
#print(json.dumps(data, indent=4))  # convert data from dictionary to json using json.dumps() and indent by 4

