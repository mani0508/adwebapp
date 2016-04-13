# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0004_auto_20160208_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('buyer_name', models.CharField(max_length=80, blank=True)),
                ('company_name', models.CharField(max_length=200)),
                ('contact_person_name', models.CharField(max_length=80, blank=True)),
                ('contact_person_number', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('alternate_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('email', models.EmailField(max_length=60)),
                ('address', models.CharField(max_length=300)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('id_type', models.CharField(max_length=200, choices=[(b'Aadhar card', b'Aadhar card'), (b'Driving License', b'Driving License'), (b'Passport', b'Passport'), (b'Election id', b'Election id'), (b'Ration Card', b'Ration Card')])),
                ('id_number', models.CharField(max_length=25, blank=True)),
                ('service_tax_number', models.CharField(max_length=25, blank=True)),
                ('vat_number', models.CharField(max_length=25, blank=True)),
                ('pan_number', models.CharField(max_length=15, blank=True)),
                ('account_number', models.CharField(max_length=25, blank=True)),
                ('ifsc', models.CharField(max_length=15, blank=True)),
                ('city', models.ForeignKey(to='codes.City')),
            ],
        ),
        migrations.CreateModel(
            name='Hoarding_Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hoarding_id', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('status', models.CharField(max_length=20, choices=[(b'confirm', b'confirm'), (b'closed', b'closed'), (b'cancel', b'cancel')])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=15)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=15)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('owner_name', models.CharField(max_length=80, blank=True)),
                ('agency_name', models.CharField(max_length=200)),
                ('contact_person_name', models.CharField(max_length=80, blank=True)),
                ('contact_person_number', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('alternate_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('email', models.EmailField(max_length=60)),
                ('address', models.CharField(max_length=300)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('id_type', models.CharField(max_length=200, choices=[(b'Aadhar card', b'Aadhar card'), (b'Driving License', b'Driving License'), (b'Passport', b'Passport'), (b'Election id', b'Election id'), (b'Ration Card', b'Ration Card')])),
                ('id_number', models.CharField(max_length=25, blank=True)),
                ('service_tax_number', models.CharField(max_length=25, blank=True)),
                ('vat_number', models.CharField(max_length=25, blank=True)),
                ('pan_number', models.CharField(max_length=15, blank=True)),
                ('account_number', models.CharField(max_length=25, blank=True)),
                ('ifsc', models.CharField(max_length=15, blank=True)),
                ('city', models.ForeignKey(to='codes.City')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('tran_id', models.AutoField(serialize=False, primary_key=True)),
                ('total_price', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('customer_contact_person_name', models.CharField(max_length=50)),
                ('customer_contact_person_number', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to='codes.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('user_type', models.CharField(max_length=10, choices=[(b'admin', b'Admin'), (b'owner', b'Owner'), (b'broker', b'Broker'), (b'customer', b'Customer')])),
            ],
        ),
        migrations.AddField(
            model_name='hoarding',
            name='area',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='available',
            field=models.CharField(default=b'yes', max_length=10, choices=[(b'yes', b'YES'), (b'no', b'NO')]),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='available_from',
            field=models.DateField(default=datetime.datetime(2016, 2, 8, 14, 49, 57, 150008, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='available_to',
            field=models.DateField(default=datetime.datetime(2016, 2, 8, 14, 50, 5, 405958, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='description',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='elevation',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='facing_from',
            field=models.CharField(default=b'Not Available', max_length=200),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='facing_to',
            field=models.CharField(default=b'Not Available', max_length=200),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='image1',
            field=models.ImageField(upload_to=b'/home/mani/vishal/media/images', blank=True),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='image2',
            field=models.ImageField(upload_to=b'/home/mani/vishal/media/images', blank=True),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='image3',
            field=models.ImageField(upload_to=b'/home/mani/vishal/media/images', blank=True),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='image4',
            field=models.ImageField(upload_to=b'/home/mani/vishal/media/images', blank=True),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='landmark',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='length',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='pin',
            field=models.CharField(blank=True, max_length=6, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='price_per_month',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='speciality',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='trafic_signal',
            field=models.CharField(default=b'no', max_length=10, choices=[(b'yes', b'YES'), (b'no', b'NO')]),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='width',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='outdoortype',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='hoardings',
            field=models.ManyToManyField(to='codes.Hoarding'),
        ),
        migrations.AddField(
            model_name='location',
            name='hoarding_id',
            field=models.ForeignKey(to='codes.Hoarding'),
        ),
        migrations.AddField(
            model_name='hoarding_customer',
            name='tran_id',
            field=models.ForeignKey(to='codes.Transaction'),
        ),
        migrations.AddField(
            model_name='hoarding',
            name='city',
            field=models.ForeignKey(default='', to='codes.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='owner',
            field=models.ForeignKey(default='', to='codes.Owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hoarding',
            name='state',
            field=models.ForeignKey(default='', to='codes.State'),
            preserve_default=False,
        ),
    ]
