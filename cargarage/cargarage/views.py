from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


class AuthView:

    @csrf_exempt
    def custom_login(request):
        if request.method == "POST":
            data = json.loads(request.body)
            required_fields = ["username", "password"]
            for field in required_fields:
                if field not in data or not data[field]:
                    return JsonResponse(
                        {"error": f"'{field}' is required."}, status=400
                    )
            username = data["username"].strip()
            password = data["password"].strip()
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"errors": "Invalid login"}, status=400)
        else:
            return JsonResponse({"error": "Only POST method allowed"}, status=405)
