# 哈哈新闻
这是通过Django编写的一个简易后台，为了这个后台，有必要给自己增加点知识储备了[RESTful](http://www.ruanyifeng.com/blog/2011/09/restful)
# 关于MySQL的一些操作
在setting.py中设置DATABASE
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hhnews',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```
使用了pymysql模块，只需要使用pip install pymysql，还有一个地方要注意的是，如果当前环境中没有安装mysqlclient的话，还需要用pip安装一下，不然会导致在初始化表的时候报错python manage.py makemigrations
# 设置语言
在setting.py中设置`LANGUAGE_CODE = 'zh-Hans'`  表示使用中文简体
如果一些简单的模块可以不使用csrf这一个中间件，去setting.py中注释一下就可以了
#关于登录注册模块的密码加密
用户注册部分涉及到隐私数据时，一定要进行加密，否则用户隐私泄露的风险承担不起。
Django中自带了一个加密和验证的模块
    `from django.contrib.auth.hashers import make_password, check_password`
操作也简单，只需要将用户POST过来的密码make_password()之后存入到数据库中，验证的时候根据用户名从数据库中获取到密码，在使用check_password()方法会返回一个布尔值。

# Django的一些常用查询语句
例:
```
User.objects.filter(username).values('password')
```
这个语句翻译成MySQL的话就是
```
SELECT password from User WHERE username = 'xxx'
```
Django的ORM写的很完善了，只要数据访问量不是特别大的，基本都没问题，流量过大的话还是SQL语句的性能表现更好