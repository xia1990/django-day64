from django.db import models

class Publisher(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=64,null=True,unique=True)

class Book(models.Model):
    bid=models.AutoField(primary_key=True)
    bname=models.CharField(max_length=64,null=True,unique=True)
    #定义外键的时候需要加上 on_delete=;
    publisher = models.ForeignKey(to="Publisher",on_delete=models.CASCADE)

    def __str__(self):
        return "<Book object>:{}".format(self.bname)

class Author(models.Model):
    aid=models.AutoField(primary_key=True)
    aname=models.CharField(max_length=16,null=False,unique=True)
    book=models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author object>:{}".format(self.aname)

