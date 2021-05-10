from rest_framework import serializers


class hyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id','url','first_name','last_name','username','Email','mobile_no','Address','gender','age']

class userSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)
    Email = serializers.EmailField()
    mobile_no = serializers.IntegerField()
    Address = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.IntegerField()
    