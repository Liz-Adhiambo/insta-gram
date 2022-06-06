# Generated by Django 4.0.5 on 2022-06-06 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instasocial', '0004_followerscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('postc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instasocial.post')),
            ],
        ),
    ]
