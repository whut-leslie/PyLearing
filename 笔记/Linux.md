# Linux

## #一、操作系统

例如windows

操作系统直接和硬件打交道

计算机硬件：CPU,内存，硬盘,声卡等

**操作系统的作用：管理硬件设备**![image-20200414093044784](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200414093044784.png)

#### 1.2不同领域的主流操作系统

1.桌面操作系统

- Windows系列——用户群体大
- macOS——适用于开发人员

- Linux——应用软件少

2.服务器操作系统（服务器本质上是一个硬件，通过软件远程登录）

- Linux——安全稳定免费，占有率高
- Windows Server——付费，占有率低

3.嵌入式操作系统（智能硬件，智能机器人，智能家居）

- Linux

4.移动设备操作系统

- IOS
- Android（基于Linux，谷歌）

#### 1.3虚拟机

虚拟机（Virtual Machine）指通过软件模拟具有完整硬件系统功能的、运行在一个完全隔离的计算机系统![image-20200416095519413](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416095519413.png)

- 虚拟系统通过生成现有操作系统的全新虚拟镜像，具有真实操作系统完全一样的功能
- 进入虚拟系统后，所有操作都是在这个全新场地独立的虚拟系统里进行，可以独立安装运行软件，保存数据，拥有自己的独立桌面，不会对真正的系统产生任何影响
- 而且能够在现有系统与虚拟镜像之间灵活切换的一类操作系统

## #二、操作系统的发展史（科普）

### 01操作系统的发展历史

#### 1.1操作系统的发展历史

![image-20200416095946362](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416095946362.png)

![image-20200416100251323](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416100251323.png)

![image-20200416100333837](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416100333837.png)

#### 1.2Minix

- 因为政策的改变，Unix源代码私有化
- Andrew S.Tanenbaum（塔能鲍姆）坚守自行开发与Unix兼容的操作系统，以避免版权上的争议
- 以小型Unix(mini-Unix)之意，将他称为Minix

#### 1.3Linux

![image-20200416101043930](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416101043930.png)

### 02.Linux内核及发行版

#### 2.1Linux内核版本(内核只有一个，发信号板有很多种)

- 内核（kernel）是系统的心脏，试运行程序和管理像磁盘和打印机等硬件设备的核心程序，他提供了一个裸设备与应用程序清单间的抽象层![image-20200416184324467](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416184324467.png)
- Linux内核版又分为稳定版和开发版
  - 稳定版：具有专业级强度，可以广泛地应用和部署。新的稳定版相对于较旧的只是修订一些bug或加入一些新的驱动程序
  - 开发版：由于y要试验各种解决方案，所以变化很快

#### 2.2Linux发行版本

- Linux发行版（GUN/Linux发行版）通常包括了桌面环境、办公套件、媒体播放器、数据库等应用软件
- 常见的发行版本如下：
  - Ubantu
  - Redhat
  - Fedora
  - openSUSE
  - Linux Mint
  - Debian
  - Manjaro
  - Mageia
  - CentOS
  - Arch

## #三、文件和目录

### 01.单用户操作系统和多用户操作系统（科普）

- 单用户操作系统：指一台计算机在同一时间只能由一个用户使用，一个用户独享系统的全部硬件和软件资源
  - Windows XP之前的都是单用户系统

- 多用户操作系统：指一台计算机在同一时间可以由多个用户使用，多个用户共享系统的全部硬件和软件资源
  - Unix和Linux的设计初衷就是多用户系统

### 02Windows和Linux文件系统区别

#### 2.1Windows下的文件系统

![image-20200416185831234](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416185831234.png)

#### 2.2Linux下的文件系统

（没有盘符的概念）

![image-20200416190200928](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416190200928.png)

![image-20200416185940851](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416185940851.png)

#### 2.3文件和目录

- /:根目录
- /home:家目录

#### 2.4Linux主要目录

![image-20200416190424430](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416190424430.png)

## #四、Ubantu图形界面

## #常用Linux命令的基本应用

### 01.学习Linux终端命令的原因

![image-20200416190649053](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416190649053.png)

### 02.常用Linux命令的基本使用

| 序号 | 命令          | 对应英文            | 作用                     |
| ---- | ------------- | ------------------- | ------------------------ |
| 01   | ls            | list                | 查看当前文件夹下的内容   |
| 02   | pwd           | print workdirectory | 查看当前所在文件夹       |
| 03   | cd [目录名]   | change directory    | 切换文件夹               |
| 04   | touch[文件名] | touch               | 如果文件不存在，新建文件 |
| 05   | mkdir[目录名] | make directory      | 创建目录                 |
| 06   | rm[文件名]    | remove              | 删除指定的文件名         |
| 07   | clear         | clear               | 清屏                     |

- *ctrl+shift+=*放大窗口的字体显示
- *ctrl+-*缩小窗口的字体显示

ls：![image-20200416194035800](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416194035800.png)

pwd:

![image-20200416194111489](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416194111489.png)

cd空格目录名：

![image-20200416194238986](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416194238986.png)

touch:![image-20200416194404679](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416194404679.png)

mkdir:![image-20200416194448786](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416194448786.png)

rm空格文件名：![image-20200416194659932](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416194659932.png)

rm -r 目录名、文件名：删除目录/文件![image-20200416200318111](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416200318111.png)

clear:在终端中清理屏幕中的命令

### 03.自动补全

- 在敲出“文件/目录/命令”的前几个字母后，按下tab键
  - 如果输入的没有·歧义，

## #五、Linux终端命令格式

### 01.终端命令格式

```
command [-options] [parameter]
```

- command:命令名，相应功能的英文单词或单词的缩写（ls/pwd/clear）
- [-options]：选项，可用来对命令进行控制，也可以省略（rm -r 目录名）
- parameter：传给命令的参数，可以是零个、一个或多个（touch 文件名称/cd 目录名称/mkdir 目录名/rm 文件名

> []代表可选
>
> 命令名，选项，传递给命令的参数之间有空格

### 02.查阅命令帮助信息（知道即可）

![image-20200416200927373](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416200927373.png)

#### 2.1 --help(两个减号)

```
command --help
```

说明:

- 显示command命令的帮助信息![image-20200416201328493](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416201328493.png)

#### 2.2 man

```
man command
```

说明

- 查阅command命令的使用手册

![image-20200416201552532](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416201552532.png)

> man是manual的缩写，是Linux提供的一个手册，，包含了绝大部分的命令、函数的详细使用说明

使用man时的操作键：

![image-20200416201503396](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416201503396.png)

## #六、文件和目录常用命令

![image-20200416202517589](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416202517589.png)

### 01.查看目录内容

#### 1.1终端实用技巧

![image-20200416203053713](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416203053713.png)

#### 1.2 ls命令说明

- ls是英文单词list的简写，其功能为列出目录的内容，使用户最常用的命令之一，类似于DOS下的dir命令

##### Linux下文件和目录的特点

- Linux文件或者目录名称最长可以有256个字符
- 以.开头的文件为隐藏文件，需要用-a参数才能显示
- . 代表当前目录
-  . .代表上一级目录

![image-20200416204644809](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416204644809.png)![image-20200416204840642](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416204840642.png)

#### 1.3 ls常用选项

| 参数 | 含义                                           |
| ---- | ---------------------------------------------- |
| -a   | 显示指定文件下所有的子目录与文件，包括隐藏文件 |
| -l   | 以列表方式显示文件详细信息                     |
| -h   | 配合 -l以人性化的方式显示文件大小              |

ls -l：**前面有d（蓝色字体），文件夹；前面为-（白色字体），文件**；![image-20200416205150836](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416205150836.png)

ls -l -h：比只有-l时，文件信息更容易看清楚

![image-20200416210022515](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416210022515.png)

**拓展：**

可以分开输入，也可以一起输入

ls -l -h：ls -lh

ls -l -h -a：ls -lha（很多以.开头的隐藏文件，用来配置安装的软件，配置内容，不予理会）

##### 计算机中文件大小的表示方式（科普)

![image-20200416213145266](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416213145266.png)

#### 1.4 ls通配符的使用

| 通配符 | 含义                           |      |
| ------ | ------------------------------ | ---- |
| *      | 代表任意个数个字符             |      |
| ？     | 代表任意一个字符，至少一个     |      |
| []     | 表示可以匹配字符租中的任意一个 |      |
| [abc]  | 匹配a、b、c中的任意一个        |      |
| [a-f]  | 匹配a到f范围内的任意一个       |      |

![image-20200416214059893](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416214059893.png)

**拓展**

![image-20200416214359350](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416214359350.png)

### 02.切换目录

#### 2.1cd

- cd石英文单词change directory的简写，其功能为更改当前的工作目录，也是用户最常用的命令之一

  > *注意：Linux所有的目录和文件名都是大小写敏感的*

| 命令  | 含义                                     |
| ----- | ---------------------------------------- |
| cd    | 切换到当前用户的主目录（/home/用户目录） |
| cd ~  | 切换到当前用户的主目录（/home/用户目录） |
| cd  . | 保持在当前目录不变                       |
| cd .. | 切换到上级目录                           |
| cd -  | 可以在最近两次工作目录之间来回切换       |

![image-20200416214838802](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416214838802.png)

![image-20200416215926127](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416215926127.png)

#### 2.2相对路径和绝对路径

- 相对路径在输入路径时，最前面不是/或者~，表示相对当前目录所在的目录位置
- ![image-20200416220850556](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416220850556.png)

- 绝对路径在输入路径时，最前面是/或者~，表示从根目录/家目录开始的具体目录位置

![image-20200416220605367](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200416220605367.png)

### 03.创建和删除操作

#### 3.1 touch

- 创建文件或修改文件时间

  - 如果文件不存在，可以创建一个空白文件
  - 如果文件已经存在，可以修改文件的末次修改日期

  ![image-20200417204528413](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417204528413.png)

#### 3.2 mkdir

- 创建一个新的目录

| 选项 | 含义             |
| ---- | ---------------- |
| -p   | 可以递归创建目录 |

> 新建目录的名称不能与当前目录中已有的目录或文件同名

![image-20200417204800436](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417204800436.png)

#### 3.3 rm

- 删除文件或目录

> 使用rm命令要小心，因为文件删除后不能恢复

| 参数 | 含义                                           |
| ---- | ---------------------------------------------- |
| -p   | 强制删除，忽略不存在的文件，无需提示           |
| -r   | 递归地删除目录下的内容，删除文件夹必须加此参数 |

![image-20200417214310144](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417214310144.png)

### 04.拷贝和移动文件

| 序号 | 命令               | 对应英文 | 作用                                |
| ---- | ------------------ | -------- | ----------------------------------- |
| 01   | tree [目录名]      | tree     | 以树状图列出文件目录结构            |
| 02   | cp 源文件 目标文件 | copy     | 复制文件或者目录                    |
| 03   | mv 源文件 目标文件 | move     | 移动文件或者目录/文件或者目录重命名 |

#### 4.1 tree

- tree 命令可以树状图列出文件目录结构（当前文件夹下的目录结构）

| 选项 | 含义       |
| ---- | ---------- |
| -d   | 只显示目录 |

tree ~：家目录用树形图列出

![image-20200417215622877](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417215622877.png)

#### 4.2 cp

- cp命令的功能是将给出的文件或者目录复制到另一个文件或目录中，相当于Dos下的copy命令

| 选项 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| -f   | 已经存在的目标文件直接覆盖，不会提示                         |
| -i   | 覆盖文件前提示                                               |
| -r   | 若给出的源文件是目录文件，则cp。将递归复制该目录下的所有子目录和文件，目标文件必须是一个目录名 |

cp -i：复制文件

![image-20200417221046206](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417221046206.png)

![image-20200417221404447](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417221404447.png)

![image-20200417221509359](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417221509359.png)

n：不覆盖

y：覆盖

cp -r复制目录

![image-20200417221721840](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417221721840.png)

#### 4.3 mv

- mv命令可以用来移动文件或目录，也可以给文件或目录重命名

| 选项 | 含义           |
| ---- | -------------- |
| -i   | 覆盖文件前提示 |

![image-20200417222401897](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417222401897.png)

![image-20200417222537450](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417222537450.png)

### 05.查看文件内容

| 序号 | 命令                 | 对应英文    | 作用                                                 |
| ---- | -------------------- | ----------- | ---------------------------------------------------- |
| 01   | cat 文件名           | concatenate | 查看文件内容、创建文件、文件合并、追加文件内容等功能 |
| 02   | more 文件名          | more        | 分屏显示文件内容                                     |
| 03   | grep 搜索文本 文件名 | grep        | 搜索文本文件内容                                     |

#### 5.1 cat

- cat 命令可以用来查看文件内容、创建文件、文件合并、追加文件内容等功能
- cat 会一次显示所有的内容，适合查看内容较少的文本文件

| 选项 | 含义               |
| ---- | ------------------ |
| -b   | 対非空输出行编号   |
| -n   | 对输出的所有行编号 |

> Linux中还有一个nl的命令和cat -b的效果等价

![image-20200417223143274](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417223143274.png)

![image-20200417223228880](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417223228880.png)

#### 5.2 more

- more命令可以用于分屏显示文件内容，每次只显示一页内容
- 适合于查看内容较多的文本文件

![image-20200417223938821](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417223938821.png)

#### 5.3 grep

- Linux系统中grep命令是一种强大的**文本搜索**工具
- grep 允许对文本文件进行模式查找，所谓模式查找，又被称为正则表达式

| 选项 | 含义                                     |
| ---- | ---------------------------------------- |
| -n   | 显示匹配行及行号                         |
| -v   | 显示不包含匹配文本的所有行（相当于求反） |
| -i   | 忽略大小写                               |

![image-20200417225525846](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417225525846.png)

- 常用的两种模式查找

| 参数 | 含义                   |
| ---- | ---------------------- |
| ^a   | 行首，搜寻以a开头的行  |
| ke$  | 行尾，搜索以ke结束的行 |

![image-20200417230101552](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417230101552.png)

### 06.其他

#### 6.1 echo文字内容

- echo会在中断中显示参数指定的文字

#### 6.2 重定向>和>>

- Linux允许将命令执行结果 重定向到一个文件

- 将本应该显示在终端上的内容 输出/追加 到指定文件中

其中

- “>”表示输出，会覆盖文件原有的内容
- “>>”表示追加，会将内容追加到已有文件的末尾

![image-20200417231736687](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417231736687.png)

#### 6.3 管道 |

- Linux允许将一个命令的输出可以通过另一个命令的输入

- 可以理解现实生活的管子，管子的一头塞东西进去，另一头取出来，这里的|的左右分为两端，左端塞东西（写），右端取东西（读）

  常用的管道命令有：

- more：分屏显示内容

- grep：在，命令执行结果的基础上查询指定的文本

  ![image-20200417232327507](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417232327507.png)

## #七、远程管理常用命令

![image-20200417232546333](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417232546333.png)

### 01.关机/重启

| 序号 | 命令               | 对应英文 | 作用          |
| ---- | ------------------ | -------- | ------------- |
| 01   | shutdown 选项 时间 | shutdown | 关机/重新启动 |

#### 1.1shutdown

- shutdown 命令可以安全关闭 或者 重新启动系统

| 选项 | 含义     |
| ---- | -------- |
| -r   | 重新启动 |

> - 不指定选项和参数时，默认表示1分钟后关闭电脑
> - 远程维护服务器时，最好不要关闭系统，而应该重启系统

- 常用命令实例

![image-20200417233209243](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200417233209243.png)

### 02.查看或配置网卡信息

| 序号 | 命令        | 对应英文                      | 作用                              |
| ---- | ----------- | ----------------------------- | --------------------------------- |
| 01   | ifconfig    | configure a network interface | 查看/配置计算机当前的网卡配置信息 |
| 02   | ping ip地址 | ping                          | 检测到目标ip地址的连接是否正常    |

#### 2.1网卡和ip地址

##### 网卡

- 网卡是一个专门负责网络通讯的硬件设备
- ip地址是设置在网卡上的地址信息

> 我们可以把电脑比作电话，网卡相当于SIM卡，ip地址相当于电话号码

##### IP地址

- 每台联网的电脑上都有IP地址，是保证电脑之间正常通讯的重要设置

> 注意：每台电脑的IP地址不能相同，否则会出现IP地址冲突，并且没有办法正常通讯

#### 2.2 ifconfig

- ifconfig 可以查看/配置计算机当前的网卡配置信息

![image-20200418000832179](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418000832179.png)

![image-20200418000455937](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418000455937.png)

利用管道，一个命令的结果作为下一个命令的开始，grep文本搜索

![image-20200418000622006](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418000622006.png)

> 提示：一台计算机中可能会有一个屋里网卡和多个虚拟网卡，在Linux中物理网卡的名字通常以ensXX表示

- 127.0.0.1 被称为本地回环/环回地址，一般用来测试本级网卡是否正常

#### 2.3 ping

![image-20200418001218605](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418001218605.png)

- ping 一般用于检测计算机到目标计算及之间的网络是否通常，数值越大，速度越慢

> - ping 的工作原理与潜水艇的声呐相似，ping这个命令就是取自声呐的声音
> - 网络管理员之间也常将ping用作动词——ping 一下计算机X，看他是否开着

原理：网络上到机器都有唯一确定的IP地址，我们给目标IP地址发送一个数据包，对方就要返回一个数据包，根据返回的数据包以及时间，我们可以确定目标主机的存在

> 提示:在Linux中，想要终止一个终端程序的的执行，绝大多数都可以用CTRL+C

![image-20200418002034171](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418002034171.png)

time越小网速越快，Ctrl+c终止ping命令

### 03.远程登录和复制文件

| 序号 | 命令                                             | 对应英文     | 作用          |
| ---- | ------------------------------------------------ | ------------ | ------------- |
| 01   | ssh 用户名@ip                                    | secure shell | 关机/重新启动 |
| 02   | scp 用户名@ip:文件名或路径 用户名@ip文件名或路径 | secure copy  | 远程复制文件  |

#### 3.1 ssh基础（重点）

在Linux中SSH是非常常用的工具，通过SSH客户端 我们可以连接到运行率 SSH服务器的远程机器上

![image-20200418002830272](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418002830272.png)

SSH客户端和SSH服务器都是一个软件，Ubantu，mac都没默认有SSH客户端，只有Windows需安装软件

- SSH客户端是一种使用 Secure Shell（SSH）协议连接到远程计算机的**软件程序**
- SSH是目前较可靠、专为远程登录回话和其他网络服务提供安全性的协议
  - 利用SSH协议，可以有效房防止远程管理过程中的信息泄露
  - 通过SSH协议，可以对所有传输的数据进行加密，也能够防止DNS、欺骗和IP欺骗
- SSH的另一项优点是传输的文件是经过压缩的，所以可以加快传输的速度

##### 1）域名 和 端口号

##### 域名

- 由一串 用点分隔的名字组成，例如www.itcast.cn
- 是ip地址的别名，方便用户记忆

![image-20200418093519509](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418093519509.png)

##### 端口号

- ip地址：通过ip地址找到网络上的计算机

- 端口号：通过端口号可以找到极端及上运行的应用程序
  - SSH服务器的默认端口号是22，如果是默认端口号，在连接的时候，可以省略
- 常见的服务器端口号列表

| 序号 | 服务      | 端口号 |
| ---- | --------- | ------ |
| 01   | SSH服务器 | 22     |
| 02   | Web服务器 | 80     |
| 03   | HTTPS     | 443    |
| 04   | FTP服务器 | 21     |

找到百度而不是谷歌或其他软件，百度服务器安装有web服务器**软件**（专门提供给用户浏览器访问内容）

通过ip地址找到计算机，通过端口号找到计算机上运行的程序

![image-20200418094721637](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418094721637.png)

##### 2）SSH客户端的简单实用

```
ssh [-p port] user@remote
```

- user是在远程服务器上的用户名，如果不指定的话默认为当前用户
- remote是远程机器
- port是SSH Server 监听的端口，如果不指定，就为默认值22，用-p指定为22

> 提示：
>
> - 使用exit退出当前用户的登录
>
> 注意：
>
> - ssh 这个终端这只能在Linux或者Unix系统下使用
> - 如果在Windows系统中，可以安装Putty或者Xshell客户端软件即可
>
> 提示
>
> - 在工作中，SSH服务器的端口号很可能**不是22**，如果遇到这种情况就需要使用-p选项，指定正确的端口号，否则无法正常连接到服务器

![image-20200418095834399](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418095834399.png)

sudo，超用户权限，可以强制关闭服务器

sudo shutdown -r now

#### 3.2 scp(掌握)

- scp就是secure copy、是一个在Linux下用来远程拷贝文件的命令
- 它的地址格式与ssh基本相同，需要注意的是，在指定端口时用的是大写的-P，而不是小写的
- 不要忘记冒号，注意冒号后的路径是以家目录为路径

![image-20200418110003123](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418110003123.png)

| 选项 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| -r   | 若给出的源文件是目录文件，则scp；姜帝圭复制该目录下的所有子目录和文件，目标文件必须为一个目录名 |
| -P   | 若远程SSH服务器的端口不是22，则需要使用大写字母-P选项指定端口 |

> 注意
>
> - scp这个终端命令只能在Linux或者Unix下使用
> - 如果在Windows系统中，可以安装Putty，使用pscp命令行工具或者安装FIleZilla使用FTP进行文件传输
>
> **FileZilla*
>
> FilaZilla在传输文件时，使用的是FTP服务而不是SSH服务，隐刺端口号应该设置为21

#### 3.3 SSH高级（知道）

- 免密码登录
- 配置别名

> 提示：有关SSH配置信息都保存用户家目录下.的ssh目录下(.隐藏文件夹)
>
> 在Ubantu中，隐藏文件是.白色字体，隐藏文件夹是.蓝色字体

ls -lah以人性化列表显示文件包括隐藏文件

##### 1）免密码登录

**步骤**

- 配置公钥

  - 执行ssh-keygen、即可生成SSH要是，一路回车即可

- 上传公钥到服务器

  - 执行ssh-copy-id -p port user@remote，可以让远程服务器记住我们的公钥(remote-远程登录的服务器的IP地址)

  ![image-20200418145058630](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418145058630.png)

**示意图**

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418144602364.png" alt="image-20200418144602364" style="zoom:50%;" />

> 非对称加密算法
>
> - 使用**公钥**加密的数据，需要使用**私钥**解密
> - 使用**私钥**加密的数据，需要使用**公钥**解密

##### 2）配置别名

每次都输入ssh -p port user@remote，对时间久了会觉得麻烦，特别是当user，remote和port都得输入，而且还不好记忆

而**配置别名**可以让我们进一步偷懒，譬如用ssh ma来代替上面这么一长串，那么就在~/.ssh/config里面追加以下内容：![image-20200418150402767](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418150402767.png)

**保存以后，即可ssh mac实现远程登录，scp同样可以使用**

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418151034107.png" alt="image-20200418151034107" style="zoom:67%;" />

## #八、用户权限相关命令

![image-20200418151504864](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418151504864.png)

### 01.用户 和 权限 的 基本概念

#### 1.1基本概念

- 用户是Linux系统工作中重要的一环，用户管理包括**用户**与**组**管理

- 在Linux系统中，不论是由本机或是远程登录系统，每个系统必须拥有一个账号，并且**对于不同的系统资源拥有不同的使用权限**
- 在Linux中，可以指定每一个用户针对不同的文件或者目录的不同权限
- 对文件/目录的权限包括：

| 序号 | 权限   | 英文   | 缩写 | 数字代号 |
| ---- | ------ | ------ | ---- | -------- |
| 1    | 读     | read   | r    | 4        |
| 2    | 写     | write  | w    | 2        |
| 3    | 执行   | excute | x    | 1        |
| 4    | 无权限 |        | -    | 0        |

#### 1.2组

- 为了方便用户管理，提出了 **组**的概念，如下图所示

![image-20200418152822816](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418152822816.png)

- 在实际应用中，可以预先针对组设置好权限，然后将不同的用户添加到对应点组中，从而不用依次为每一个用户设置权限

#### 1.3 ls -l扩展

- ls -l 可以查看文件夹下文件的详细信息，从左到右依次是：

  - **权限**，第一个字符如果是d 表示目录
  - **硬链接数**，通俗地讲，就是有多少种方式，可以访问到当前目录/文件
  - **拥有者**，家目录下 文件/目录 的拥有者通常是当前用户
  - **组**，在Linux 中，很多时候，会出现组名和用户名相同的情况
  - **大小**
  - 时间
  - 名称

  ![image-20200418154037720](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418154037720.png)

![image-20200418154745364](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418154745364.png)

#### 1.4 chmod 简单使用（重要）

- chmod 可以修改 **用户/组** 对**文件/目录**的权限

- 命令格式如下：

  ```
  chmod +/-rwx 文件名|目录名
  ```

> 提示：以上方式会一次性修改 **拥有者/组** 权限，有关 chmod 的高级用法在后面

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418161057388.png" alt="image-20200418161057388" style="zoom:50%;" />![image-20200418161348319](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418161348319.png)

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418161230313.png" alt="image-20200418161230313" style="zoom:50%;" />

![image-20200418164226287](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418164226287.png)

#### 1.5 超级用户

- Linux 系统中的root 账号 通常**用于系统的维护和管理**，对操作系统的所有资源 **具有所有访问权限**
- 在大多数版本的Linux中，都不推荐 **直接使用root账号登录系统**
- 在Linux安装的过程中，系统会自动创建一个用户账号，而这个默认的用户就称为“标准用户”

**sudo**

- su 是subsititude user的缩写，表示**使用另一个用户的身份**
- sudo命令用来以其他身份来执行命令，预设的身份为root
- 用户使用sudo时，必须先输入密码，之后有**5分钟的有效期限**，超过期限必须重新输入密码

> *若其未经授权的用户企图使用sudo，则会发出警告邮件给管理员*

### 02.组管理 终端命令

> 提示：创建组/删除组 的终端命令否组要通过sudo执行

| 序号 | 命令                      | 作用                  |
| ---- | ------------------------- | --------------------- |
| 01   | groupadd 组名             | 添加组                |
| 02   | groupdel 组名             | 删除组                |
| 03   | cat/etc/group             | 确认组信息            |
| 04   | chgrp -R 组名 文件/目录名 | 修改文件/目录的所属组 |

> 提示：
>
> - 组信息保存在/etc/group文件中
>
> - /etc 目录是专门保存**系统配置信息** 的目录

### 03.用户管理 终端命令

> 提示：创建用户/删除用户/修改其他用户密码 的终端命令都需要通过 sudo执行

#### 3.1 创建用户/设置密码/删除用户

| 序号 | 命令                          | 作用           | 说明                                                         |
| ---- | ----------------------------- | -------------- | ------------------------------------------------------------ |
| 01   | useradd -m -g 组新建用户名    | 添加新用户     | -m 自动建立用户家目录；-g指定用户所在的组，否则会建立一个同名的组 |
| 02   | passwd 用户名                 | 设置用户名密码 | 如果是普通用户，直接用passwd，可以修改自己的账户密码         |
| 03   | userdel -r 用户名             | 删除用户       | -r选项会自动删除用户家目录                                   |
| 04   | cat/etc/password\|grep 用户名 | 确认用户信息   | 新建用户后，用户信息会保存/etc/passwd文件中                  |

> 提示：
>
> - 创建用户时，如果忘记添加-m选定指定新用户的家目录——最简单的方法就是**删除用户，重新创建**
> - 创建用户时，默认会创建一个和用户名**同名的**组名**
> - 用户信息保存/etc/passwd文件中

![image-20200418175325358](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418175325358.png)

![image-20200418175727125](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418175727125.png)



#### 3.2 查看用户信息

| 序号 | 命令      | 作用                       |
| ---- | --------- | -------------------------- |
| 01   | id 用户名 | 查看用户UID和GID信息       |
| 02   | who       | 查看当前所有登录的用户列表 |
| 03   | whoami    | 查看当前登录用户的账户名   |

![image-20200418182313502](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418182313502.png)

![image-20200418182905451](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418182905451.png)

**passwd文件**

/etc/passwd 文件存放的是用户的信息，由6个分号组成的7个信息，分别是

1. 用户名
2. 密码（x，表示加密的密码）
3. UID(用户标识)
4. GID（组标识）
5. 用户全名或本地账号
6. 家目录
7. 登录使用的Shell，就是登陆之后，使用的终端命令，Ubantu默认是**dash**

**usermod**

- usermod 可以用来设置用户的主组/附加组和登录Shell，命令格式如下：
- 主组：通常在新建用户时指定，在etc/passwd 的第4列GID对应的组
- 附加组：在etc/group中最后一列表示该组的用户列表，用于指定 用户的附加权限

Shell：用来输入终端命令的软件

> 提示：设置了用户的附加组后，需要重新登录才能生效！

![image-20200418210723063](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418210723063.png)

> 注意：默认使用useradd添加的用户是没有权限使用sudo以root身份执行命令的，可以使用以下命令，将用户添加到sudo附加组

![image-20200418210942957](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418210942957.png)

**which**（重要）

> 提示：
>
> - /etc/passwd 适用于保存用户信息的文件
> - /usr/bin/passwd 是用于修改用户密码的程序

![image-20200418212130198](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418212130198.png)

- which 命令可以查看执行命令所在位置，例如

![image-20200418212534228](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418212534228.png)

**bin和sbin**

- 在Linux中，绝大所数可执行文件都是保存在/bin、/sbin、/usr/sbin
- /bin(binary)是二进制执行文件目录，主要用于具体应用
- /sbin(system binary)是系统管理员专用的二进制代码存放目录，主要用于系统管理
- /usr/bin(usr commands for applications)后期安装的一些软件
- /usr/sbin(super user commands for applications)超级用户的一些管理程序

> 提示：
>
> - cd 这个终端命令是内置在系统内核中，没有独立的文件，因此用which无法找到cd命令的位置

#### 3.3 切换用户

| 序号 | 命令       | 作用                   | 说明                                    |
| ---- | ---------- | ---------------------- | --------------------------------------- |
| 01   | su -用户名 | 切换用户，并且切换目录 | -可以切换到用户家目录，否则保持位置不变 |
| 02   | exit       | 退出当前登录账户       |                                         |

- su不接用户名，可以切换到root，但是不推荐使用，因为不安全
- exit示意图如下

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418214416286.png" alt="image-20200418214416286"  />

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418214640770.png" alt="image-20200418214640770"  />

### 04 修改文件权限

| 序号 | 命令  | 作用       |
| ---- | ----- | ---------- |
| 01   | chown | 修改拥有者 |
| 02   | chgrp | 修改组     |
| 03   | chmod | 修改权限   |

- 命令格式如下

```
#修改文件/目录的拥有者
chown 用户名 文件名/目录名

# 递归修改文件|目录的组
chgrp -R 组名 文件名/目录名

#递归修改文件权限
chmod -R 755 文件名/目录名
```

- chmod在设置权限时，可以简单使用三个数字分别对应 拥有者（7）/组（5）和其他用户的权限（5）

```
#直接修改文件/目录 的读/写/执行 权限，但是不能精确到 拥有者/组 和其他用户的权限
chmod +/-rwx 文件名/目录名
```

![image-20200418220524511](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200418220524511.png)

- 常见数字组合有（u表示用户/g表示组/o表示其他）
  - 777 ===> u=rwx，g=rwx，o=rwx
  - 755 ===> u=rwx，g=rx，o=rx
  - 644 ===> u=rw，g=r，o=r

![image-20200419143823250](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419143823250.png)

## 系统信息相关命令

![image-20200419143933966](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419143933966.png)

### 01.时间和日期

| 序号 | 命令 | 作用                                       |
| ---- | ---- | :----------------------------------------- |
| 01   | date | 查看系统时间                               |
| 02   | cal  | calender查看日历，-y选项可以查看一年的日历 |

cal -y

![image-20200419144202791](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419144202791.png)

### 02.磁盘信息

| 序号 | 命令  | 作用                           |
| ---- | ----- | ------------------------------ |
| 01   | df -h | disk free显示磁盘剩余空间      |
| 02   | du -h | disk usage显示目录下的文件大小 |

- 选项说明

| 参数 | 含义                       |
| ---- | -------------------------- |
| -h   | 以人性化的方式显示文件大小 |

<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419144707705.png" alt="image-20200419144707705" style="zoom:;"   />![image-20200419144742118](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419144742118.png)<img src="C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419144707705.png" alt="image-20200419144707705" style="zoom:;"   />![image-20200419144742118](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419144742118.png)

### 03.进程信息

- 所谓**进程**，通俗地说就是**当前正在执行的一个程序**

| 序号 | 命令               | 作用                                       |
| ---- | ------------------ | ------------------------------------------ |
| 01   | ps aux             | process status查看当前进程的详细状况       |
| 02   | top                | 动态显示运行中的进程并且排序（按q退出top） |
| 03   | kill [-9] 进程代号 | 终止指定代号的进程，-9表示强心终止         |

> **ps默认只会显示当前用户通过终端启动的应用程序**

- ps选项说明功能

| 选项 | 含义                                     |
| ---- | ---------------------------------------- |
| a    | 显示终端上的所有进程，包括其他用户的进程 |
| u    | 显示进程的详细状态                       |
| x    | 显示没有控制终端的进程                   |

> 提示：使用kill命令时，最好只终止有当前用户开启的进程，而不要终止root身份开启的进程，否则可能导致系统的崩溃
>
> - 要退出 top可以直接输入 q

![image-20200419151510185](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419151510185.png)

![image-20200419152113013](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419152113013.png)

## 其他命令

![image-20200419152331585](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419152331585.png)

### 01.查找文件

- find 命令功能非常强大，通常用来在特定的目录下搜索符合条件的文件

| 序号 | 命令                             | 作用                                       |
| ---- | -------------------------------- | ------------------------------------------ |
| 01   | find [路径] -name “搜索条件*.py” | 查找指定路径下扩展名.py 的文件，包括子目录 |

- 如果**省****略路径**，表示**在当前文件夹**下查找
- 之前学习的通配符，在使用 find命令时同时可用
- 有关find的高级使用

**演练**

- 1.搜索桌面目录下，文件名包含 1的文件

```
find -name "*1*"
```

![image-20200419153403250](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419153403250.png)

- 2.搜索桌面目录下所有以.txt为扩展名的文件

```
find -name "*.txt"
```

![image-20200419153535309](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419153535309.png)

- 3.搜索

```
find -name "1*"
```



![image-20200419153604902](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419153604902.png)

### 02.软链接

| 序号 | 命令                          | 作用                                                         |
| ---- | ----------------------------- | ------------------------------------------------------------ |
| 01   | ln -s 被链接的源文件 链接文件 | 建立文件的软链接，用通俗是方式讲**类似于**Windows下的**快捷方式** |

- 注意：
  - 1.没有-s 选项建立的是一个**硬链接文件**
    - 两个文件占用相同的硬盘空间，**工作中几乎不会建立文件的硬链接**
  - 2.**源文件要使用绝对路径**,不能使用相对路径，这样可以方便移动链接文件后，仍然能够正常使用

**演练**

- 1.将桌面目录下的01.py**移动到**demo/b/c目录下

![image-20200419232551861](C:\Users\Leslie\AppData\Roaming\Typora\typora-user-images\image-20200419232551861.png)

- 2.在桌面目录下新建01.py 的**软链接** FirstPython
  - 分别使用 **相对路径**和**绝对路径**建立FirstPython
- 3.将FirstPython  移动到 demo目录下，对比使用**相对路径** 和**绝对路径**的区别

**硬链接简介**

- 在使用ln创建链接时，如果没有-s选项，会创建一个硬链接，而不是软链接