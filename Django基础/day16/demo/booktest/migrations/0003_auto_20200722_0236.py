# Generated by Django 2.2.5 on 2020-07-22 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20200722_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bcomment',
            field=models.IntegerField(default=0, verbose_name='评论量'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateField(verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bread',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo', verbose_name='英雄属于的图书'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=200, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.SmallIntegerField(choices=[(0, 'female'), (1, 'male')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hname',
            field=models.CharField(max_length=20, verbose_name='人名'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
    ]
