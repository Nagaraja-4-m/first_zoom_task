from django.shortcuts import render
from .scrapper import scrape_trending_repos
# Create your views here.
tmp_base_dir='app/'

languages=['c','c++','c#','dart','go','java','javascript','php','python','ruby','scala','typescript',
]


def  dashboard(request):
    data={'languages':languages}
    lang_selected=request.GET.get('language')
    # print(data)
    if lang_selected is not None:
        scrp_response=scrape_trending_repos(lang_selected)
        if scrp_response['status']==True:
            data['repos_data']=scrp_response['data']
            print(data)
    else:
        print("language not selected")
    # print(User.objects.all())
    return render(request,tmp_base_dir+'dashboard.html' ,data)
