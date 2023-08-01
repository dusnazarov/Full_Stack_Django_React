from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed



class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")       
        by_user = request.query_params.get("by_user")
        by_serverid = request.query_params.get("by_serverid")

        if by_user or by_serverid and not request.user.is_authenticated:
            raise AuthenticationFailed()    
        
        if category:        
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id          
            self.queryset = self.queryset.filter(member=user_id)      

        if by_serverid:
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                # print(self.queryset.exists())
                # print(self.queryset)
                if not self.queryset.exists():                   
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail=f"Server with id {by_serverid} not found")
            
        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)

