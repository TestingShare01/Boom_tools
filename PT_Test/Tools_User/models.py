from django.db import models

class User(models.Model):
    user= models.CharField(max_length=100,verbose_name="用户名",unique=True)
    pwd = models.CharField(max_length=100,verbose_name="密码")
    token = models.CharField(max_length=200,verbose_name="token",default="")
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "User"

class Dev(models.Model):
    username = models.CharField(max_length=100,verbose_name="所属者") # 归属者
    dev_status = models.CharField(max_length=32,verbose_name="所属端") # 所属端
    devname = models.CharField(max_length=200,verbose_name="设备名") # 设备名
    version = models.CharField(max_length=32,verbose_name="系统版本") # 设备系统
    size = models.CharField(max_length=32,verbose_name="分辨率") # 分辨率
    serial = models.CharField(max_length=200,verbose_name="序列号") # 序列号
    status = models.CharField(max_length=32,verbose_name="设备状态") # 设备状态
    remark = models.CharField(max_length=500,verbose_name="备注") # 备注
    create_time = models.DateField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table = "Dev"

class Tags(models.Model):
    tagname = models.CharField(max_length=100,verbose_name="标签名")
    create_time = models.DateField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table = "Tags"