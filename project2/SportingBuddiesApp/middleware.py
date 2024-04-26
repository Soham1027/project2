from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from project2.settings import SECRET_KEY
from .models import UserDatas
import jwt  # type: ignore


class MiddelewareToken(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):

        if request.path.startswith("/api/register/") or request.path.startswith(
                "/api/login/") or request.path.startswith("/admin/"):
            return None
        auth_header = request.headers.get('Authorization')
        print("\nauth", auth_header)
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Invalid'}, status=200)
        token = auth_header.split(' ')[1]
        # token = request.GET.get('token')

        print("\nADSFsd", token)
        try:
            payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256'])

            print("Aispayload", payload)

            # user = UserDatas.objects.get(id=payload['user_id'])

            print("user:", payload['user_id'])

            request.META['HTTP_USER_ID'] = payload['user_id']

        except jwt.ExpiredSignatureError:
            return JsonResponse({'Error': ' expired token'}, status=400)
        except jwt.InvalidTokenError:
            return JsonResponse({'Error': ' Invalid token'}, status=400)
        except UserDatas.DoesNotExist:
            return JsonResponse({'Error': ' user not exists'}, status=400)
       
        except Exception as e:
            print(f"Unknown Error:{e}")
            return JsonResponse({"error": "server error"}, status=400)
