原作者： [w-devin](https://github.com/w-devin/Seat) & BinYou

## 安装

### 运行环境

python3

mysql (关系型数据库均可)

### 准备

1. Ubuntu 的服务器(会配置python的其他电脑均可)
2. ssh工具

### 开始

1. **下载源码**

```bash
 git clone https://github.com/lisongqian/ujn_library.git ujnlib
 cd ujnlib
```

2. **安装python3环境（目前不建议使用python3.7）**

```bash
 sudo apt-get install python3
 sudo apt-get install python3-pip
 sudo pip3 install -r requirements.txt
```

3. **安装MySQL**

```bash
 sudo apt-get install mysql-server
```

4. **启动MySQL服务**

```
 cd 
 mysql -h localhost -u root -p
```

5. **创建数据库**

```sql
 mysql> create database seats;
 mysql> use seats;

 mysql> source Database/admin.sql;
 mysql> source Database/rooms.sql;
 mysql> source Database/seats.sql;
 mysql> source Database/tasks.sql;


 mysql> insert into admin values(0, 'wang', '123456');
 #创建管理员账户, 其中第一个数字0是指超级管理员, 超级管理员只能有一个, 能看到并管理其他所有管理员创建的记录, 普通管理员则只能看到和创建自己创建的记录
 mysql> exit;
```

5. **配置数据库**

`./Seats/db.py`文件第11行：

```
mysql://user_name:user_password@address:3306/database_name?driver=connector
```

`user_name`: 连接数据库用户名

`user_password`: 连接数据库密码

`address`: 数据库地址(当前为`localhost`或`127.0.0.1`)

`database_name`: 数据库名(当前为`Seats`)

6. 启动服务

```
 sudo python3 runserver.py
```

<p style="color:red;">注意，程序启动后当前会话不可关闭!</p>

### 其他配置

- `runserver.py` 第20行`5555`端口可更改

```
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
```

- `config.py`  见代码注释

```json
JOBS = [
        {
            'id': 'booking',
            'func': 'tasks:booking',# 座位预约服务
            'args': (),
            'trigger': {
                'type': 'cron',
                'day_of_week': "mon-sun",
                'hour': '5',       #5h
                'minute': '0-1',   #0min到1min
                'second': '2,5,10' #2s、5s或10s时
            }# 早晨5:00:02,5:00:05,5:00:10,5:01:02,5:01:05,5:01:10时尝试进行次日座位预约，下同
        }
        ,
        {
            'id': 'checkin',
            'func': 'tasks:checkin',
            'args': '',
            'trigger': {
                'type': 'cron',
                'day_of_week': "mon-sun",
                'hour': '8',
                'minute': '0',
                'second': '11'
            }
        },
        {
            'id': 'clearLog',
            'func': 'tasks:clearLog',
            'args': '',
            'trigger': {
                'type': 'cron',
                'day_of_week': "mon-sun",
                'hour': '8',
                'minute': '0',
                'second': '11'
            }
        }
    ]
```

- 设置网站主页的显示内容

更改`./Seats/templates/index.html`第5-12行内容

## 彩蛋！

- 默认每天早上5点开始，进行4次预约尝试；
- 添加的预约任务若不删除则会继续预约；
- 登录时账号密码错误服务器会报错，返回上一页重新登录即可；
- 新建记录时, 输入的时间的单位为小时, 修改记录时单位则为分钟；
- `msg.log` 为前几项记录的日志和所有记录的密码错误信息；



**祝：考研成功！**