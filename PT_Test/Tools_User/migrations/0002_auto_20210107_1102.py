# Generated by Django 3.1.1 on 2021-01-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tools_User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('dev_status', models.CharField(max_length=32)),
                ('devname', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=32)),
                ('size', models.CharField(max_length=32)),
                ('serial', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=32)),
                ('remark', models.CharField(max_length=500)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Dev',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=100, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.CharField(max_length=100, verbose_name='用户名'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
