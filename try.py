from bs4 import BeautifulSoup
import requests
def get_movie():
    headers = {
        'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
    }
    movie_list=[]
    for i in range(1,10):
        url = 'https://movie.douban.com/top250?start='+str(i*25)
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        #print(r.text)
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list
movie=get_movie()
print(movie)


