from django.db import models

# Create your models here.
class GroupDiscussionTeacher(models.Model):
    index = models.IntegerField(null=True)
    name=models.CharField(max_length=4)
    def __str__(self):
        return self.name