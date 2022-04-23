# Generated by Django 4.0.4 on 2022-04-22 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('phone', models.CharField(max_length=70, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('notice', models.TextField(blank=True, verbose_name='Примечание к заказу')),
                ('date_order', models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')),
                ('status', models.CharField(choices=[('NEW', 'Новый платёж'), ('APR', 'Подтверждён'), ('PAY', 'Оплачен'), ('CNL', 'Отменён')], default='NEW', max_length=3, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Платёж',
                'verbose_name_plural': 'Платежи',
                'ordering': ['-date_order'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Тут надо ввести название раздела', max_length=70, unique=True, verbose_name='Название раздела')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Необходимая сумма')),
                ('country', models.CharField(max_length=70, verbose_name='Регион')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.section', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['title'],
            },
        ),
    ]