import machine


#共阴极的引脚对象，可修改
led1 = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(4, machine.Pin.OUT)
led4 = machine.Pin(16, machine.Pin.OUT)

led_list = [led1, led2, led3, led4]

#阳极的引脚对象
c = machine.Pin(13, machine.Pin.OUT)
b = machine.Pin(12, machine.Pin.OUT)
a = machine.Pin(14, machine.Pin.OUT)
h = machine.Pin(32, machine.Pin.OUT)
g = machine.Pin(26, machine.Pin.OUT)
f = machine.Pin(25, machine.Pin.OUT)
e = machine.Pin(33, machine.Pin.OUT)
d = machine.Pin(27, machine.Pin.OUT)

light_list = [a, b, c, d, e, f, g, h]

#0~9对应abcdefgh引脚的电平
num_index = {
    0: "11111100",
    1: "01100000",
    2: "11011010",
    3: "11110010",
    4: "01100110",
    5: "10110110",
    6: "10111110",
    7: "11100000",
    8: "11111110",
    9: "11110110"
    
    }

#此函数用于清屏与全亮
def main(show):
    
    if show == 'open':
        for led in light_list:
            led.value(1)
            
    elif show == 'close':
        for led in light_list:
            led.value(0)

#此函数用于显示1位数字
def light(num):
    main('close')
    
    i = 0
    for bit in num_index.get(num):
        if bit == '1':
            light_list[i].value(1)
            i += 1
            
        else:
            light_list[i].value(0)
            i += 1

#此函数用于显示小数点
def dot(bit_dot):
    led_list[bit_dot-1].value(0)
    h.value(1) 

#此函数用于将阴极电平设为1
def led_light_on():
    for led in led_list:
        led.value(1)

#此函数的参数为要显示的内容，类型为字符串
def show_4bit(number):
    
    n = 0
    for num_show in number:
        led_light_on()
        
        if num_show == '.':
            dot(n)
        
        else:
            main('close')
            
            led_list[n].value(0)
            light(int(num_show))
            
            n += 1
        

#显示
while 1:
    show_4bit('0.721')