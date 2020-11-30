import requests
import mysql.connector

# v3 auth key
key = '2beb4404fb7ab95728c66da114274c20'


def get_upcoming():
    url = 'https://api.themoviedb.org/3/movie/upcoming?api_key={}&language=en-US&page=1'.format(key)
    movies = requests.get(url).json()['results']
    
    mydb = mysql.connector.connect(
        host="sql7.freemysqlhosting.net",
        user="sql7379267",
        password="rAuYPjlxvi",
        database="sql7379267"
    )
    mycursor = mydb.cursor()


    for movie in movies:
        try:
            genre_ids = ""
            for genre_id in movie['genre_ids']:
                genre_ids += str(genre_id)
                genre_ids += ","
            genre_ids = genre_ids[:-1]
            sql = "INSERT INTO upcoming_movies (id, popularity, overview, release_date, title, genre_ids, vote_average, original_language, poster_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (movie['id'], movie['popularity'], movie['overview'], movie['release_date'], movie['title'], genre_ids, movie['vote_average'], movie['original_language'] ,movie['poster_path'])
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except mysql.connector.errors.IntegrityError as e:
            print("error:", e)

    mycursor.close()
    mydb.close()
        

