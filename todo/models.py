from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.content

    class Meta:
        ordering = ['-created']
