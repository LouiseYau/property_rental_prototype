# Generated by Django 2.1.5 on 2019-02-08 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenancy_services_id', models.CharField(blank=True, max_length=8)),
                ('is_first_timer', models.BooleanField(null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('duration', models.CharField(blank=True, max_length=80)),
                ('price', models.DecimalField(decimal_places=2, default='0', max_digits=9)),
                ('payment_frequency', models.CharField(default='', max_length=20)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenancy_services_id', models.CharField(blank=True, max_length=8)),
                ('room_number', models.CharField(blank=True, max_length=4)),
                ('unit_number', models.CharField(blank=True, max_length=4)),
                ('house_number', models.CharField(blank=True, max_length=4)),
                ('building_name', models.CharField(blank=True, max_length=80)),
                ('street_name', models.CharField(default='', max_length=80)),
                ('suburb', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('region', models.CharField(blank=True, max_length=50)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('tenant_capacity', models.IntegerField()),
                ('car_spaces', models.IntegerField(blank=True, null=True)),
                ('dwelling_type', models.CharField(blank=True, choices=[('House/Townhouse', 'House/Townhouse'), ('Apartment', 'Apartment'), ('Room', 'Room'), ('Boarding house room', 'Boarding house room'), ('Bedsit/Flat', 'Bedsit/Flat')], max_length=20)),
                ('description', models.TextField(blank=True)),
                ('has_unit_title', models.BooleanField(default=False)),
                ('property_picture', models.ImageField(blank=True, upload_to='')),
                ('school_zone', models.CharField(blank=True, max_length=80)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('has_rental_wof', models.BooleanField(null=True)),
                ('landlord', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property_listing.Landlord')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='property_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property_listing.PropertyManager'),
        ),
        migrations.AddField(
            model_name='listing',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_listing.Property'),
        ),
    ]
