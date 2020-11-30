import requests
import mysql.connector
import json

# youtube key
key = 'AIzaSyBpMyq8TYlXYhdzTZ26936WPPyy13b7hvQ'


def connect():
    cnx = mysql.connector.connect(
        user='admin',
        password='filmdigger',
        host='rds-mysql.cwkwgvkea1uk.us-east-2.rds.amazonaws.com',
        database='filmdiggerDB')
    return cnx


def get_trailers():
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=30&order=relevance&q=trailer&regionCode=US&relevanceLanguage=EN&topicId=%2Fm%2F02vxn&type=video&key={}'.format(
        key)
    items = requests.get(url).json()['items']
    cnx = connect()
    cursor = cnx.cursor()
    sql = "DELETE FROM trailers;"
    cursor.execute(sql)
    sql = "INSERT INTO trailers (videoId, title, published) VALUES (%s, %s, %s)"
    for item in items:
        val = (item['id']['videoId'], item['snippet']
               ['title'], item['snippet']['publishedAt'])
        cursor.execute(sql, val)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("30 minutes")


def select_trailers():
    cnx = connect()
    cursor = cnx.cursor(dictionary=True)
    sql = "SELECT * FROM trailers ORDER BY published DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    cnx.close()
    return json.dumps(results)
