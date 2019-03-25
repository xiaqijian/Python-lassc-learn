

参数
--

在安装包的时候，用-i，会很快

```

pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple

```

后面的地址可以换成国内的 pip 镜像：

清华
https://pypi.tuna.tsinghua.edu.cn/simple/

中科大
https://pypi.mirrors.ustc.edu.cn/simple/

阿里云
https://mirrors.aliyun.com/pypi/simple/

豆瓣
http://pypi.douban.com/simple/



如果你那儿的网络总是不给力，又不想每次手动添加，可以加在配置文件里一劳永逸。

配置文件
--

### Linux / Mac：

文件地址为 ~/.pip/pip.conf，其余相同。

```
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```