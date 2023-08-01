from rest_framework import serializers 
from .models import Server, Channel

# 1) /////////////////////////
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
#         x = hasattr(obj, "num_members")        
#         print(x)
#         print(obj)
#         if x:           
#             return obj.num_members       
#         return None
    

# 2) /////////////////////////
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
        x = hasattr(obj, 'num_members')
        if x:                      
            return obj.num_members            
        return None

    def to_representation(self, instance):
        # print(instance)            
        data = super().to_representation(instance)
        print(data)
        
        num_members = self.context.get('num_members')        
        if not num_members:
            data.pop('num_members', None)
            # print(data['num_members'])
        return data
    

    
       
        
