from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=500)
    old_price = models.IntegerField()
    now_price = models.IntegerField()
    product_image = models.ImageField(upload_to="media/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
