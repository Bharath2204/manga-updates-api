from django.http import JsonResponse
import requests
import json

def getMangaDetails(id):
    headers = {
        'API-Version': '1.1.0',
        'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8,ja;q=0.7'
    }

    params = (
        ('id', id),
    )

    response = requests.get('https://www.mangaupdates.com/api/series.php', headers=headers, params=params)

    json_string = json.dumps(response.json(), ensure_ascii=False) # .encode('utf-8')

    # f = json_string.decode().replace(r'\r\n', ', ')
    f = json_string.replace(r'\r\n', ', ').replace('&#039;', '\'')

    f_j = json.loads(f)
    return f_j


def api(request):
    id=request.GET['id']
    return JsonResponse(getMangaDetails(id))
