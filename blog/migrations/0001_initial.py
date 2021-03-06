# Generated by Django 2.0.4 on 2019-02-25 04:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(default='http://wx1.sinaimg.cn/large/006gFOhdly1fr0hdrzlolj30b40b4dg7.jpg', max_length=1000, verbose_name='头像')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '博文评论',
                'verbose_name_plural': '博文评论',
            },
        ),
        migrations.CreateModel(
            name='Commentcoment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(default='http://wx1.sinaimg.cn/large/006gFOhdly1fr0hdrzlolj30b40b4dg7.jpg', max_length=1000, verbose_name='头像')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name='留言')),
            ],
            options={
                'verbose_name': '博文回复',
                'verbose_name_plural': '博文回复',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SmallIntegerField(choices=[(1, 'django'), (2, 'flask学习'), (3, '爬虫教程'), (4, '编程项目'), (5, '生活推荐'), (6, '视频分享')], default=0, verbose_name='分类')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('image', models.CharField(default='//ws3.sinaimg.cn/large/6f8a2832gy1fj7xtfzb5kj23pj2lonpi.jpg', max_length=1000, verbose_name='图片')),
                ('body_text', models.TextField(verbose_name='正文')),
                ('input_time', models.DateTimeField(default=datetime.datetime(2019, 2, 25, 12, 54, 44, 67579), verbose_name='时间')),
                ('out_time', models.DateTimeField(default=datetime.datetime(2019, 2, 25, 12, 54, 44, 67579), verbose_name='修改时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
            ],
            options={
                'verbose_name': '博文管理',
                'verbose_name_plural': '博文管理',
            },
        ),
        migrations.CreateModel(
            name='Frend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='网站名')),
                ('head', models.CharField(max_length=1000, verbose_name='头像')),
                ('url', models.URLField(verbose_name='网站链接')),
                ('text', models.TextField(verbose_name='网站介绍')),
                ('yes', models.SmallIntegerField(choices=[(0, '未通过'), (1, '通过')], default=0, verbose_name='状态')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2019, 2, 25, 12, 54, 44, 67579), verbose_name='时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250, verbose_name='姓名')),
                ('user_img', models.CharField(default='http://wx1.sinaimg.cn/large/006gFOhdly1fr0hdrzlolj30b40b4dg7.jpg', max_length=1000, verbose_name='头像')),
                ('usertext', models.TextField(default=' ', max_length=250, verbose_name='个人介绍')),
                ('usertime', models.DateTimeField(default=datetime.datetime(2019, 2, 25, 12, 54, 44, 67579), verbose_name='加入时间')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Entry', verbose_name='文章'),
        ),
    ]
