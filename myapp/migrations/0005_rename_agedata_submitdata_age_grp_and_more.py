# Generated by Django 4.2.4 on 2023-10-12 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_data1_submitdata_locdata_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submitdata',
            old_name='AgeData',
            new_name='AGE_GRP',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='LocData',
            new_name='GENDER',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='BudgetData',
            new_name='INCOME',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='CompanionData',
            new_name='TRAVEL_COMPANIONS_NUM',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='MotiveData',
            new_name='TRAVEL_MOTIVE_1',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue1',
            new_name='TRAVEL_STYL_1',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue2',
            new_name='TRAVEL_STYL_2',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue3',
            new_name='TRAVEL_STYL_3',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue4',
            new_name='TRAVEL_STYL_4',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue5',
            new_name='TRAVEL_STYL_5',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue6',
            new_name='TRAVEL_STYL_6',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue7',
            new_name='TRAVEL_STYL_7',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='StyleValue8',
            new_name='TRAVEL_STYL_8',
        ),
        migrations.RenameField(
            model_name='submitdata',
            old_name='MfmData',
            new_name='city',
        ),
    ]
