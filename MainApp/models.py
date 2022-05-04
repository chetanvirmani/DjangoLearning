from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model): #This is inheriting all the properties of the Models class (this is a subclass)
    text = models.CharField(max_length=200) #Name of the topic
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries' #This will make Entrys > into Entries
    
    
    def __str__(self):
        return f"{self.text[:50]}..."

