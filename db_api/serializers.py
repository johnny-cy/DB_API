from db_api.models import DomainListAll, DomainTestLog
from db_api.models import ForwardDomainListAll, ForwardDomainTestLog # Depricated
from db_api.models import DomainListDT3, DomainTestLogDT3
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

# ForwardDomainTestLog (Depricated)
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
    
# ForwardDomainListAll (Depricated)
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

# DomainListDT3
class DomainListDT3ListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [DomainListDT3(**item) for item in validated_data]
        return DomainListDT3.objects.using('default').bulk_create(data)

class DomainListDT3Serializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = DomainListDT3ListSerializer
        model = DomainListDT3
        fields = (
            'id',
            'AgentID',
            'Domain',
            'Latest',
            'HasRun',
            'CreatedTime',
        )
# DomainTestLogDT3
class DomainTestLogDT3ListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        data = [DomainTestLogDT3(**item) for item in validated_data]
        return DomainTestLogDT3.objects.using('default').bulk_create(data) 

class DomainTestLogDT3Serializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = DomainTestLogDT3ListSerializer
        model = DomainTestLogDT3
        fields = (
            'id',
            'DomainListDT3',
            'AgentID',
            'TestTime',
            'UrlIn',
            'UrlOut',
            'MyIP',
            'MyZone',
            'Status',
            'Browser',
            'IPScreenshot',
            'ProductScreenshot1',
            'ProductScreenshot2',
            'ProductScreenshot3',
            'ProductScreenshot4',
            'CreatedTime',
        )
        
