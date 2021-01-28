from db_api.models import DomainListAll, DomainTestLog, ForwardDomainListAll, ForwardDomainTestLog
from rest_framework import serializers
# DomainTestLog
class DomainTestLogListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [DomainTestLog(**item) for item in validated_data]
        return DomainTestLog.objects.using('default').bulk_create(data) 


class DomainTestLogSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = DomainTestLogListSerializer
        model = DomainTestLog
        fields = (
            'id',
            'AgentID',
            'TestTime',
            'UrlIn',
            'UrlOut',
            'MyIP',
            'MyZone',
            'CDN',
            'CDNIP',
            'PageLoadTime',
            'Status',
            'Through',
            'Browser',
            'IPScreenshot',
            'ProductScreenshot1',
            'ProductScreenshot2',
            'ProductScreenshot3',
            'ProductScreenshot4',
            'CreatedTime',
            'DomainType',
        )

        
# DomainListAll
class DomainListAllListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [DomainListAll(**item) for item in validated_data]
        return DomainListAll.objects.using('default').bulk_create(data)

class DomainListAllSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = DomainListAllListSerializer
        model = DomainListAll
        fields = (
            'id',
            'AgentID',
            'CodeToMatch',
            'DomainListAPP',
            'DomainListInner',
            'DomainListOuter',
            'Active',
            'CreatedTime',
            'DomainType',
        )



# ForwardDomainTestLog
class ForwardDomainTestLogListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [ForwardDomainTestLog(**item) for item in validated_data]
        return ForwardDomainTestLog.objects.using('default').bulk_create(data) 


class ForwardDomainTestLogSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = ForwardDomainTestLogListSerializer
        model = ForwardDomainTestLog
        fields = (
            'id',
            'AgentID',
            'TestTime',
            'UrlIn',
            'UrlOut',
            'MyIP',
            'MyZone',
            'Status',
            'Browser',
            'CreatedTime',
            'DomainType',
        )

        
# ForwardDomainListAll
class ForwardDomainListAllListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [ForwardDomainListAll(**item) for item in validated_data]
        return ForwardDomainListAll.objects.using('default').bulk_create(data)

class ForwardDomainListAllSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = ForwardDomainListAllListSerializer
        model = ForwardDomainListAll
        fields = (
            'id',
            'AgentID',
            'UrlIn',
            'UrlOut',
            'MyZone',
            'DomainType',
            'CreatedTime',
        )
