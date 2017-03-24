from django.shortcuts import render
from game_search.forms import keywordForm
import pybomb, json
from random import randint
from game_search.obj import data
# Create your views here.

my_key = "6536b1ed838938215679d25613be52f3dfcab93d"
games_client = pybomb.GamesClient(my_key)

def index(request):

    return_fields = ('id', 'name', 'platforms', 'image')
    limit = 10
    offset = randint(0,20000)
    sort_by = 'name'
    filter_by = {'platforms': pybomb.PC}

    response = games_client.search(
        filter_by=filter_by,
        return_fields=return_fields,
        sort_by=sort_by,
        desc=True,
        limit=limit,
        offset=offset
    )

    results = []
    for i in response.results:
        try:
            a = data(i["name"], i['image']['small_url'])
        except TypeError:
            a=data(i["name"], "")
        #a = data(i["name"],i['image']['small_url'])
        results.append(a)


    return render(request, 'game_search/index.html', {"results":results})

def search(request):

    if request.method == 'POST':
        form = keywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
    else:
        form = keywordForm()


    response = games_client.quick_search(
        name=keyword,
        sort_by='original_release_date',
        desc=True,
    )

    results = []
    for i in response.results:
        try:
            a = data(i["name"], i['image']['small_url'])
        except TypeError:
            a=data(i["name"], "")
        #a = data(i["name"],i['image']['small_url'])
        results.append(a)



    return render(request, 'game_search/search.html', {"results":results})

def detail(request,title):


    return render(request, 'game_search/detail.html', {"title":title})