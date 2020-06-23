#### 第一章	安装和配置mysql

##### 1.1	安装mysql

1. 去官网下载 mysql-5.7.27-linux-glibc2.12-x86_64.tar

2. 上传到linux，使用tar -xvf mysql-5.7.27-linux-glibc2.12-x86_64.tar

   1. tar -xzvf mysql-5.7.27-linux-glibc2.12-x86_64.tar.gz

4. mv  mysql-5.7.27-linux-glibc2.12-x86_64 /usr/local/mysql

5. 创建/var/run/mysqld

6. chown mysql:mysql -R /var/run/mysqld

7. vim /etc/my.cnf

8. 添加如下内容：

   ```
   [mysqld]
   bind-address=0.0.0.0
   port=3306
   user=mysql
   basedir=/usr/local/mysql
   datadir=/usr/local/mysql/data
   socket=/tmp/mysql.sock
   log-error=/var/log/mysqld.log
   user=mysql
   port=3306
   pid-file=/var/run/mysqld/mysqld.pid
   #character config
   character-set-server=utf8
   symbolic-links=0
   skip-grant-tables
   
   ```

7.  初始化，cd /usr/local/mysql/bin， 使用 ./mysqld --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data/ --user=mysql --initialize

8. cp  /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql

9. 启动mysql, service mysql start

10. ./mysql -u root -p  不需要登录密码就可以登录

11. 设置密码

    ```
    >>use mysql;
    >>update user set authentication_string=password('你的密码') where user='root';
    >>flush privileges;
    ```

12. 允许远程连接

    ```
    /usr/local/mysql/bin/mysql -u root -p
    >>use mysql;
    >>update user set host='%' where user = 'root';
    >>flush privileges;
    >>eixt;
    ```

##### 1.2 卸载mysql

1. 查看当前安装情况，rpm -qa | grep -i mysql

2. 停止Mysql的服务，service mysql stop

3. 删除之前安装的mysql，将第一步查到的包都逐个删除

   rpm -ev mysql-client-5.x.x --nodeps

4. 查找之前mysql的目录，删除其文件和目录

   find / -name mysql

5. 删除对应的mysql目录

   rm -rf xxxxxx

6. 卸载后/etc/my.cnf不会删除，需要进行手工删除

   rm -rf /etc/my.cnf

7. 再次查找mysql是否仍有残留

   rpm -qa | grep -i mysql

##### 1.3 添加server服务

可以使用service mysql start命令

```
cp -a /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql
```

##### 1.4 添加环境变量

可以在任何路径下使用mysql -uroot -p

```
ln -s /usr/local/mysql/bin/ /bin
```

##### 1.5 添加到systemctl服务

可以使用systemctl start mysqld.service

```
#vim /usr/lib/systemd/system/nginx.service
[Unit]
Description=nginx - high performance web server
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
ExecStart=/usr/lib/nginx/sbin/nginx
ExecReload=/usr/lib/nginx/sbin/nginx -s reload
ExecStop=/usr/lib/nginx/sbin/nginx -s stop

[Install]
WantedBy=multi-user.target
————————————————
版权声明：本文为CSDN博主「blueicex2020」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/blueicex2017/java/article/details/104207946
```



#### 第二章	mysql服务使用命令

##### 2.1 常用命令

启动命令：service mysql start

停止命令：service mysql stop

重启命令：service mysql restart

查看状态：service mysql status

##### 2.2 常见问题

- ##### 发现问题一：

执行mysql命令报错如下：

You must reset your password using ALTER USER statement before executing this statement.

这个问题通常因为密码过期导致

```
ALTER USER 'root@localhost' IDENTIFIED BY '123456';修改密码
ALTER USER USER() IDENTIFIED BY '123456'; 修改当前用户密码
ALTER USER 'jeffrey'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE; 当前密码过期
ALTER USER 'jeffrey'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER;  密码永不过期
ALTER USER 'jeffrey'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE DEFAULT; 设置密码按照默认的时期过期
ALTER USER 'jeffrey'@'localhost' IDENTIFIED BY '123456' PASSWORD EXPIRE INTERVAL 90 DAY;设置密码的过期时间
SET PASSWORD FOR 'jeffrey'@'localhost'  = '123456' 设置密码
```

- ##### 发现问题二：


重启服务器后启动mysql，报错：The server quit without updating PID file

这个问题通常是因为mysqld-pid这个文件没有被写入导致

解决办法：

查看一下my.cnf配置文件里的mysqld-pid文件路径是否开放权限或者是否存在

```
chown -R mysql:mysql /var/run/mysqld/ 然后重启mysqld
mkdir /var/run/mysqld
```

- ##### 发现问题三：


使用navicat远程连接mysql，报错不成功

解决方法：

1. 阿里云服务器安全组配置增添3306端口，然后重启服务器

2. 查看防火墙开放的端口有没有3306，如果没有则需要增添

   ```
   firewall-cmd --list-port  查看防火墙开放端口
   firewall-cmd --permanent --add-port=3306/tcp 添加开放端口
   firewall-cmd --reload  开放端口生效
   ```

3. 新增一个mysql的远程用户

   ```
   create user 'netuser'@'%' identified by 'password' 新增一个远程用户
   flush privileges; 更新权限
   grant all on *.* to 'netuser'@'%' 给该用户分配所有权限
   ```

4. 打开/etc/my.cnf注释bind-address = 127.0.0.1，注释skip-netwoking

#### 第三章    SQL操作语句分类

##### 3.1 DDL 数据定义语言，建库，建表

建库语句

```
create database db01;
create database if not exists db01;
create database default character set gbk;
```

建表语句

```
create table mytab01(
	eno int(5) not null zerofill auto_increment primary key,
    ename varchar(10) default null comment '雇员姓名',
    depno int(4) not null unsigned unique key,
    sex char(5) comment '雇员性别',
    unique key(depno)
);
#这里的primary key，auto_increment,zerofill有很多知识点，暂时先放弃
```

复制表结构或数据

```
create table mytab01 like mytab02; #复制表结构
create table mytab01 as select * from mytab02 where 1=2; #复制表结构，但是经常索引复制不过来，不推荐
create table mytab01 as select * from mytab02;#复制表结构和表数据
```

日常操作语言

```
select database();	#查看当前选中的数据库
show databases;	#查看数据库列表
show tables;	#查看数据库的表列表
show create database db01;	#查看数据库编码
show create table mytab01;	#查看建表语句和表编码和引擎
desc mytab01;	#查看表结构
show full columns from mytab01;	 #查看字段编码
use db01;
rename table 旧表名 to 新表名;
```

\g：sql语句结束
\G：sql语句结束，数据显示纵向旋转90度

表常用的约束条件

```
unique key	#唯一性，数据不能重复，允许空值，一张表可以有多个唯一键
zerofill	#自动补0，配合int(5)使用，一种输出格式化属性
unsigned	#设为非负数，可以用来增加数据长度，比如tinyint unsigned 数据范围为127*2
auto_increment	#自动增长，只能适用于整型数据对字符串无效，正序增加，被标识为自动增长的字段一定是主键，但是主键不一定要设为自动增长
default	#默认值
comment	#添加备注
not null #不为空
primary key #不允许为空值，一张表只能有一个主键
```

表结构的修改或删除操作

```
#在工作字段后面添加新字段‘地址’
alter table mytab01 add address varchar(20) after job;
#在第一个字段前添加date新字段
alter table mytab01 add date date first	
#删除字段
alter table mytab01 drop job;	
#给表新增主键
alter table mytab01 add primary key(test_no);
#删除表的主键
alter table mytab01 drop primary key;
#给表新增外键约束
alter table mytab01 add foreign key
#修改字段的类型
alter table mytab01 modify ename varchar(20)
#修改字段的名称
alter table mytab01 change job depname varchar(20)	
#修改表的字符编码
alter table mytab01 character set gbk;
#修改字段的字符编码
alter table mytab01 change oldname newname character set gbk;
#删除表(表的数据和结构都会没有)
drop table mytab01;	
#删除数据库(数据库的结构)
drop database db01;	
```

问题：使用alter database/table name character set *，只能更改新生记录的字符集，而已有的记录字符集是没有办法更改的。

1、建库以及建表的语句导出，sed批量修改为utf8

2、导出所有数据

3、修改mysql服务器和客户端编码为utf8

4、删除原有的库表已经数据

5、导入新的建库已经建表语句

6、导入mysql的所有数据

##### 3.2 DML 数据操作语言，对表中的数据进行增删改查

```
insert into 表名 字段名 values 字段值;
insert into mytab01(ename,sex) values('suzy','女');
insert into 表名 values (全字段值);
insert into mytab01 values ('1001','小明','男','文员','北京朝阳区');
```

```
#蠕虫复制
insert into mytab01 select * from mytab02;
insert into mytab01 (ename,job) select ename,job from mytab02;
```

```
#建表复制
create table mytab01 as select * from mytab02;
#一次插入多条数据
insert into mytab01 values('ss','女'),('yy','男'),('dd','女')
```

修改表数据 

```
update 表名 set 字段1=字段值 where 字段=值;
update mytab01 set ename=ss where ename=yy; 注：一定要加where条件，不然会全部更改值
update 表名 set 字段1=值1,字段2=值2 where 字段=值；
```

删除表数据

```
delete from 表名 where 字段=值 #删除某条记录，删除id=5的记录，auto_increment值会从6开始
drop table mytab01; 注:同时删除数据和表结构
delete from 表名;	# 只删除数据不会删除表定义，会把删除的数据记录下来，方便回退，不会释放空间
truncate table 表名;	#只删除表数据不删除表定义，会释放空间，auto_increment值会从1开始
alter table mytab01 auto_increment=1; #也可以强行是新增记录从auto_increment值从1开始
```

查询mysql使用的字符编码变量

```
show variables like 'character%';
```

临时显示使用字符集gbk

```
set names gbk;
```

永久修改字符集的方法，打开/etc/my.cnf

```
[client]
default-character-set=gbk
[mysqld]
character_set_server=gbk
```

修改字符编码集

```
#修改库的字符编码集
alter database db01 default character set gbk;
#修改表的字符编码集
alter table mytab01 default character set gbk;
#修改字段的字符编码集
alter table mytab01 modify ename varchar(50) character set gbk;
```

注：alter table mytab01 modify ename character set gbk; 报错了，必须加varchar

##### 3.3 DQL 数据查询语言，对数据进行查询

```
#对字段增加auto_increment
alter table mytab01 change id id int auto_increment; #给该字段增加auto_increment约束
此时新增数据，id自动生成
alter table mytab01 change id id int; #删掉该字段的auto_increment约束
此时新增数据，会报错，id必须有值
```

简单查询

```
select * from employee; 注：尽量不要直接用该语句查全表数据，性能会很慢
select ename,job as e_job from employee
```

精确查询

```
select * from employee where ename='sss';
select * from employee where sal!=7500;
select * from employee where sal>10000;
select * from employee where sal<>5500;
select * from employee where ename like '张%';
```

范围查询

```
select * from employee where sal between 10000 and 20000;
select * from employee where sal between '2013-02-16' and '2018-02-20';
```

日期的比较

​	如果你存储的格式是YY-mm-dd是这样的，你就可以使用DATE()函数用来返回日期的部分

```
select * from employee where Date(datetime)>'2020-02-21'
```

​	如果你存储的格式是2013-01-12 23:23:56这种格式，你就可以使用timestamp()函数来比较

```
select * from product where timestamp(add_time)='2013-01-12 23:23:56'；
```

​	你还可以使用Year()和Month()

```
select * from product where Year(add_time) = 2013 and Month(add_time) = 1 #1月份的产品
```

	mysql> SELECT something FROM table 
	WHERE TO_DAYS(NOW()) - TO_DAYS(date_col) <= 30;  #最后30天内		

​	使用DAYOFWEEK(date)返回日期date的星期索引

```
select dayofweek('2020-02-26');
```

​	DAYOFWEEK(date)返回日期date的星期索引

​	DAYOFMONTH(date)返回日期date的月日期，1-31

​	DAYOFYEAR(date)返回日期date的年日期，1-366

​	DAYNAME(date)返回date的星期名字

​	MONTHNAME(date)返回date的月份名字

​	QUARTER(date)返回date一年中的季度，范围1到4。

离散查询

```
select * from employee where job in ('销售员','文员');
```

消除重复值
select distinct(job) from employee;

统计查询，聚合函数

``` 
select sum(sal) from employee where sal>=10000;
select avg(sal) from employee;
select count(*) from employee;
select max(sal) from employee;
select ename from employee where sal=(select max(sal) from employee);注：不要直接用sal=max(sal)会报错
```

group by 通常用于统计结果的筛选，一般与聚合函数一起使用

```
select deptnu,count(*) from employee group by deptnu;
select deptnu,job,count(*) from employee group by deptnu,job;
```

having 语句通常跟在group by后面，用于获取统计中的某项

```
select deptnu,job,count(*) from employee group by deptnu,job having count(*)>=2;

```

order by对查询的结果进行排序

```
select * from employee order by ename asc
select * from employee order by ename desc;
select job,count(*) from employee group by job order by count(*); 
```

limit起到搜索结果起到限制条数的作用，例如：limit n,m(n代表起始条数值，默认为0，m代表条数)

```
select * from employee limit 2,4;
select * from employee limit 4\G
```

---- where ---- group by ---- having ---- order by ----

```
#exists子查询，作用是限制查询，如果exists为TRUE，则返回查询结果，如果为False，则返回空
select * from dept where exists (select * from employee where dept.deptnu = employee.deptnu)
select * from dept a where not exists (select * from employee b where a.deptnu = b.deptnu)
```

mysql查询之左连接查询与右连接查询

左右连接又称为左外连接和右外连接，左连接就是左表全部记录显示，右表部分显示符合条件的记录，不足的地方显示为NULL

例如： 

Left join 表名 on 条件 == left outer 表名 join on 条件

right jonin 表名 on 条件 == right outer 表名 join on 条件

```
select a.dname,b.* from dept a left join employee b on a.deptnu=b.deptnu;
#查询所有部门所对应的员工信息，包括显示没有员工的部门名称
```

mysql的查询条件判断关于日期的处理

date()	会返回"yyyy-mm-dd  hh: mm: dd" 的日期值

timestamp()	可以将"yyyy-mm-dd  hh: mm: dd"转为时间戳用来进行时间比较判断

例如：

```
select * from employee where date(hiredate) > "2012-01-01";
```

mysql查询之内连接查询

获取两个表中字段匹配关系的记录

例如：

inner join 表名 on 条件

```
select a.addr from dept a inner join employee b on a.deptnu=b.deptnu and b.ename='张飞'
select a.addr from dept a, employee b where a.deptnu=b.deptnu and b.ename="张飞"
```



##### 3.4 DCL 数据控制语言，对数据权限进行设置

1. ###### root用户的指定ip登录

   mysql -uroot -hlocalhost -p 

   ```
   select user,host from user where user='root'
   update user set host='localhost' where user='root';
   flush privilege;
   ```

2. ###### 修改用户密码

   ```
   #第一种
   mysqladmin -u root -p旧密码 password
   #第二种
   set password for root@localhost = password('密码')
   #第三种
   update mysql.user set authentication_string=password('密码') where user='root' and host='localhost'  注：host可能有多种，要区分
   #第四种
   alter user 'username'@'host' identified by '123456' password expire interval 90 day;
   ```

   忘记密码：

   修改/etc/my.cnf，添加skip-grant-tables跳过权限，重启mysql服务，登录mysql后重设密码。

3. ###### 创建新用户并限制用户IP登录

   创建mysql用户

   ``` 
   create user 'username'@'host' identified by 'password'; 
   #host指定在哪个主机可以登录，也可以为localhost,也可以任意主机都可以登录，通配符%
   create user 'pig'; #非常省略的写法，不推荐
   ```

   设置指定的IP网段登录

   ```
   update user set host='120.%.%.%' where user='pig';
   flush privileges;
   ```

   删除mysql用户

   ```
   drop user 'pig'@'host';
   delete from mysql.user where user='root';
   ```

   查看mysql用户权限

   ```
   show grants for 'pig'@'%'; #查看用户的权限
   select * from mysql.user where user='root';
   ```

4. ###### 库表授权和回收

   授权语法

   ```
   grant 权限1，权限2... on 数据库对象 to '用户'@'host' identified by 'password';
   #可以对现有用户也可以是不存在的用户授权
   all privileges #所有权限
   *.*	#代表所有库所有表
   grant all privileges on *.* to 'pig'@'host';	#针对已有用户授权
   grant all privileges on XD.* to 'pig'@'host' identified by 'password'
   grant select on XD.* to 'pig'@'host';	#只有查权限
   grant update,select on XD.employee to 'pig'@'%';	#授权修改，查询权限给用户
   ```

   回收权限语法

   ```
   revoke 权限1，权限2... on 数据库对象 from '用户'@'host';	#不能回收登录权限
   delete from mysql.user where user='pig';	#回收了它的登录权限
   ```


5. ###### mysql各种权限

   usage

   连接（登陆）权限，建立一个用户，就会自动授予其usage权限（默认授予）。

   ```
   mysql> grant usage on *.* to ‘p1′@’localhost’ identified by ‘123′
   ```

   该权限只能用于数据库登陆，不能执行任何操作；且usage权限不能被回收，也即REVOKE用户并不能删除用户，除非delete该用户从user表中。

   select/insert/update/delete

   必须有select的权限，才可以使用select table

   ```
   mysql> grant select on pyt.* to ‘p1′@’localhost’;
   ```

   create/alter/drop

   必须有create的权限，才可以使用create table

   ```
mysql> grant create on db01.* to 'p1'@'localhost';
   ```

   create routine/alter routine/drop routine
   
   必须具有create routine的权限，才可以使用{create |alter|drop} {procedure|function}

   ```
mysql> grant create routine on pyt.* to ‘p1′@’localhost’;
   ```

   create temporary tables

   create view/show view/drop view/

   创建视图的权限

   create user

   show database

   index

   必须拥有index权限，才能执行[create |drop] index

   lock tables

   必须拥有lock tables权限，才可以使用lock tables

   ```
mysql> grant lock tables on pyt.* to p1@localhost;
   
   ```

mysql> lock tables a1 read;

mysql> unlock tables;





#### 第四章	事务、视图、触发器、存储过程

##### 4.1 事务

目的一：提供一个从失败状态恢复到正常状态的方法，同时提供了数据库在异常状态下保持一致性的方法

目的二：多个应用并发访问数据库时，可以提供隔离方法，让彼此的操作互不干扰

- ###### 事务的特性（ACID）

  - 原子性	事务必须是原子工作单元，一个事务的所有语句要做到要么不做要么全做
  - 一致性	让数据保持逻辑上的合理性
  - 隔离性	多个事务并发执行，要保证事务的各自独立性
  - 持久性	一个事务执行成功，不仅仅是内存的变化，应该是明确的数据硬盘的更改

- ###### 事务的声明

  1. 数据表的engine=innodb，也就是引擎必需是Innodb

  2. begin......commit或者begin......rollback

  3. 此外如果autocommit=0，那么一句sql语句就不会自动提交了，需要commit提交。

  4. 【临时生效】

     ```
     set autocommit=0
     show variables like 'autocommit'
     ```

     【永久生效】在配置文件my.cnf中[mysqld]中添加autocommit=1

- ###### 事务example

  ```
  mysql>begin;
  mysql>insert into mytab01 values ('1','张三','OK');
  mysql>commit;(rollback)
  ```

##### 4.2 视图

视图是虚拟存在的表，是一个逻辑表，本身没有数据，其数据来源于基表。通过视图，可以展现基表的部分数据。

- ###### 视图的优点

  1. 简单

     视图用户不需要关心表结构，关联条件和筛选条件，只需要提取视图里的结果集

  2. 安全

     视图限制用户只能访问被允许查看的数据，权限管理并不能限制到表的某行某列，而视图可以

  3. 数据独立

     屏蔽了表结构改变对视图的影响

  4. 不占用空间

     视图是逻辑上的表，不占用空间

- ###### 视图的创建

  ```
  create view employview (id,name,job) as select empno,ename,job from employee;
  create or replace view employview;
  ```

- ###### 视图修改

  ```
  alter view employview (id,name,job,sal) as select empno,ename,job,sals from employee;
  ```

- ###### 删除视图

  ```
  drop view employview;
  ```

- ###### 视图缺点

  1. 性能差	sql必须把视图查询转换为对基本表的查询，如果视图查询太过于复杂，解释转换的时候就会耗费时间
  2. 修改限制	当用户试图修改试图的某些信息，数据库必须将它转换为对基本表的某些信息的修改，对于复杂视图就比较麻烦

##### 4.3 触发器

监视某种情况，触发某种操作

- ###### 触发器创建

  ```
  create trigger 触发器名称 after/before insert/update/delete  on 表名
  for each row
  begin
  sql语句
  end
  ```

- ###### 触发器删除

  ```
  drop trigger 触发器名称；
  ```

- ###### 触发器example

  ```
  create table work_time_delay (
  empno int not null comment '员工编号';
  ename varchar(50) comment '员工姓名';
  status int comment '出勤状态'
  );
  ```

  ```
  delimiter //
  create trigger work_trigger after insert on work_time_delay
  for each row
  begin
  update employee set sal=sal-100 where empno=new.empno;
  end
  # new 指的是befor或after保存的新数据。
  
  insert into mytab01 ('1004','猪八戒','1');
  ```

##### 4.4 存储过程

把复杂的一系列操作，封装成一个过程，类似shell脚本，python脚本

- ###### 存储过程的优缺点

  1. 优点

     复杂操作，调用简单

     速度快

  2.  缺点                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          封装复杂

     没有灵活性

  3. 创建存储过程

     ```
     create procedure 名称(参数)	#参数有in/out/inout
     begin
     	过程体
     end
     ```

     声明变量：declare 变量名 类型 default

     变量赋值：set @变量名=值

     调用存储命令： call 存储名称

     删除存储过程： drop procedure 存储过程

  4. 存储过程example 

     ```
     create procedure name(in n int)
     begin
     select * from employee limit n;
     end
     #赋值变量
     set @n=5;
     #调用存储过程
     call name(@n);
     #删除存储过程
     drop procedure name;
     ```

​     

#### 第五章   索引与存储引擎

##### 5.1什么是存储引擎

数据库底层软件组织，不同的存储引擎提供不同的存储机制，索引技巧和锁定水平等功能，不同的存储引擎有不同的特定功能。注：存储引擎是基于表不是基于库

- ###### 如何查看引擎

  ```
  show engines;
  show create table tab01;
  show table status\G #查看所有表的状态
  ```

- ###### 建表指定引擎

  ```
  create table tab01(id int,name varchar(20) engine='InnoDB');
  ```

- ###### 修改表的引擎

  ```
  alter table tab01 engine='MyisAM';
  ```

  vi /etc/my.cnf 修改默认引擎，然后重启mysql服务

  ```
  [mysqld]
  default-storage-engine=MyISAm
  ```

- ###### MyISAm和InnoDB的区别

  - MyIsAm不支持事务，支持全文索引，表级锁，读出表的具体行数，奔溃恢复不好

  - InnoDB支持事务，以前的版本不支持全文索引，行级锁，有时候也会是表级锁，不能读出表的具体行数，奔溃恢复好。

    ```
    update tab01 set id=3 where name like 'a%' 注：不确定该语句波及的范围，使用行级
    ```

- 使用范围

  MyISAm: 一般不需要支持事务，需要做很多count运算

  InnoDB: 、可靠性要求高的，需要支持事务

##### 5.2常用的索引

- 什么是索引

  单独存储在磁盘的数据结构，包含着对所有数据表里的记录的引用指针，使用索引可以快速查询到特定值的行

- 索引的优点

  通过创建唯一索引，来保证数据表的数据唯一性

- 索引的缺点

  索引需要占用物理空间

  对表中的数据进行更改，索引也要跟着动态维护，降低了数据的可维护性

- 常用的索引

  index	普通索引

  unique	唯一索引
  
  primary key	主键索引
  
  foreign key	
  
  full text
  
  组合索引

##### 5.3索引操作语句

- 创建表语句添加索引

  ```
  create table test(
  	id tinyint(4) zerofill auto_increment not null,
  	username varchar(20) ,
  	servnumber varchar(20) ,
  	password varchar(20),
  	createtime datetime,
  	primary key(id)
  )default charset=utf8;
  ```

  

- 修改表结构添加索引

  ```
  alter table test add index 索引名称(字段名);
  alter table test add index index_username(username); 注：如果没有指定索引名称，会默认为字段的名称
  ```

- 直接创建索引

  ```
  create index 索引名称 on 表名（字段名）;
  ```

- 删除索引

  ```
  alter table text drop index 索引名称;
  drop index 索引名称 on 表名（字段名）
  ```

- 查询索引

  ```
  show index from 表名\G
  ```

##### 5.4普通索引和唯一索引

- 普通索引

  普通索引是各类索引中最为普通的索引

#### SQL练习

```
select name, ROUND(population/1000000,2)as population,ROUND(gdp/1000000000,2) as gdp from world where continent='South America'
#ROUND函数可以将小数位数保存为设定的位数
```

```
SELECT name, capital
FROM world
where LEFT(name,1)=LEFT(capital,1)AND name<>capital
#LEFT(str,1)把str的第一位
```

```
SELECT name,continent FROM world
WHERE LENGTH(name)=LENGTH(continent)
# LENGTH(str)计算str的字符长度
```

```
SELECT name
   FROM world
WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%' AND name LIKE '%o%' AND name LIKE '%u%' AND name NOT LIKE '% %'
```

