from django.db import models

# Create your models here.
class User(models.Model):
    class Meta(object):
        db_table= 'user'

    user_name=models.CharField('name', blank=False, null=False, max_length=45, db_index = True)

    password=models.CharField('password', blank=False,max_length=150, null=False, db_index = True)

    email=models.EmailField('email', blank=False, null=False, db_index= True)

    token=models.CharField('token', blank=True, null=True,max_length=500, db_index = True)

    token_expired=models.DateTimeField('token_expired', blank=True, null=True)

    created_at=models.DateTimeField('created_at', blank=True, auto_now_add=True)
    
    updated_at=models.DateTimeField('updated_at', blank=True, auto_now=True)

    def __str__(self):
        return self.user_name