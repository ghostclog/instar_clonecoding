from django.db import models
from djagno_instar_clone.users import models as user_model

# Create your models here.
class TimeStateModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(TimeStateModel):
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_author') 
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=False)
    likes = models.ManyToManyField(
        user_model.User,
        blank=True,
        related_name='post_image_likes'
    )

    def __str__(self):
        return f"{self.author}:{self.caption}"


class Comment(TimeStateModel):
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_author')  
    post = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post') 
    contents = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}:{self.contents}"