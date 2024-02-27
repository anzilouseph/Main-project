# Generated by Django 3.2.22 on 2024-02-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('place', models.CharField(max_length=60)),
                ('phone', models.BigIntegerField()),
                ('Email', models.CharField(max_length=60)),
                ('Wedsite', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=60)),
                ('Last_name', models.CharField(max_length=60)),
                ('Address', models.CharField(max_length=60)),
                ('Phone', models.BigIntegerField()),
                ('Email', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=60)),
                ('option1', models.CharField(max_length=60)),
                ('option2', models.CharField(max_length=60)),
                ('option3', models.CharField(max_length=60)),
                ('option4', models.CharField(max_length=60)),
                ('Answer', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='vaccancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=600)),
                ('Vaccancy', models.CharField(max_length=60)),
                ('qualification', models.CharField(max_length=60)),
                ('exp', models.CharField(max_length=60)),
                ('salary', models.CharField(max_length=60)),
                ('details', models.CharField(max_length=700)),
                ('COMPANY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.company')),
            ],
        ),
        migrations.CreateModel(
            name='vac_qn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('Answer', models.CharField(max_length=500)),
                ('vaccancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.vaccancy')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=60)),
                ('Last_name', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=60)),
                ('place', models.CharField(max_length=60)),
                ('post', models.CharField(max_length=60)),
                ('pin', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=60)),
                ('photo', models.FileField(upload_to='')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.login')),
            ],
        ),
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
            ],
        ),
        migrations.CreateModel(
            name='tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips', models.CharField(max_length=60)),
                ('details', models.CharField(max_length=60)),
                ('GUIDE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.guide')),
            ],
        ),
        migrations.CreateModel(
            name='test_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('res', models.CharField(max_length=60)),
                ('ans', models.CharField(max_length=60)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
                ('quetion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.questions')),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_name', models.CharField(max_length=60)),
                ('date', models.CharField(max_length=60)),
                ('GUIDE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.guide')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=60)),
                ('date', models.DateField(max_length=60)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.login')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='TEST',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.test'),
        ),
        migrations.CreateModel(
            name='guideline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guidelines', models.CharField(max_length=60)),
                ('details', models.CharField(max_length=60)),
                ('GUIDE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.guide')),
            ],
        ),
        migrations.AddField(
            model_name='guide',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.login'),
        ),
        migrations.CreateModel(
            name='doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubt', models.CharField(max_length=60)),
                ('reply', models.CharField(max_length=60)),
                ('date', models.DateField(max_length=60)),
                ('GUIDE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.guide')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.CharField(max_length=60)),
                ('Date', models.DateField(max_length=60)),
                ('Reply', models.CharField(max_length=60)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.login'),
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('message', models.CharField(max_length=1000)),
                ('fromid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='f', to='interview.login')),
                ('toid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t', to='interview.login')),
            ],
        ),
        migrations.CreateModel(
            name='app_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=60)),
                ('status', models.CharField(max_length=60)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
                ('vaccancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.vaccancy')),
            ],
        ),
        migrations.CreateModel(
            name='answer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=60)),
                ('emot', models.CharField(max_length=60)),
                ('date', models.DateField(max_length=60)),
                ('oans', models.CharField(max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.user')),
                ('vac_qn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.vac_qn')),
            ],
        ),
    ]
