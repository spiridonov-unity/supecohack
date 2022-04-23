from django.db import models


class Section(models.Model):
    title = models.CharField(
        max_length=70,
        help_text='Тут надо ввести название раздела',
        unique=True,
        verbose_name='Название раздела'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Product(models.Model):
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True, verbose_name='Раздел')
    title = models.CharField(max_length=70, verbose_name='Название')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    country = models.CharField(max_length=70, verbose_name='Регион')
    description = models.TextField(verbose_name='Описание')
    address = models.TextField(blank=True, verbose_name='Адрес')

    class Meta:
        ordering = ['title']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.section.title)


class Order(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    phone = models.CharField(max_length=70, verbose_name='Телефон')
    email = models.EmailField()
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма вложения')

    STATUSES = [
        ('NEW', 'Новый платёж'),
        ('APR', 'Подтверждён'),
        ('PAY', 'Оплачен'),
        ('CNL', 'Отменён')
    ]

    status = models.CharField(choices=STATUSES, max_length=3, default='NEW', verbose_name='Статус')

    class Meta:
        ordering = ['-date_order']
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return 'ID: ' + str(self.id)
