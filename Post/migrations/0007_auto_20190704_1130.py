# Generated by Django 2.2.2 on 2019-07-04 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20190704_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatedcomments', to='Post.Post'),
        ),
    ]
