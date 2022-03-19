from django.db import models

class studentDB(models.Model):

    rollnumber = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=100)
    DOB = models.DateField(null=True)
    marks = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.rollnumber+ '---'+self.name