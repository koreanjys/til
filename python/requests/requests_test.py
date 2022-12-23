import requests

key = '8cb1b55c87ce758e9389d6b2a2d7b92c'
url = 'https://api.themoviedb.org/3/movie/popular?api_key=8cb1b55c87ce758e9389d6b2a2d7b92c&language=ko-KR'
data = requests.get(url).json()
movies = data['results']

# data 딕셔너리 안에 results 리스트 안에 dic 이있다. dic 안에 key와 value가 있다.

def popular_count():
    return len(data['results'])


def vote_average_movies(n):
    good_movies = filter(lambda movie: movie["vote_average"] >= n, movies)
    return list(map(lambda movie: (movie["vote_average"], movie["title"]), good_movies))


def ranking(n):
    ttl_vt = list(map(lambda movie: (movie["vote_average"], movie["title"]), movies))
    ttl_vt.sort(reverse=True)
    return ttl_vt[:n]
    

def recommendation(title):
    url_2 = f'https://api.themoviedb.org/3/search/movie?api_key=8cb1b55c87ce758e9389d6b2a2d7b92c&language=ko-KR&query={title}'
    data_2 = requests.get(url_2).json()
    if not data_2['results']:
        return None
    id_num = str(data_2['results'][0]["id"])
    url_rec = f'https://api.themoviedb.org/3/movie/{id_num}/recommendations?api_key=8cb1b55c87ce758e9389d6b2a2d7b92c&language=ko-KR'
    data_rec = requests.get(url_rec).json()
    return list(map(lambda movie: movie["title"], movies))

# print(popular_count())
# print(vote_average_movies(8))
# print(ranking(5))
# print(recommendation('기생충'))