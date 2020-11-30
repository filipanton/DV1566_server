import requests

# v3 auth key
key = '2beb4404fb7ab95728c66da114274c20'

def get_upcoming():
    url = 'https://api.themoviedb.org/3/movie/upcoming?api_key={}&language=en-US&page=1'.format(key)
    movies = requests.get(url).json()['results']

    for movie in movies:
        print(movie['title'])