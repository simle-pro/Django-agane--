from django.db import models

class Group(models.Model):
    name = models.CharField( max_length=50)
    room = models.CharField( max_length=50)
    start_date = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    age = models.IntegerField()
    email = models.EmailField( max_length=254)
    phone = models.CharField( max_length=50)
    grade = models.FloatField()
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name 
