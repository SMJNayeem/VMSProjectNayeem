# Generated by Django 3.1.7 on 2021-06-25 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vmsUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisition',
            old_name='deprtr_time',
            new_name='departr_time',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='department',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='user_name',
        ),
        migrations.AddField(
            model_name='requisition',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requisition',
            name='is_requisited',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='aplctn_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Requisition Date'),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='jour_date',
            field=models.DateField(blank=True, null=True, verbose_name='Journey Date'),
        ),
    ]