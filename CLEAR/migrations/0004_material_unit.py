# Generated by Django 5.0 on 2024-01-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLEAR', '0003_material_markup_material_type_alter_material_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='unit',
            field=models.CharField(default='default', max_length=15),
            preserve_default=False,
        ),
    ]