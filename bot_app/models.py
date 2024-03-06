from django.db import models

# Create your models here.

class PositionModel(models.Model):
    position = models.CharField(max_length=150)

    def __str__(self):
        return self.position
    
class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    image = models.ImageField(default='person.jpg')
    position = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name +'' + self.last_name
    