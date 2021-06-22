# Generated by Django 3.2 on 2021-05-19 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('email', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(default='profile.png', null=True, upload_to='photo_pics/')),
            ],
        ),
    ]
