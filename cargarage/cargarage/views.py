from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import json
import re


class AuthView:

    @csrf_exempt
    def custom_register(request):
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                first_name = data.get("first_name", "").strip()
                last_name = data.get("last_name", "").strip()

                if not username or not password or not email:
                    return JsonResponse(
                        {"error": "Username, email, and password are required."},
                        status=400,
                    )

                if not re.match(r"^\w+$", username):
                    return JsonResponse(
                        {"error": "Username must be alphanumeric."}, status=400
                    )

                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    return JsonResponse({"error": "Invalid email address."}, status=400)

                if len(password) < 8:
                    return JsonResponse(
                        {"error": "Password must be at least 8 characters long."},
                        status=400,
                    )

                if User.objects.filter(username=username).exists():
                    return JsonResponse(
                        {"error": "Username already taken."}, status=400
                    )

                if User.objects.filter(email=email).exists():
                    return JsonResponse(
                        {"error": "Email already registered."}, status=400
                    )

                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                return JsonResponse(
                    {
                        "message": "User registered successfully.",
                        "user": {
                            "id": user.id,
                            "username": user.username,
                            "email": user.email,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                        },
                    },
                    status=201,
                )

            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON format."}, status=400)

            except ValidationError as e:
                return JsonResponse({"error": e.message_dict}, status=400)

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": "Only POST method is allowed."}, status=405)

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
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                return JsonResponse({"errors": "Invalid login"}, status=400)
        else:
            return JsonResponse({"error": "Only POST method allowed"}, status=405)

    @login_required
    def custom_logout(request):
        if request.method == "DELETE":
            logout(request)
            return JsonResponse(
                {"message": "You have successfully logged out."}, status=200
            )
        else:
            return JsonResponse({"error": "Only DELETE method allowed"}, status=405)
