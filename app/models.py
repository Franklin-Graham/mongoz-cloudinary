# from django.db import models
#
# # Create your models here.
# class Profile(models.Model):
#     Name = models.CharField(max_length=100)
#     profile = models.ImageField()
#     def __str__(self):
#         return self.Name
#
# class Main(models.Model):
#     image = models.ImageField(upload_to='picture')
#
# class Portrait(models.Model):
#     image = models.ImageField(upload_to='portrait')
#
# class Mandal(models.Model):
#     image = models.ImageField(upload_to='mandala')
#
# class Canvas(models.Model):
#     image = models.ImageField(upload_to='canvas')
#
# class Bottle(models.Model):
#     image = models.ImageField(upload_to='bottle')


from mongoengine import fields,Document

class head(Document):
    name = fields.StringField()
    def __str__(self):
        return self.name