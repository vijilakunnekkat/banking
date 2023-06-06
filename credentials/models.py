from django.db import models

# Create your models here.

# class District(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
# class Branch(models.Model):
#     country = models.ForeignKey(District, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name

class Final(models.Model):
    name=models.CharField(max_length=250)
    date=models.DateField(auto_now_add=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    district=models.CharField(max_length=250)
    account=models.CharField(max_length=250)
    materials=models.CharField(max_length=250,null=True,blank=True)
    # district= models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    # branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)


def __str__(self):
    return self.name

