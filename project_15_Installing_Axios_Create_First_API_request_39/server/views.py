from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed



# # 3) //////////// filter(category__name=cat1), quantity   ////////////////////
class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user")

        
        
        if category:        
            self.queryset = self.queryset.filter(category__name=category) 
            
        if by_user:
            user_id = request.user.id           
            self.queryset = self.queryset.filter(member=user_id)           

        if qty:
            self.queryset = self.queryset[: int(qty)]                           

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)


# # 4) //////////////////////////////////////////////////
# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all()

#     def list(self, request):        
#         by_user = request.query_params.get("by_user")
#         category = request.query_params.get("category")

#         if category:                        
#             self.queryset = self.queryset.filter(category__name=category)      

#         if by_user:
#             user_id = request.user.id
#             print(user_id)
#             print(request.user)
           
#             self.queryset = self.queryset.filter(member=user_id)
#             # print(self.queryset)

#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)


# # 5) ////////////  ////////////////////

# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all()

#     def list(self, request):
#         category = request.query_params.get("category")
#         qty = request.query_params.get("qty")
#         by_user = request.query_params.get("by_user")
#         by_serverid = request.query_params.get("by_serverid")     
        
        
#         if category:        
#             self.queryset = self.queryset.filter(category__name=category)          
     

#         if by_user:
#             user_id = request.user.id          
#             self.queryset = self.queryset.filter(member=user_id)          

      

#         if by_serverid:
#             try:
#                 self.queryset = self.queryset.filter(id=by_serverid)
#                 # print(self.queryset.exists())
#                 print(self.queryset)   #  <QuerySet [<Server: ser2-2>]>
                
#                 if not self.queryset.exists():                   
#                     raise ValidationError(detail=f"Server with id {by_serverid} not found")
#             except ValueError:
#                 raise ValidationError(detail=f"Server with id {by_serverid} not found")
            
#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)

# 6) ////////////////////////////////

# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all()

#     def list(self, request):
#         category = request.query_params.get("category")       
#         by_user = request.query_params.get("by_user")
#         by_serverid = request.query_params.get("by_serverid")
        
     
#         if not request.user.is_authenticated:
#             raise AuthenticationFailed()     
        
        
#         if category:        
#             self.queryset = self.queryset.filter(category__name=category)           
     

#         if by_user:
#             user_id = request.user.id          
#             self.queryset = self.queryset.filter(member=user_id)
        

#         if by_serverid:
#             try:
#                 self.queryset = self.queryset.filter(id=by_serverid)
                
#                 if not self.queryset.exists():                   
#                     raise ValidationError(detail=f"Server with id {by_serverid} not found")
#             except ValueError:
#                 raise ValidationError(detail=f"Server with id {by_serverid} not found")
            
#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)

       