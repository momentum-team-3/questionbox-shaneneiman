# Generated by Django 3.1.1 on 2020-09-10 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.question'),
        ),
    ]
