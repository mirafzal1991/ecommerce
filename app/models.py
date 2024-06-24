from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def get_attributes(self) ->list[dict]:
        product_attributes = ProductAttribute.objects.filter(product=self)
        attributes = []
        for pa in product_attributes:
            attributes.append({
                'attribute_key':pa.attribute.key_name,
                'attribute_value':pa.attribute_value.value_name})
        return attributes









    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)

        return self.price
    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='products', null=True)
    product = models.ForeignKey('app.Product', on_delete=models.SET_NULL, related_name='images', null=True)

class Attribute(models.Model):
    key_name = models.CharField(max_length=125,unique=True)

    def __str__(self):
        return self.key_name

class AttributeValues(models.Model):
    value_name = models.CharField(max_length=125,unique=True)

    def __str__(self):
        return self.value_name

class ProductAttribute(models.Model):
    product = models.ForeignKey('app.Product',on_delete=models.CASCADE)
    attribute = models.ForeignKey('app.Attribute',on_delete=models.CASCADE)
    attribute_value = models.ForeignKey('app.AttributeValues',on_delete=models.CASCADE)
