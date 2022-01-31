from django.db import models


# Create your models here.
class PublishingHouse(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name: "Publishing House"
        verbose_name_plural = "Publishing Houses"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=50)  # odpowiednik <input type="text">
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    publishingHouse = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)  # odpowiednik <textarea>  blank=True - nieobowiązkowe
    price = models.DecimalField(max_digits=6, decimal_places=2)  # liczby max 6 cyfrowe, z dwoma miejscami po przecinku

    class Meta:
        verbose_name = "Book"  # liczba pojedyncza
        verbose_name_plural = "Books"  # liczba mnoga

    def __str__(self):
        return self.title
