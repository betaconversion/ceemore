from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username is required')
        
        user = self.model(
            email= self.normalize_email(email),
            username= username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,password):
        user = self.create_user(
             email= self.normalize_email(email),
            username= username,
            password= password,
        
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff= True
        user.save(using=self._db)
        return user








class Account(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email', max_length=60, unique=True )
    username    = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    #profile_image = models.ImageField(blank=True, null=True, default='default.jgp', upload_to='profile')
    hide_email    = models.BooleanField(default=True)

    
    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def  has_module_perms(self, app_label):
        return True



class Reservatioin(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    time_to_meet = models.DateTimeField()
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)