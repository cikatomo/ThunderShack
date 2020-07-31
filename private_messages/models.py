from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ads.models import Ad

class Conversation(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='starter', on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User) 

    def get_absolute_url(self):
        return reverse('messages-conversation', kwargs={'pk':self.pk})

    @classmethod
    def get_if_exists(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None
        except cls.MultipleObjectsReturned:
            return "multiple"


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.SET_NULL, null=True)
    #receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.SET_NULL, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    conversation =  models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True, blank=True)

