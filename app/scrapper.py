import requests
import json
from bs4 import BeautifulSoup 


trending_url='https://github.com/trending'
github_url='https://github.com'

def scrape_trending_repos(language, *args, **kwargs):
    response=requests.get(trending_url+f'/{language}',headers={'User-Agent':"Mozilla/5.0"})
    if not response.status_code==200:
        return {'status':False,'data':{}}
    html_content=response.content
    bs4obj=BeautifulSoup(html_content, 'html.parser')
    all_trending_repos=bs4obj.select('article.Box-row h1')
    data=[]
    for repo in all_trending_repos:
        # print(repo.span.attr['programmingLanguage'])
        link=str(repo.a.attrs['href'])
        repo=link[1:]
        temp={'repo':repo,'url':github_url+link }
        data.append(temp)
        
    return {'status':True,'data':data}
