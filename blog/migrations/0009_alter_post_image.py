# Generated by Django 4.2.7 on 2023-11-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/blog/default.jpg', upload_to='media/'),
        ),
    ]
