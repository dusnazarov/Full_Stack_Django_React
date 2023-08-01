from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed


# # 1) ///////////  filter(category=category)  /////////////////////
# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all() 
#     # print(queryset)   # <QuerySet [<Server: ser1-1>, <Server: ser2-2>, <Server: se3-3>, <Server: ser4-4>, <Server: ser5-5>]>

#     def list(self, request):
#         # print(dir(self.request))
#         category = request.query_params.get("category")
#         # print(request.query_params)  # <QueryDict: {'category': ['1']}>
#         # print(category)              # 1
        
#         if category:
#             self.queryset = self.queryset.filter(category=category)       # http://127.0.0.1:8000/api/server/select/?category=1
#             # print(self.queryset)     # <QuerySet [<Server: ser1>, <Server: ser2>]>
        
#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)
    

# # 2) /////////// filter(category__name=cat1)  /////////////////////

# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all()

#     def list(self, request):
#         category = request.query_params.get("category")       

#         # print(request.query_params)         # <QueryDict: {'category': ['cat1']}> 
#         # print(category)                     # cat1
        
#         if category:        
#             self.queryset = self.queryset.filter(category__name=category)   # http://127.0.0.1:8000/api/server/select/?category=cat1
#             # print(self.queryset)           # <QuerySet [<Server: ser1>, <Server: ser2>]>

#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)

# # 3) //////////// filter(category__name=cat1), quantity   ////////////////////

# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all()

#     def list(self, request):
#         category = request.query_params.get("category")
#         qty = request.query_params.get("qty")

#         # print(request.query_params)      #  <QueryDict: {'category': ['cat1'], 'qty': ['2']}>
#         # print(category, qty)             #  cat1 2
        
        
#         if category:        
#             self.queryset = self.queryset.filter(category__name=category)            

#         if qty:
#             self.queryset = self.queryset[: int(qty)]             # http://127.0.0.1:8000/api/server/select/?category=cat2&qty=1           

#             # print(self.queryset)             # <QuerySet [<Server: ser1>, <Server: ser2>]>      

#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)


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

class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")       
        by_user = request.query_params.get("by_user")
        by_serverid = request.query_params.get("by_serverid")
        
     
        if not request.user.is_authenticated:
            raise AuthenticationFailed()     
        
        
        if category:        
            self.queryset = self.queryset.filter(category__name=category)           
     

        if by_user:
            user_id = request.user.id          
            self.queryset = self.queryset.filter(member=user_id)
        

        if by_serverid:
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                
                if not self.queryset.exists():                   
                    raise ValidationError(detail=f"Server with id {by_serverid} not found")
            except ValueError:
                raise ValidationError(detail=f"Server with id {by_serverid} not found")
            
        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
