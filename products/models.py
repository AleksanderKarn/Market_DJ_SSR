from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='название категории')
    description = models.TextField("Описание категории")

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Продавец', **NULLABLE)
    name_product = models.CharField("Название продукта", max_length=250)
    description = models.TextField("Описание продукта")
    image = models.ImageField("Изображение", upload_to='products/', **NULLABLE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', verbose_name='Категория')
    unit_price = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='цена в рублях')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Заполняется когда пользователь создает экземпляр товара
    updated_at = models.DateTimeField(auto_now=True)  #заполняется когда пользователь сам чтото меняет

    def __str__(self):
        return f'{self.name_product}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def version(self):
        return self.products.get(status_version=True)




    #def delete(self, *args, **kwargs):
    #    '''запрещает удаление из БД продукта'''
    #    self.is_active = False
    #    self.save()

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')

    number_version = models.IntegerField(default=1, verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='название версии')
    status_version = models.BooleanField(default=False, verbose_name='признак версии')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'версия {self.number_version} - {self.name}'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


