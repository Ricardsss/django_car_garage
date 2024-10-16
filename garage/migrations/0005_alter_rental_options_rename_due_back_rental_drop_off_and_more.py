# Generated by Django 5.1.1 on 2024-10-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_alter_car_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'ordering': ['drop_off']},
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='due_back',
            new_name='drop_off',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='taken',
            new_name='pick_up',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='returned',
        ),
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('u', 'Unavailable'), ('m', 'Maintenance')], default='a', max_length=1),
        ),
    ]
