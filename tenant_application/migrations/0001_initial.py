# Generated by Django 2.1.5 on 2019-02-12 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManagement', '0001_initial'),
        ('property_listing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_request', models.DateField(blank=True)),
                ('duration_request', models.CharField(blank=True, max_length=80)),
                ('comments', models.TextField(blank=True)),
                ('has_accepted_tcd', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('referee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UserManagement.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(default=None, max_length=80)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_18_plus', models.BooleanField()),
                ('identification_type', models.CharField(blank=True, choices=[('Drivers License', 'Drivers License'), ('Passport', 'Passport'), ('Other', 'Other')], max_length=20)),
                ('identification_number', models.CharField(blank=True, max_length=40)),
                ('vehicle_registration', models.CharField(blank=True, max_length=10)),
                ('vehicle_make_and_model', models.CharField(blank=True, max_length=80)),
                ('is_first_timer', models.BooleanField(null=True)),
                ('has_verified_id', models.BooleanField(default=False)),
                ('is_verified_profile', models.BooleanField(default=False)),
                ('is_background_checked', models.BooleanField(default=False)),
                ('is_smoker', models.BooleanField(null=True)),
                ('has_children', models.BooleanField(null=True)),
                ('has_pets', models.BooleanField(null=True)),
                ('comments', models.TextField(blank=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.Contact')),
                ('emergency_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emergency_contact_set', to='UserManagement.Contact')),
                ('employer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employer_set', to='UserManagement.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='reference',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant_application.Tenant'),
        ),
        migrations.AddField(
            model_name='application',
            name='co_tenants',
            field=models.ManyToManyField(related_name='co_tenants_set', to='tenant_application.Tenant'),
        ),
        migrations.AddField(
            model_name='application',
            name='lead_tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lead_tenant_set', to='tenant_application.Tenant'),
        ),
        migrations.AddField(
            model_name='application',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='property_listing.Listing'),
        ),
    ]
