# Generated by Django 4.1.5 on 2023-02-08 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_post_image_post_like_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]