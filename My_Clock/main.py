import RPi.GPIO as GPIO
from adafruit_ssd1306 import SSD1306_I2C
from config.settings import *
from board import I2C
from Applications import *
import time,sys

i2c = I2C()

screen = SSD1306_I2C(128,64,i2c)
width = screen.width
height = screen.height
screen.init_display()

# 设置GPIO的编码方式
GPIO.setmode(GPIO.BCM)


# 设置21号引脚为输出，并将其置为高电平
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup([pin_state,pin_switch], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


screen.text('Here is an guidancce',0,0,font_name=font_bin5x8,color=255)
screen.hline(0,10,width,255)
screen.text(intro_init,0,15,font_name=font_bin5x8,color=255)
screen.show()

clock = SetClock(screen,pin_state,pin_switch)

try:
    while True:
        
        if 0 <= index_function <=3:
            
            if GPIO.input(pin_state) == GPIO.HIGH:
                if index_function == 3:
                    clock.stop_clock()  # Stop the clock when switching away
                index_function += 1
                index_function = (index_function - 1) % 3 + 1
                screen.init_display()
                screen.text(f'function:{index_function}',0,0,font_name=font_bin5x8,color=255)
                screen.hline(0,10,width,255)
                screen.text(intro_list[index_function-1],0,15,font_name=font_bin5x8,color=255)
                #screen.text(intro_button_right,0,45,font_name=font_bin5x8,color=255)
                screen.show()
                time.sleep(0.1)
        else:
            index_function = 1
            
        if index_function == 1:
            words_list = [text_intro,text_wangjiao]

            if GPIO.input(pin_switch) == GPIO.HIGH:
                index_text = (index_text + 1) % len(words_list)
                head_text = (words_list[index_text].split('/')[-1]).split('.txt')[0]+':'
                page = str(index_text+1)+'/'+str(len(words_list))

                screen.init_display()
                screen.text(head_text,0,0,font_name=font_bin5x8,color=255)
                screen.text(page,90,0,font_name=font_bin5x8,color=255)
                screen.hline(0,10,width,255)
                words = SetChar(words_list[index_text])
                formatted_words = words.char_reset(3)
                screen.text(formatted_words,0,20,font_name=font_bin5x8,color=255)
                screen.show()
        
        elif index_function == 2:
            image_paths = [image_python_logo,image_kust,image_me,image_wangjiao,image_you_and_me]
            
            if GPIO.input(pin_switch) == GPIO.HIGH:
                
                 # 检查切换按钮是否被按下
                index_images = (index_images +1) % len(image_paths)  # 切换图片索引
                screen.init_display() 
                image_base = SetImage(screen, pin_state, pin_switch)  # 创建SetImage类的实例
                image_base.show_image(image_paths[index_images])  # 显示新的图片
                screen.show()
                
        elif index_function == 3:
            if GPIO.input(pin_switch) == GPIO.HIGH:
                clock.run_clock()
                
                
                
                
            
except KeyboardInterrupt:
    print('end...')

finally:
    # 清理GPIO设置，确保所有引脚被正确地设置为输入模式，并关闭内部上拉/下拉电
    screen.init_display()
    GPIO.cleanup()
    sys.exit()
    