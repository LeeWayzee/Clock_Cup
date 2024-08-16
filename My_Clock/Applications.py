

from config.settings import *
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image,ImageDraw
import time
import RPi.GPIO as GPIO
import threading

class SetBase:
    def __init__(self,root,pin_check,pin_change) -> None:
        self.root = root
        self.pin_change = pin_change 
        self.pin_check = pin_check
        
        self.running = True

        self.scanning_thread = threading.Thread(target=self.check_stop_condition)
        #self.scanning_thread = multiprocessing.Process(target=self.check_stop_condition)
        self.scanning_thread.start()

    def check_stop_condition(self):
        while self.running:
            if GPIO.input(self.pin_check) == GPIO.HIGH:
                self.running = False
            time.sleep(0.2)
            
        '''
        except Exception as e:
            print(e)
            self.root.init_display()
            self.root.text(text_error,0,0,font_name=font_bin5x8,color=255)
            self.root.show()
            time.sleep(3)
            self.root.poweroff()
        '''

        
#定义设置时钟的类
class SetClock(SetBase):
    def __init__(self, root, pin_check, pin_change) -> None:
        super().__init__(root, pin_check, pin_change)
        self.clock_thread = None

    def run_clock(self):
        if self.clock_thread is None or not self.clock_thread.is_alive():
            self.clock_thread = threading.Thread(target=self.update_clock)
            self.clock_thread.start()

    def stop_clock(self):
        self.running = False
        if self.clock_thread is not None:
            self.clock_thread.join()
        self.running = True  # Reset running flag for future use

    def update_clock(self):
        while self.running:
            image = Image.new("1", (self.root.width, self.root.height))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, self.root.width, self.root.height * 2), outline=0, fill=0)
            text = time.strftime("%A")
            draw.text((0, 0), text, font=font_dejavusans_16, fill=255)
            text = time.strftime("%e %b %Y")
            draw.text((0, 14), text, font=font_dejavusans_16, fill=255)
            text = time.strftime("%X")
            draw.text((0, 36), text, font=font_dejavusans_24, fill=255)
            self.root.image(image)
            self.root.show()
            time.sleep(1)

 
#定义图像展示的类
class SetImage(SetBase):
    def __init__(self, root, pin_check, pin_change):
        super().__init__(root, pin_check, pin_change)

    def show_image(self, image_path):
        image = Image.open(image_path).resize((self.root.width, self.root.height), Image.ANTIALIAS).convert('1')
        self.root.image(image)
        self.root.show()

     

#定义展示字符的类
class SetChar:
    def __init__(self, content_file) -> None:
        self.content_file = content_file
        
        with open(self.content_file, 'r', encoding='utf-8') as f:
            self.text = f.read().split()
        
    def char_reset(self, per_words):
        formatted_text = []
        # 计算需要的行数
        num_rows = (len(self.text) + per_words - 1) // per_words
        for i in range(num_rows):
            # 计算每行的起始和结束索引
            start_index = i * per_words
            end_index = min((i + 1) * per_words, len(self.text))
            # 如果当前行的单词数量超过per_words，则分配到两行
            if end_index - start_index > per_words:
                # 分配到第一行的单词数量
                first_line_words = self.text[start_index:start_index + per_words - 1]
                # 分配到第二行的单词数量，包括剩余的所有单词
                second_line_words = self.text[start_index + per_words - 1:end_index]
                # 将两行添加到结果列表中
                formatted_text.append(' '.join(first_line_words))
                formatted_text.append(' '.join(second_line_words))
            else:
                # 如果当前行的单词数量不超过per_words，直接添加
                formatted_text.append(' '.join(self.text[start_index:end_index]))
        result = '\n'.join(formatted_text)
        return result

if __name__ == '__main__':


    i2c = board.I2C()
    disp = SSD1306_I2C(128,64,i2c)
    width = disp.width
    height = disp.height

    a = SetChar(text_wangjiao)
    new_a = a.char_reset(3)
    disp.text(new_a,0,0,font_name=font_bin5x8,color=255)
    disp.show()

    

    
    
    


