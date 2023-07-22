import os
from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    path_to_img = models.CharField(max_length=511)
    cost = models.FloatField()
    amount = models.CharField(max_length=127)  # e.g. kilo, 100 gr, 500 gr, liter, 200 ml, 500ml, 3 liter, piece
    type = models.CharField(max_length=31)  # e.g. drinks, food, other
    
    def __str__(self):
        """
        displays the product name on the admin site
        """
        return self.name

    def delete(self):
        """
        deletes image file(if it exists) on deleting product
        """
        full_path_to_img = os.path.join(settings.STATICFILES_DIRS[0], self.path_to_img)

        if os.path.exists(full_path_to_img):
            os.remove(full_path_to_img)

        super(Product, self).delete()
