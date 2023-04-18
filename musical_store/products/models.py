from django.db import models


class Product(models.Model):
    name = models.CharField(
        verbose_name='Наименование товара',
        max_length=30,
        blank=False,
    )
    image = models.ImageField(
        verbose_name='Фото товара',
        upload_to='',
        blank=False,
    )
    description = models.CharField(
        verbose_name='Описание товара',
        max_length=256,
        blank=True,
    )
    color = models.CharField(
        verbose_name='Цвет товара',
        max_length=20,
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена товара',
        blank=False,
    )
    link_to_shop = models.CharField(
        max_length=256,
        verbose_name='Ссылка на магазин'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.name}, {self.description}, {self.price}'
