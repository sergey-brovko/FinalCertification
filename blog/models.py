from django.db import models

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return self.title