from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.db import IntegrityError

from myapp.models import Todo
from myapp.serializers import TodoSerializer
import bcrypt



@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
def create_account(request):
    salt = bcrypt.gensalt()
    try:
        #CREATE ACCOUNT
        if request.data:
            todo = Todo(name=request.data['name'],
                        email=request.data['email'],
                        password=bcrypt.hashpw(request.data['password'].encode('utf8'), salt).decode('utf8'),
                        )
            todo.save()


            return Response({
                "status": "success",
                "message": "Account created, check your registered email for verification.",
                "profile": TodoSerializer(todo).data
            })
        else:
            return Response({"status": "failed", "message": "Account not created"})

    except IntegrityError:
        return Response({"status": "failed", "message": "User already exists proceed with login"})
    except Exception as exception:
        return Response({"status": "failed", "message": str(exception)})


#LOGIN
@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])
def login(request):
    try:

        if request.data:
            todo = TodoSerializer.objects.get(email=request.data['email'])
            if not bcrypt.checkpw(request.data['password'].encode('utf8'), todo.password.encode('utf8')):
                return Response({
                    "status": "failed",
                    "message": "The password entered is incorrect."
                })
            else:
                return Response({
                    "status": "success",
                    "message": "Login successful",
                    "profile": TodoSerializer(todo).data
                })
        else:
            return Response({"status": "failed", "message": "Invalid user role"})
    except KeyError:
        return Response({"status": "failed", "message": "Invalid data provided"})
    except IntegrityError:
        return Response({"status": "failed",
                         "message": "The email address entered is not associated with the indicated form account type."
                         })
    except Exception as exception:
        return Response({"status": "failed", "message": str(exception)})