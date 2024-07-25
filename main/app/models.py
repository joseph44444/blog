from django.db import models

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=55)
    content = models.TextField()
    image = models.ImageField(upload_to="Blog_media")
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    comment = models.ImageField(upload_to="Blog_media")
    created_at = models.DateTimeField(auto_now=True)
    
    class meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.commment
    
class Like(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ["-created_at"]

class NewsLetter(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.email

    


