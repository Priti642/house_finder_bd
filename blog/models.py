from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Blog Model
class BlogModel(models.Model):
    blog_id = models.AutoField(primary_key=True)
    text = models.TextField(null=False)

    picture1 = models.ImageField(null=False, upload_to='blog_images/%Y/%m/%d/')
    picture2 = models.ImageField(null=True, upload_to='blog_images/%Y/%m/%d/')
    picture3 = models.ImageField(null=True, upload_to='blog_images/%Y/%m/%d/')

    time = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, db_column='email', on_delete=models.CASCADE)