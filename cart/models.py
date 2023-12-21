from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import  BaseUserManager
# Create your models here.

class  UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,  email, password=None, **extra_fileds):

        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra_fileds):
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)
        extra_fileds.setdefault('is_active', True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(("Superuser is must have a staff true"))
        return self.create_user(email, password, **extra_fileds) 

class Account(models.Model):
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    

    objects = UserManager()
    
    USERNAME_FIELD = 'company_name'

    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.company_name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    create_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    company_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.product_name
    