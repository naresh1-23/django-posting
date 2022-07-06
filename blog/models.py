import email
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    caption = models.TextField()
    post_image = models.ImageField(upload_to = 'images/')
    time_now = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username} Post'

    def get_absolute_url(self):
        return reverse('blog-home')


    def save(self):
        super().save()

        img  = Image.open(self.post_image.path)

        if img.height >550 or img.width>500:
            outpur_size = (550, 500)
            img.thumbnail(outpur_size)
            img.save(self.post_image.path)