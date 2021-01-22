from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from Tools_User import models
from logzero import logger
from Tools_User.tools.common import *
from Tools_User import Seari
# 登陆相关
class Login(APIView):
    def post(self,request,*args,**kwargs):
        dtic={}
        user = request.data.get("username")
        pwd = request.data.get('pwd')
        user = models.User.objects.filter(user=user)
        if(user):
            pwds = user.first().pwd
            if(pwd==pwds):
                tokens = set_token()
                dtic["error_code"] = 0
                dtic["msg"] = "登录成功"
                dtic["user"] = user[0].user
                dtic["token"] = tokens
                user.update(token=tokens)
            else:
                dtic["error_code"] = 1001
                dtic["msg"] = "密码错误"
        else:
            dtic["error_code"] = 1001
            dtic["msg"] = "账号不存在"
        return Response(dtic)

    def get(self,request,*args,**kwargs):
        return Response("请使用正确方式登陆")

#设备数据管理
class DevList(APIView):
    def get(self,request,*args,**kwargs):
        dev = request._request.GET["dev"]
        logger.info(dev)

        if dev == "1":
            dev_list = models.Dev.objects.filter(dev_status="Android")
        elif dev == "2":
            dev_list = models.Dev.objects.filter(dev_status="IOS")
        else:
            dev_list = models.Dev.objects.all()

        dev_list = Seari.DevSerializers(dev_list,many=True)
        return Response(dev_list.data)

    def post(self,request,*args,**kwargs):
        dtic={}
        try:
            user = request.data.get("username")
            dev = request.data.get("dev_status")
            devname = request.data.get("devname")
            version = request.data.get("version")
            size = request.data.get("size")
            serial = request.data.get("serial")
            remark = request.data.get("remark")
            models.Dev.objects.create(username=user,dev_status=dev,devname=devname,version=version,size=size,serial=serial,status=0,remark=remark)
            dtic["error_code"] = 0
            dtic["msg"] = "添加成功"
        except Exception as e :
            dtic["error_code"] = 10002
            dtic["msg"] = "添加失败，后端报错->{}".format(e)
        return Response(dtic)

    def delete(self,request,*args,**kwargs):
        dtic={}
        try:
            id = request.data.get("id")
            models.Dev.objects.filter(id=id).delete()
            dtic["error_code"] = 0
        except Exception as e:
            dtic["error_code"] = 10003
            dtic["msg"] = "删除失败->{}".format(e)
        return Response(dtic)

#标签管理
class ApiTag(APIView):
    def get(self,request):
        dtic={}
        try:
            tages = models.Tags.objects.all()
            tages = Seari.TageSerializers(tages,many=True)
            dtic["error_code"]=0
            dtic["res"] = tages.data
        except Exception as e:
            dtic["error_code"]= 10003
            dtic["msg"] = "请求问题->{}".format(e)
        return Response(dtic)

    def post(self,request,*args):
        dtic={}
        try:
            name = request.data.get("tagname")
            tagsname = models.Tags.objects.filter(tagname=name)
            if(tagsname):
                dtic["error_code"] = 10005
                dtic["msg"] = "标签已存在"
            else:
                models.Tags.objects.create(tagname=name)
                dtic["error_code"] = 0
                dtic["msg"] = "添加成功"
        except Exception as e:
            dtic["error_code"] = 10004
            dtic["msg"] = "请求报错->{}".format(e)
        return Response(dtic)