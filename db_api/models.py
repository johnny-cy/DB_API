from django.db import models

# Create your models here.
class DomainListAll(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    AgentID = models.CharField(max_length=30, unique=True)
    CodeToMatch = models.CharField(max_length=50, unique=True)
    DomainListAPP = models.CharField(max_length=300, blank=True, null=True)
    DomainListInner = models.CharField(max_length=300, blank=True, null=True)
    DomainListOuter = models.CharField(max_length=300, blank=True, null=True)
    Active = models.IntegerField()
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    DomainType = models.CharField(max_length=50)
    class Meta:
        db_table = "DomainListAll"


class DomainTestLog(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    AgentID = models.CharField(max_length=50, blank=True, null=True)
    TestTime = models.DateTimeField(blank=True, null=True)
    UrlIn = models.CharField(max_length=200, blank=True, null=True)
    UrlOut = models.CharField(max_length=200, blank=True, null=True)
    MyIP = models.CharField(max_length=200, blank=True, null=True)
    MyZone = models.CharField(max_length=200, blank=True, null=True)
    CDN = models.CharField(max_length=200, blank=True, null=True)
    CDNIP = models.CharField(max_length=200, blank=True, null=True)
    PageLoadTime = models.FloatField(null=True, blank=True)
    Browser = models.CharField(max_length=50, blank=True, null=True)
    Through = models.CharField(max_length=5, blank=True, null=True)
    Status = models.CharField(max_length=50, blank=True, null=True)
    IPScreenshot = models.CharField(max_length=300, blank=True, null=True)
    ProductScreenshot1 = models.CharField(max_length=300, blank=True, null=True)
    ProductScreenshot2 = models.CharField(max_length=300, blank=True, null=True)
    ProductScreenshot3 = models.CharField(max_length=300, blank=True, null=True)
    ProductScreenshot4 = models.CharField(max_length=300, blank=True, null=True)
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    DomainType = models.CharField(max_length=50)
    class Meta:
        db_table = "DomainTestLog"


class ForwardDomainListAll(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    AgentID = models.CharField(max_length=30, unique=True)
    UrlIn = models.CharField(max_length=200)
    UrlOut = models.CharField(max_length=200)
    MyZone = models.CharField(max_length=50)
    DomainType = models.CharField(max_length=50)
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = "ForwardDomainList"


class ForwardDomainTestLog(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    AgentID = models.CharField(max_length=30)
    TestTime = models.DateTimeField(blank=True, null=True)
    UrlIn = models.CharField(max_length=200)
    UrlOut = models.CharField(max_length=200)
    MyIP = models.CharField(max_length=200)
    MyZone = models.CharField(max_length=200)
    Status = models.CharField(max_length=50)
    Browser = models.CharField(max_length=50)
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    DomainType = models.CharField(max_length=50)
    class Meta:
        db_table = "ForwardDomainTestLog"



class DomainListDT3(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    AgentID = models.CharField(max_length=50)
    Domain = models.CharField(max_length=200)
    HasRun = models.IntegerField()
    Latest = models.IntegerField()
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = "DomainListDT3"


class DomainTestLogDT3(models.Model):
    """
    a migrate --fake table.
    """
    id = models.AutoField(primary_key=True)
    DomainListDT3 = models.ForeignKey(DomainListDT3, on_delete=models.CASCADE)
    AgentID = models.CharField(max_length=30)
    TestTime = models.DateTimeField(blank=True, null=True)
    UrlIn = models.CharField(max_length=200)
    UrlOut = models.CharField(max_length=200)
    MyIP = models.CharField(max_length=200)
    MyZone = models.CharField(max_length=200)
    Status = models.CharField(max_length=50)
    Browser = models.CharField(max_length=50)
    CreatedTime = models.DateTimeField(auto_now_add=True, null=True)
    DomainType = models.CharField(max_length=50)
    class Meta:
        db_table = "DomainTestLogDT3"
