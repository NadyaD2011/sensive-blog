# Generated by Django 2.2.5 on 2019-09-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(default="1000-01-01"),
            preserve_default=False,
        ),
    ]
