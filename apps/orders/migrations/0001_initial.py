# Generated by Django 4.2.10 on 2024-02-27 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total Price')),
                ('full_name', models.CharField(db_index=True, max_length=25, verbose_name='Full Name')),
                ('address_line1', models.CharField(db_index=True, max_length=250, verbose_name='Address Line1')),
                ('address_line2', models.CharField(db_index=True, max_length=250, verbose_name='Address Line2')),
                ('city', models.CharField(db_index=True, max_length=25, verbose_name='City')),
                ('state', models.CharField(db_index=True, max_length=25, verbose_name='State')),
                ('postal_code', models.IntegerField(db_index=True, verbose_name='Postal Code')),
                ('country', models.CharField(db_index=True, default='United State', max_length=25, verbose_name='Country')),
                ('telephone', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Telephone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(db_index=True, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]
