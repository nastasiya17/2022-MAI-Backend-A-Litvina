from django.contrib.auth.models import User

try: 
    User.objects.create_superuser('anast', 'anast@mail.ru', 'password')
except:
    pass