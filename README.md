# alipay_red_helper

支付宝抢红包助手

### 演示环境

* archlinux 
* xfce desktop

### 开发依赖

* openjdk or oracle jdk
* Android SDK

### 项目简介

* 基于 android monkeyrunner 实现,非直接修改数据包,所以不能称为外挂,只能称为助手.

### 步骤

* 首先简单的搭建 android 的相关环境,主要是安装android sdk. 下载地址 http://developer.android.com/sdk/index.html#Other
* 下载 Android Platform Tool
* 开启手机的调试,像linux一般还需要添加udev文件,就像windows下一般需要安装驱动一样. arch 可以直接安装包即可, https://wiki.archlinux.org/index.php/Android#Connecting_to_a_real_device_-_Android_Debug_Bridge_.28ADB.29
* adb shell, 测试是否可以连接上手机
* 运行脚本,记得路径改成你自己的 ./monkeyrunner ~/workspace/alipay_red_helper/red_helper.py


### 结尾

支付宝 cutdeer@vip.qq.com
