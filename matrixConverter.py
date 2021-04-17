from PIL import Image, ImageFont, ImageDraw
import cv2 as cv
import numpy as np
import random, math
import parameters

alphabet = 'qwiopasdfghjklzxcvbnm,1234567890QWEYUIOPASDFGHJKLZXCVBNM.!$&*(){}[]<>\'"\\|/?@#^%'

def iteratePulse():
    global brightness
    brightness = [[]] + brightness[:-1]
    for i in range(text_x):
        brightness[0].append(max(min_brightness, brightness[1][i]-(max_brightness-min_brightness)//light_pulse_decay_time))
        if random.randint(1, light_pulse_period) == 1:
            brightness[0][i] = max_brightness


def init(frame_width, frame_height):

    global res, darkness, brightness
    global vertical_margin, horizontal_margin
    global max_brightness, min_brightness
    global light_pulse_period, light_pulse_decay_time
    global output_height, output_width
    global font, font_name, font_width, font_height
    global text_x, text_y
    global colors, texts

    res = parameters.resolution
    if type(res) != type(1) or res < 1:
        print("Parameter Error: resolution must be a positive integer.")
        exit(1)

    vertical_margin = parameters.vertical_margin
    if type(vertical_margin) != type(1) or vertical_margin < 0:
        print("Parameter Error: vertical_margin must be a non-negative integer.")
        exit(1)

    horizontal_margin = parameters.horizontal_margin
    if type(horizontal_margin) != type(1) or horizontal_margin < 0:
        print("Parameter Error: horizontal_margin must be a non-negative integer.")
        exit(1)

    darkness = parameters.darkness
    if type(darkness) != type(1) and type(darkness) != type(1.1):
        print("Parameter Error: darkness must be a float.")
        exit(1)
    elif darkness < 1 or darkness > 5:
        print("Parameter Error: darkness must be beween 1 and 5.")
        exit(1)

    max_brightness = parameters.max_brightness
    if type(max_brightness) != type(1) or not (1 <= max_brightness <= 255):
        print("Parameter Error: max_brightness must be an integer between 1 and 255.")
        exit(1)
    
    min_brightness = parameters.min_brightness
    if type(min_brightness) != type(1) or not (1 <= min_brightness <= max_brightness):
        print("Parameter Error: min_brightness must be an integer between 1 and max_brightness.")
        exit(1)
    
    light_pulse_period = parameters.light_pulse_period
    if type(light_pulse_period) != type(1) or light_pulse_period < 1:
        print("Parameter Error: light_pulse_period must be a positive integer.")
        exit(1)
    
    light_pulse_decay_time = parameters.light_pulse_decay_time
    if type(light_pulse_decay_time) != type(1) or light_pulse_decay_time < 1:
        print("Parameter Error: light_pulse_decay_time must be a positive integer.")
        exit(1)
    
    output_height = parameters.output_height
    if type(output_height) != type(1) or output_height < 1:
        print("Parameter Error: output_height must be a positive integer bigger than resolution.")
        exit(1)
    
    font_name = parameters.font_name
    try:    
        font = ImageFont.truetype("fonts/{}.ttf".format(font_name), res)
    except:
        print("Parameter Error: font is not recognized.")
        exit(1)
    
    font_height = res + vertical_margin
    font_width = round(font.getsize("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")[0]/62) + horizontal_margin
    output_width = (output_height*frame_width)//frame_height
    text_x = math.ceil(output_width/font_width)
    text_y = math.ceil(output_height/font_height)


    colors = [(10, ' ')]
    tmpimg = Image.fromarray(np.zeros((int(font_height+1), int(font_width+1)), dtype=np.uint8))
    draw = ImageDraw.Draw(tmpimg)
    for i in range(len(alphabet)):
        draw.rectangle((0, 0, res*2, res*2), 0)
        draw.text((0, 0), alphabet[i], fill=255, font=font, spacing=0)
        light = np.average(np.array(tmpimg))*darkness
        if light != 0:
            colors.append((light, alphabet[i]))

    colors.sort()

    brightness = []
    texts = []
    for i in range(text_y):
        brightness.append([])
        texts.append([])
        for _ in range(text_x):
            brightness[i].append(min_brightness)
            texts[i].append(' ')

    for _ in range(text_y):
        iteratePulse()


def convert(raw):

    little = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)
    little = cv.resize(little, (text_x, text_y))

    for i in range(text_y):
        for j in range(text_x):
            # binary search
            l, r = 0, len(colors)-1
            while l < r:
                m = (l+r)//2
                if colors[m][0] >= little[i][j]:
                    r = m
                else:
                    l = m+1
            texts[i][j] = colors[l][1]

    pilim = Image.fromarray(np.zeros((output_height, output_width, 3), dtype=np.uint8))
    draw = ImageDraw.Draw(pilim)
    for i in range(text_y):
        for j in range(text_x):
            draw.text((j*font_width, i*font_height), texts[i][j], fill=(0,brightness[i][j],0), font=font)
    matrix = np.array(pilim)

    iteratePulse()

    return matrix