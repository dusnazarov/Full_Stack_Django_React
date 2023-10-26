from rest_framework import serializers 
from .models import Server, Channel

# # 1) /////////////////////////
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):
    num_members = serializers.SerializerMethodField()
    channel_server = ChannelSerializer(many=True)    

    class Meta:
        model = Server
        exclude = ("member",)
   

    def get_num_members(self, obj):       
        x = hasattr(obj, "num-memebers")
        print('Hello')    
        print(x)
        print(obj)
        if x:           
            return obj.num_members       
        return None
    

# # 2) /////////////////////////
# class ChannelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Channel
#         fields = '__all__'

# class ServerSerializer(serializers.ModelSerializer):
#     num_members = serializers.SerializerMethodField()
#     channel_server = ChannelSerializer(many=True)
    

#     class Meta:
#         model = Server
#         exclude = ("member",)

#     def get_num_members(self, obj):
#         x = hasattr(obj, 'num_members')
#         # print('hello')
#         # print(x)
        
#         if x:                      
#             return obj.num_members            
#         return None

#     def to_representation(self, instance):
#         # print(instance)
#         # print(instance.owner)    
#         # print(instance.category)    
            
#         data = super().to_representation(instance)
         
#         num_members = self.context.get('num_members')
#         # print(self.context)
#         # print(data)  
#         # print(num_members)
#         # print(data['channel_server'])
#         # print(data['name'])
        
#         if not num_members:
#             data.pop('num_members', None)
#             print(data)
#         return data
    
#     def hasattr(ServerSerilizer):
#         return None

    
       
        
