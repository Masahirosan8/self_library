from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

## Register your models here
class Books(models.Model):
	id				= models.AutoField(primary_key=True)
	user_id 		= models.ForeignKey('User', on_delete=models.CASCADE, null=True)
	category_id 	= models.ForeignKey('Categories', on_delete=models.CASCADE)
	name 			= models.CharField(max_length=150)
	author 			= models.CharField(max_length=100)
	impression 		= models.TextField(blank=True)
	review 			= models.IntegerField()
	#image 			= models.ImageField(null=True)
	create_user 	= models.CharField(max_length=100)
	create_date		= models.DateField(auto_now_add=True)
	update_user		= models.CharField(max_length=100,null=True)
	update_date		= models.DateField(auto_now=True, null=True)

class Categories(models.Model):
	id				= models.AutoField(primary_key=True)
	name			= models.CharField(max_length=50)
	create_user     = models.CharField(max_length=100)
	create_date     = models.DateField(auto_now_add=True)
	update_user     = models.CharField(max_length=100,null=True)
	update_date     = models.DateField(auto_now=True, null=True)

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            name = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
	name			= models.CharField(max_length=100, blank=True)
	create_user     = models.CharField(max_length=100)
	create_date     = models.DateField(auto_now_add=True)
	update_user     = models.CharField(max_length=100,null=True)
	update_date     = models.DateField(auto_now=True, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'name'
	REQUIRED_FIELDS = []

