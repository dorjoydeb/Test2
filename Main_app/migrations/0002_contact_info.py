# Generated by Django 3.2.7 on 2021-10-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=550)),
                ('Phone', models.IntegerField()),
                ('B_phone', models.IntegerField()),
            ],
        ),
    ]