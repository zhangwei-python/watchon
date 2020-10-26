from django.db import models

# Create your models here.

class BookInfo(models.Model):

    btitle = models.CharField(max_length=20, verbose_name="书名")
    bpub_date = models.DateField(verbose_name="发布日期")
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = "tb_books"

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):

    GENDER_CHOICE = (
        (0, "female"),
        (1, "male")
    )

    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="英雄属于的图书")
    hname = models.CharField(max_length=20, verbose_name="人名")
    hgender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name="性别")
    hcomment = models.CharField(max_length=200, verbose_name="描述")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = "tb_heros"

    def __str__(self):
        return self.hname


"""
=======================过滤查询=======================
#1.查询编号为1的图书。
BookInfo.objects.filter(id=1)
BookInfo.objects.filter(id__exact=1)

#2.查询书名包含'传'的图书。contains
BookInfo.objects.filter(btitle__contains='传')

#3.查询书名以'部'结尾的图书 endswith startswith
BookInfo.objects.filter(btitle__endswith="部")
BookInfo.objects.filter(btitle__startswith="天")

#4.查询书名不为空的图书。 isnull = False
BookInfo.objects.filter(btitle__isnull=False)

#5.查询编号为1或3或5的图书  in
BookInfo.objects.filter(id__in=[1,3,5])

#6.查询编号大于3的图书 gt/lt/gte/lte
BookInfo.objects.filter(id__gt=3)

#7.查询编号不等于3的图书 exclude
BookInfo.objects.exclude(id=3)

#8.查询1980年发表的图书。year/month/day/...
BookInfo.objects.filter(bpub_date__year=1980)

#9.查询1980年1月1日后发表的图书。
BookInfo.objects.filter(bpub_date__gt="1990-01-01")


======================================F对象和Q对象=====================================
F对象: 两个属性进行比较时，使用F对象.
Q对象: 多个过滤条件逻辑运算时使用，&，|，~

from django.db.models import F, Q

#1.查询 阅读量 大于等于 评论量的 图书
BookInfo.objects.filter(bread__gt=F("bcomment"))

#2.查询 阅读量 大于2倍 评论量的 图书
BookInfo.objects.filter(bread__gt=F("bcomment")*2)

#3.查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(bread__gt=20, id__lt=3)
BookInfo.objects.filter(bread__gt=20).filter(id__lt=3)
BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))

#4.查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))

#5.查询编号不等于3的图书 exclude
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

======================聚合函数==================

# 查询图书的总阅读量。aggregate(Sum)
BookInfo.objects.aggregate(Sum("bread"))

======================排序=====================
order_by(属性名) 
    属性名: 升序
    -属性名：降序
# 图书阅读量降序排序. order_by
BookInfo.objects.all().order_by("-bread")

======================关联查询==================
一查多关联查询: 一对象.多类名小写_set
#案列：查询天龙八部中所有英雄
b = BookInfo.objects.get(btitle='天龙八部')
b.heroinfo_set.all()


多查一关联查询: 多对象.外键
#案列：查询令狐冲英雄属于哪个本书籍 
h = HeroInfo.objects.get(hname="令狐冲")
h.hbook
"""
from django.db.models import F, Q, Sum


