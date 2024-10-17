from django.db import models



class MenuItem(models.Model):
    menu_id = models.AutoField(primary_key=True, null=False, blank=True)
    menu_name = models.CharField(max_length=100)
    menu_price = models.DecimalField(max_digits=6, decimal_places=2)
    menu_image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.menu_name