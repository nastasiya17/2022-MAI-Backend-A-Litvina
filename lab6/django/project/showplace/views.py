from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from showplace import models

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
        <p><a href="/admin/">Доступ администратору</a></p>
    </html>
    """
    return HttpResponse(http)

@csrf_exempt 
def showplaces(request):
    if request.method == "GET": 
        showplace_id = request.GET.get("id", 8)        
        try:
            showplace = models.Showplace.objects.get(id=showplace_id)
            return JsonResponse({"id": showplace.id, "name": showplace.name, "category": showplace.category})
        except models.Showplace.DoesNotExist:
            return JsonResponse({})
        
    elif request.method == "POST":
        name = request.GET.get("name", None)
        if not name:
            return JsonResponse({"status": "Bad name param"})
        category = request.GET.get("category", None)
        
        # сохраниние в бд
        try:
            showplace = models.Showplace()
            showplace.name = name
            showplace.category = category
            
            exists = True
            try:
                _ = models.Showplace.objects.get(name=name, category = category)
            except models.Showplace.DoesNotExist:
                exists = False
            except models.Showplace.MultipleObjectsReturned:
                pass
                
            if not exists:
                showplace.save()
            return JsonResponse({"status": ("OK" if not exists else "Already exists")})
        except:
            return JsonResponse({"status": "Field error"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")

'''@csrf_exempt 
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


#@csrf_exempt 
def showplaces(request):
    if request.method == "GET":
        showplace_id = request.GET.get("showplace_id", 10)
        name = request.GET.get("name", "Памятник Ленину")
        category = request.GET.get("category", "Памятники")
        return JsonResponse({"showplace_id": showplace_id, "name": name, "category": category})
    elif request.method == "POST":
        showplace_id = request.GET.get("showplace_id", 20)
        name = request.GET.get("name", "Парк Горького")
        category = request.GET.get("category", "1")
        return JsonResponse({"showplace_id": showplace_id, "name": name, "category": category, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")
'''