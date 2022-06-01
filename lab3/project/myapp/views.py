from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def index(request):
    http = \
    """
    <html lang="ru">
    <head>
        <title>Веб-сервер</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
    </head>
    <body>
        <h1> Hello, it's Jango!</h1>
    </html>
    """
    return HttpResponse(http)

@csrf_exempt 
def profile(request):
    if request.method == "GET":
        login = request.GET.get("login", "user")
        password = request.GET.get("password", "password")
        return JsonResponse({"login": login, "password": password})
    elif request.method == "POST":
        login = request.GET.get("login", "user2")
        password = request.GET.get("password", "useruser")
        return JsonResponse({"login": login, "password": password, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

@csrf_exempt 
def showplaces(request):
    if request.method == "GET":
        showplace_id = request.GET.get("showplace_id", 10)
        sh_name = request.GET.get("sh_name", "Памятник Ленину")
        sh_category = request.GET.get("sh_category", "Памятники")
        return JsonResponse({"showplace_id": showplace_id, "sh_name": sh_name, "sh_category": sh_category})
    elif request.method == "POST":
        showplace_id = request.GET.get("showplace_id", 20)
        sh_name = request.GET.get("sh_name", "Парк Горького")
        sh_category = request.GET.get("sh_category", "Парки")
        return JsonResponse({"showplace_id": showplace_id, "sh_name": sh_name, "sh_category": sh_category, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")
