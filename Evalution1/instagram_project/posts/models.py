from django.db import models

class Post(models.Model):
    username=models.CharField(max_length=40)
    caption=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
