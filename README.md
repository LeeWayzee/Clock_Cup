# CLock-Cup 开启软硬件世界的第一步

## ⚓1.简介：
### clock-cup 是用 python语言编写的一个驱动oled-ssd1306显示屏的一个小项目，主要使用树莓派4B进行驱动。它提供了2:1比例的图片功能查看、简要文本阅读功能、时钟功能。

## 💻2.开发环境：
### 硬件： Raspberry 4B
### 软件： python 3.11  |  VSCode  |  Thonny 4.1.4
### 第三方库： RPI、adafruit_circuitpython_ssd1306、PIL、time、threading、multiprocess等

## 📰3.代码解释(简要)
### Applicants.py：
#### class SetBase: 提供了后续功能检测按钮以及滚动，切换按钮的基本属性设置，启用多线程对按钮事件进行检测。
#### class SetChar: 提供了格式化简短文本的输出，继承自SetBase的基本属性。
#### class SetImage: 对于电脑用户使用者，它提供了对图片的显示功能，最佳的展示效果需要图片长宽比接近2:1 ,且图像主体对比度明显
#### class SetClock 提供了时钟展示功能，但是必须要与电脑连接才能保证时间的准确性。
###
### main.py:
#### 程序的主要运行入口文件，对于需要的内容，用户需要手动添加(后续优化)，例如文本展示，图片展示。
###
#### config.setting.py:
#### 基础参数的设置文件，用户可以在里面定义变量以及文件等



