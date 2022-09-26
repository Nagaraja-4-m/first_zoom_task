from django.shortcuts import render
from .scrapper import scrape_trending_repos
# Create your views here.
tmp_base_dir='app/'

languages=['c','c++','c#','dart','go','java','javascript','php','python','ruby','scala','typescript',
]


def  dashboard(request):
    data={'languages':languages}
    lang_selected=request.GET.get('language')
    if lang_selected is not None:
        data['language']=lang_selected
        scrp_response=scrape_trending_repos(lang_selected)
        if scrp_response['status']==True:
            data['repos_data']=scrp_response['data']
    else:
        pass
    return render(request,tmp_base_dir+'dashboard.html' ,data)
