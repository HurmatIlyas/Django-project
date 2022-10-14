from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from MyApp.validators import phone_number_validator

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    contact = models.IntegerField()
    complain = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.CharField(max_length=120)
    care = models.CharField(max_length=400, null=True)
    category = models.CharField(max_length=120)
    currency = models.CharField(max_length=120)
    description = models.CharField(max_length=400, null=True)
    image = models.URLField()
    image_urls = models.URLField()
    lang = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
    retailer_sku = models.CharField(max_length=100, primary_key=True)
    skus = models.CharField(max_length=400)
    url = models.CharField(max_length=120)
    trail = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    validated_phone_number = phone_number_validator()
    contact_information = models.CharField(validators=[validated_phone_number], max_length=11, null=True, blank=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact_information', 'password1', 'password2']

    objects = CustomUserManager()


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_information = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.product.name
