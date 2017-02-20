# chrome自动填写插件的实现 #

###作用
本程序可以快速的输入之前收集好的标题,点击一下就可以完成输入.之前是个别人开发用的,上传阿里巴巴的产品标题和关键词用得着.
###代码分为插件和后端
- Titletookit 是插件的服务端  **基于flask**
- AutoInput 是chrome插件的安装文件
- changename.py 是修改文件整体名字的,这样才不会多人重名
- getAlTitle.py 是获取title的

###原理
- 打开百度,点击chrome的插件图标.
- 调用后台的API,API读取一条数据返回,因为之前是给阿里巴巴输入标题和关键字的,所以做了一个json返回
- 目前获取title之后才能使用,而且不能区分title的类型,每次程序只读取`perfume_box_titles.txt`这个文件,不会按照不同的类型去读取不懂的资源.所以每次用完都需要手动修改`perfume_box_titles.txt`这个文件
- 后来升级的版本已经可以获取不同的类型去读取不一样的资源文件了

用法


1. 首先安装 virtualenv  https://virtualenv.pypa.io/en/stable/userguide/
2. 新建一个文件夹 TitleTooltik,进入TitleTooltik
3.  创建 虚拟空间 virtualenv env
4. 运行virtualenv source env/bin/activate
5. 安装必要的包  pip install -r requirements.txt 
6.  - 安装nltk  http://www.nltk.org/install.html
	- Install NLTK: run sudo pip install -U nltk  (我安装了两次才成功,也使用了pip install nltk 这句话安装)
	- Install Numpy (optional): run sudo pip install -U numpy
	- Test installation: run python then type import nltk
	- 不报错就是成功了

7. 下载nltk data
	- import nltk
	- nltk.download()
	- 或者run python -m nltk.downloader all 安装
	- centos 下data在/usr/share/nltk_data  这里

8. 上传Titletookit工程文件到服务器
9. 运行  gunicorn -w 4 -b 0.0.0.0:5586 run:app 启动服务器  

###**注意: 0.0.0.0:5586 需要是0.0.0.0 而不能是 127.0.0.1 ,不然外网不能访问**