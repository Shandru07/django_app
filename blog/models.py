from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


    

