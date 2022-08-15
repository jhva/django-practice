from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from .models import User

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        # serializer = MenuSerializer(menu, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'user/user_list.html', {'user_list': user})
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, ststus=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        print(User.objects.all().get(user_name=user_name))

        try:
            request.session['user_id'] = User.objects.all().get(user_name=user_name).id
            print(request.session['user_id'])
            return render(request, 'user/success.html')
        except:
            return render(request, 'user/fail.html')

    elif request.method == 'GET':
        return render(request, 'user/login.html')
