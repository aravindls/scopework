from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_categories')
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Category"