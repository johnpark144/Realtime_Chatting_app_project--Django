# Generated by Django 4.0.6 on 2022-08-26 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatting_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatting_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('room_name', models.CharField(max_length=50)),
                ('about_room', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='chatting',
            name='chatting_room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatting_app.chatting_room'),
            preserve_default=False,
        ),
    ]