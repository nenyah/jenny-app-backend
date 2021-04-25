## 个人生活实用工具项目后端
#### 一、工程创建
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

