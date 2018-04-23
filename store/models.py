from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=250)
  price = models.DecimalField(decimal_places=2, max_digits=10)
  code = models.CharField(max_length=500)
  description = models.TextField(default='Description')
  image = models.ImageField(upload_to='images', default='images/placeholder.jpg')

  def __str__(self):
    return '{} - item: {} - price: {} - code: {}'.format(self.id, self.name, self.price, self.code)

