from django.shortcuts import render as __showWebpage
from django.http import JsonResponse as __notJsonResponse
import requests as __stseuqer
import json as __notjson

__url = 'https://www.mangaupdates.com/api/series.php'

def __getMangaDetails(__id):
    __headers = {
        'API-Version': '1.1.0',
        'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8,ja;q=0.7'
    }

    __params = (
        ('id', __id),
    )

    __response = __stseuqer.get(__url, headers=__headers, params=__params)

    __json_string = __notjson.dumps(__response.json(), ensure_ascii=False) # .encode('utf-8')

    # f = json_string.decode().replace(r'\r\n', ', ')
    __f = __json_string.replace(r'\r\n', ', ').replace('&#039;', '\'')

    __f_j = __notjson.loads(f)
    return __f_j


def api(request):
    __id = str(request.GET.get('id', 'random id')
    __user= str(request.GET('user', 'random noob')
    __pswd = str(request.GET('password', 'weak password')
    if __user in ['flamekiller','mkpro118',] and str(__pswd)=='42069':
        return __notJsonResponse(___getMangaDetails(__id))
    else:
        return __notJsonResponse({'error':'incorrect credentials', 'user' : __user, 'password' : __pswd})

def home(request):
    return __showWebpage(request, 'index.html')
