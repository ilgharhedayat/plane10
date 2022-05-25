# Generated by Django 4.0.4 on 2022-05-25 20:23

import accounts.uitils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userdocument'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otpcode',
            options={'verbose_name': 'کد  ارسالی', 'verbose_name_plural': 'کد های ارسالی'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.AlterModelOptions(
            name='userdocument',
            options={'verbose_name': 'مدرک', 'verbose_name_plural': 'مدارک'},
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.PositiveSmallIntegerField(verbose_name='کد ارسالی'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=125, verbose_name='نام '),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='ادمین'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=125, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^09[0|1|2|9][0-9]{8}$')], verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=125, unique=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='identity_card',
            field=models.ImageField(upload_to=accounts.uitils.get_file_path, verbose_name='تصویر شناسنامه'),
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='national_card',
            field=models.ImageField(upload_to=accounts.uitils.get_file_path, verbose_name='تصویر کد ملی'),
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='other',
            field=models.ImageField(blank=True, upload_to=accounts.uitils.get_file_path, verbose_name='سایر مدارک'),
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='passport',
            field=models.ImageField(blank=True, upload_to=accounts.uitils.get_file_path, verbose_name='تصویر پاسپورت'),
        ),
        migrations.AlterField(
            model_name='userdocument',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='document', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
