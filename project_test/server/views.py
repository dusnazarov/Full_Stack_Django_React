
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer
from rest_framework.response import Response
from django.db.models import Count


# 1) ////////////////////////////////

# class ServerListViewSet(viewsets.ViewSet):
#     queryset = Server.objects.all()

#     def list(self, request):   
#         with_num_members = request.query_params.get("with_num_members")


#         if with_num_members:
#             self.queryset = self.queryset.annotate(num_members=Count('member'))        

            
#         serializer = ServerSerializer(self.queryset, many=True)
#         return Response(serializer.data)


# 2) ////////////////////////////////

class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        with_num_members = request.query_params.get("with_num_members")        
        
       

        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count('member'))   # http://127.0.0.1:8000/api/server/select/?with_num_members=2
            
        serializer = ServerSerializer(self.queryset, many=True, context={"num_members":with_num_members})
        return Response(serializer.data)

       