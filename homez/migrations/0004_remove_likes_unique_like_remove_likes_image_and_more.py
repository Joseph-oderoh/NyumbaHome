# Generated by Django 4.0.4 on 2022-06-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homez', '0003_likes_alter_comment_options_remove_comment_comment_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='likes',
            name='unique_like',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='image',
        ),
        migrations.AddField(
            model_name='likes',
            name='nyumbani',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_count', to='homez.nyumbani'),
        ),
        migrations.AddConstraint(
            model_name='likes',
            constraint=models.UniqueConstraint(fields=('user', 'nyumbani'), name='unique_like'),
        ),
    ]
