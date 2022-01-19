from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics,mixins
from .serializer import *
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication,BaseAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# class LocationAPIView(APIView):
#     def get(self,request):
#         location = Location.objects.all()
#         serializer = LocationSerializer(location, many = True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = LocationSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LocationDetailsAPIView(APIView):
#     def get_object(self,id):
#         try:
#             return Location.objects.get(id=id)
#         except Location.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         location = self.get_object(id)
#         serializer = LocationSerializer(location)
#         return Response(serializer.data)

#     def put(self,request,id):
#         location = self.get_object(id)
#         serializer = LocationSerializer(location,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         location = self.get_object(id)
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class EventAPIView(APIView):

    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        event = Event.objects.all()
        # serializer = Event_memberSerializer(Event_member.objects.filter(user=request.user),many=True).data
        serializer = EventSerializer(event, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventUserAPIView(APIView):
    # def get_object(self,userid):
        
        # try:
        #     return Event.objects.filter(userid=userid)
        # except Event.DoesNotExist:
        #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,user):
        event = Event.objects.filter(user=user)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)        

class EventDetailsAPIView(APIView):

    # authentication_classes = [SessionAuthentication, BaseAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self,id):
        try:
            return Event.objects.get(id=id)
        except Event.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        event = self.get_object(id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self,request,id):
        event = self.get_object(id)
        serializer = EventSerializer(event,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        event = self.get_object(id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
