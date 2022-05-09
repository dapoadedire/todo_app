from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.content

    class Meta:
        ordering = ['-created']
