## 个人生活实用工具项目后端
#### 一、项目需求

生活中经常有购买了一些东西，这些东西是有使用期限的，但是购买后放在一些地方就忘记了，然后到期后也没有使用，后面发现了这些东西，就只能扔掉了，十分可惜。所以我们的需求方希望能够有一个应用，可以在购买东西可以记录购买的东西放在什么地方，什么时候到期，快到期的时候能够自动提醒。最好是直接使用小程序，这样就可以不用再安装一个应用。

针对上面的需求，我们整理下功能需求：

| 角色 | 功能                                 | 是否必须 |
| ---- | ------------------------------------ | -------- |
| 用户 | **添加，修改物品信息，查看物品列表** | Y        |
| 用户 | **登录小程序**                       | Y        |
| 系统 | **提示快到期物品**                   | Y        |

#### 二、工程创建

> 注意：项目统一使用 conda 管理

创建工程 herp 和一个应用 erp.
```bash
$ mkdir jenny-app-backend # 创建工程目录
$ cd jenny-app-backend # 进入工程目录

# 创建虚拟环境
$ conda create -n jenny-app-backend python=3.9
# 查看可用的虚拟环境
$ conda env list
# 或者
$ conda info --envs
# 激活虚拟环境
$ conda activate jenny-app-backend
# 安装相关库
$ conda install django -y # 安装 django
$ conda install djangorestframework -y # 安装 drf
$ conda install markdown -y # 安装 markdown 支持
# 查看虚拟环境已经安装包
$ conda list
# 退出虚拟环境
$ conda deactivate
# 导出虚拟环境
$ conda env export > env.yaml
# 创建 django 工程和应用
$ django-admin startproject herp . # 注意最后有一个小点
$ django-admin startapp erp
```

