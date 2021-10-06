# python爬虫爬取壁纸

- requests库、lxml库分别用来请求和解析html
- 将请求返回的二进制图像数据用numpy和opencv读取用于筛选图像宽高
- 图片保存可以用 文件读写或opencv保存图片，opencv可以选择图片质量
- 在windows脚本中使用anaconda中的环境，调用python，需要在脚本中activate环境
- 使用python日志
- 使用python的shutil库处理文件和文件夹
- windows bat脚本不显示控制台，后台运行

```bat
@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
```



- 开机启动脚本，将脚本放入以下目录
  - C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
- 开机后还要启动定时任务，每一小时启动一次



参考文献

教程： https://blog.csdn.net/uziwz_/article/details/100575579

requests库：https://www.cnblogs.com/lanyinhao/p/9634742.html

lxml库：https://www.cnblogs.com/zhangxinqi/p/9210211.html

读取resp的图片：https://stackoverflow.com/questions/57539233/how-to-open-an-image-from-an-url-with-opencv-using-requests-from-python

在脚本中使用anaconda环境： https://gist.github.com/maximlt/531419545b039fa33f8845e5bc92edd6

日志：https://www.cnblogs.com/yyds/p/6901864.html

开机启动脚本：https://blog.csdn.net/qq_41699621/article/details/110630446

定时任务：https://blog.csdn.net/David_jiahuan/article/details/98762806

定时任务报错：原因是命令执行的相对路径问题https://blog.csdn.net/u013948858/article/details/84664794