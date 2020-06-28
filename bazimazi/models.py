from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"

class State(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='ads', blank=True)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.email})"

class Ad(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads', blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=60)
    price = models.FloatField()
    title = models.CharField(max_length=60)
    description = models.TextField()
    saved_ads = models.ManyToManyField(User, blank=True, related_name="saved_ads")

    def __str__(self):
        return f"{self.title} {self.category.name} ({self.state.name})"
