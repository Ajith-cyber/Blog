from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    img_url=models.URLField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)

# that only prints non-sensitive information
    def __str__(self):
        return self.title 
        
    
