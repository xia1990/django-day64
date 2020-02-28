from django.db import models

class Publisher(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=64,null=True,unique=True)

class Book(models.Model):
    bid=models.AutoField(primary_key=True)
    bname=models.CharField(max_length=64,null=True,unique=True)
    #定义外键的时候需要加上 on_delete=;
    publisher = models.ForeignKey(to="Publisher",on_delete=models.CASCADE)