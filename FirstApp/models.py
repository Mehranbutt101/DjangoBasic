from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.top_name
    
class WebPage(models.Model):
    topic = models.ForeignKey(Topic,'Deleted')
    name = models.CharField(max_length=26,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,'deleted')
    date = models.DateField()

    def __str__(self):
        return str(self.date)