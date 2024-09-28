from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()
    img_url=models.URLField(null=True)

# that only prints non-sensitive information
    def __str__(self):
        return self.title 
        
    
