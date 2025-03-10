# Generated by Django 5.0.10 on 2024-12-31 17:18

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessibilityItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Accessibility Item',
                'verbose_name_plural': 'Accessibility Items',
            },
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='CheckoutInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Checkout Instruction',
                'verbose_name_plural': 'Checkout Instructions',
            },
        ),
        migrations.CreateModel(
            name='PropertyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Property Information',
                'verbose_name_plural': 'Property Information',
            },
        ),
        migrations.CreateModel(
            name='SafetyConsideration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Safety Consideration',
                'verbose_name_plural': 'Safety Considerations',
            },
        ),
        migrations.CreateModel(
            name='SafetyDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Safety Device',
                'verbose_name_plural': 'Safety Devices',
            },
        ),
        migrations.CreateModel(
            name='StandoutAmenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Standout Amenity',
                'verbose_name_plural': 'Standout Amenities',
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instant_book', models.BooleanField(default=True)),
                ('wifi_network_name', models.CharField(blank=True, max_length=100, null=True)),
                ('wifi_password', models.CharField(blank=True, max_length=100, null=True)),
                ('house_manual', models.TextField(blank=True, null=True)),
                ('bedrooms', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], default=1)),
                ('beds', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], default=1)),
                ('bathrooms', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], default=1)),
                ('guests', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], default=1)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('events_allowed', models.BooleanField(default=False)),
                ('smoking_allowed', models.BooleanField(default=False)),
                ('commercial_photography_allowed', models.BooleanField(default=False)),
                ('check_in_start_time', models.TimeField(blank=True, null=True)),
                ('check_in_end_time', models.TimeField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('additional_rules', models.TextField(blank=True, null=True)),
                ('nightly_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_listing_promotion', models.BooleanField(default=False)),
                ('weekly_discount_percentage', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('monthly_discount_percentage', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('cleaning_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('street_address', models.CharField(max_length=255)),
                ('apt_floor_bldg', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('province_state_territory', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('google_calendar_locator', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('directions', models.TextField(blank=True, null=True)),
                ('check_in_method', models.CharField(blank=True, choices=[('Smart lock', 'Smart lock'), ('Keypad', 'Keypad'), ('Lockbox', 'Lockbox'), ('Building staff', 'Building staff'), ('In-person greeting', 'In-person greeting'), ('Other', 'Other')], default='in_person_greeting', max_length=50, null=True)),
                ('other_check_in_method', models.TextField(blank=True, null=True)),
                ('additional_checkout_instructions', models.TextField(blank=True, null=True)),
                ('cancellation_policy', models.CharField(blank=True, choices=[('Flexible', 'Flexible'), ('Moderate', 'Moderate'), ('Firm', 'Firm'), ('Strict', 'Strict'), ('Non-refundable', 'Non-refundable')], default='flexible', max_length=50, null=True)),
                ('accessibility_items', models.ManyToManyField(to='destinations.accessibilityitem')),
                ('amenities', models.ManyToManyField(to='destinations.amenity')),
                ('checkout_instructions', models.ManyToManyField(to='destinations.checkoutinstruction')),
                ('host', models.ForeignKey(limit_choices_to={'is_host': True}, on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to=settings.AUTH_USER_MODEL)),
                ('property_information', models.ManyToManyField(to='destinations.propertyinformation')),
                ('safety_considerations', models.ManyToManyField(to='destinations.safetyconsideration')),
                ('safety_devices', models.ManyToManyField(to='destinations.safetydevice')),
                ('standout_amenities', models.ManyToManyField(to='destinations.standoutamenity')),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.structure')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
