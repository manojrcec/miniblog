# Generated by Django 4.1.4 on 2023-03-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='Shyam', upload_to='blogimages'),
        ),
    ]
