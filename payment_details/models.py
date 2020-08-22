from django.db import models
from django.urls import reverse
from transactions.models import User
from django_resized import ResizedImageField
# Create your models here.

class BankTransfer(models.Model):
    name = models.CharField( max_length=50)
    bank_name = models.CharField( max_length=50)
    account_number = models.CharField( max_length=50)

    def __str__(self):
        return str(self.name)

class BTCTransfer(models.Model):
    name = models.CharField( max_length=50)
    btc_address = models.CharField( max_length=50)

    def __str__(self):
        return str(self.name)

class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=70)
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = ResizedImageField(
        size=[128, 128],
        crop=['top','left'], 
        quality=80,
        upload_to="media-root/",
        null=True,
        blank=False,
        )

    def __str__(self):
        return 'Message sent to ' + str(self.user.get_full_name()) + ' on ' +str(self.timestamp.date())

    def get_snippet(self):
        return str(self.message)[0:43]+'...'

    def get_absolute_url(self):
        return reverse('read_mail', args=[str(self.id)])