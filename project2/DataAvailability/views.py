from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import (
    CourtAvailabilitySerializer,
    CreateUpdateCourtAvailabilitySerializer,
    CreateUpdateProfileAvailabilitySerializer,
    ProfileAvailabilitySerializer

)

from .models import (
    ProfileAvailabilities,
    CourtAvailabilities

)


# Create your views here.

############PROFILE AVAILABILITY#########

class ProfileAvailabilityView(APIView):
    serializer_class = CreateUpdateProfileAvailabilitySerializer

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        profile_available_objs = ProfileAvailabilities.objects.all()
        serializer = ProfileAvailabilitySerializer(profile_available_objs, many=True)
        response['data'] = serializer.data  # type: ignore

        return Response(response)

    def get_second(self, request, *args, **kwargs):
        response = {'status': 200}
        data = request.data

        profile_available_objs = ProfileAvailabilities.objects.get(id=data.get('id'))
        serializer = ProfileAvailabilitySerializer(profile_available_objs, data=data, partial=True)

        response['data'] = serializer.data  # type: ignore
        return Response(response)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateUpdateProfileAvailabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "profile available  Data Added"}
            return Response(response)

        return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):

        response = {'status': 200}
        data = request.data
        try:
            obj = ProfileAvailabilities.objects.get(id=data.get('id'))
            serializer = CreateUpdateProfileAvailabilitySerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data  # type: ignore
                return Response(response)
            else:
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': 'invalid id'})

    def delete(self, request, *args, **kwargs):
        response = {'status': 200}
        data = request.data
        try:
            obj = ProfileAvailabilities.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status': 200, 'message': "Deleted"})
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': "Invalid id"})


############Court AVAILABILITY#########


class CourtAvailabilityView(APIView):
    serializer_class = CreateUpdateCourtAvailabilitySerializer

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        court_available_objs = CourtAvailabilities.objects.all()
        serializer = CourtAvailabilitySerializer(court_available_objs, many=True)
        response['data'] = serializer.data  # type: ignore

        return Response(response)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CreateUpdateCourtAvailabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Court Detail Data Added"}
            return Response(response)

        return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):

        response = {'status': 200}
        data = request.data
        try:
            obj = CourtAvailabilities.objects.get(id=data.get('id'))
            serializer = CreateUpdateCourtAvailabilitySerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data  # type: ignore
                return Response(response)
            else:
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': 'invalid id'})

    def delete(self, request, *args, **kwargs):
        response = {'status': 200}
        data = request.data
        try:
            obj = CourtAvailabilities.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status': 200, 'message': "Deleted"})
        except Exception as e:
            print(e)
        return Response({'status': 400, 'message': "Invalid id"})
