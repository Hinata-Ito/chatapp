from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    pass

class Talk(models.Model):
    sender = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_talk')
    receiver = models.ForeignKey('User', on_delete=models.CASCADE, related_name='recieved_talk')
    #related_name は default で設定されている、参照するための関係の名前。ここが二つの外部キーで一致してしまうと、
    #クラッシュする
    message = models.CharField(max_length=300)
    # dt = models.DateTimeField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -> {}".format(self.sender, self.receiver)
