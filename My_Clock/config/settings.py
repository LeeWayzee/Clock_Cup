import board
from PIL import ImageFont

#设置索引值
index_function = 0
index_images = 0
index_text = 0

running = True

#设置功能简介
intro_list = ['words','images','clock',
              'developing...\n\nIt is not available\nat present!']
intro_init = 'Here is menu\n\n'\
             'function1:show words\n'\
             'fucntion2:show images\n'\
             'function3:show clock\n' \
             'function4:developing...'  
intro_char = 'This function is for\n\ndisplaying words.'
intro_image = 'This function is for\n\ndisplaying images.'
intro_clock = 'This function is for\n\ndisplaying clock.'
intro_button_right = 'Please press the right\nbutton to run'
intro_button_left = 'Please press the left\nbutton to switch'
text_error = 'This is an\n\nerror occured!\n\nplease try again!'

#设置管脚
pin_state = 5
pin_switch = 6
pin_high_signal = 21

#定义IIC
i2c = board.I2C()

#设置字体
font_default =  ImageFont.load_default()
font_dejavusans_16 = ImageFont.truetype('font_lib/DejaVuSans.ttf',12)
font_dejavusans_24 = ImageFont.truetype('font_lib/DejaVuSans.ttf',24)
font_bin5x8 = 'font_lib/font5x8.bin'

#设置图片路径
image_kust = 'photos/KUST.jpeg'
image_me = 'photos/Me.jpeg'
image_python_logo = 'photos/PythonLogo.jpeg'

#设置文本路径
text_intro = 'content/Intro.txt'

if __name__ == '__main__':
    print(font_default)
