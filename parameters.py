
# resolution: vertical length of each character in pixels.
# Small values means more characters.
# Must be a positive integer.
# Use small values at your own risk.
resolution = 20

# vertical_margin: vertical distance between characters.
# Must be a positive integer.
vertical_margin = 0

# horizontal_margin: horizontal distance between characters.
# Must be a positive integer.
horizontal_margin = 3

# darkness: more values means darker character usage
# must be a float between 1 and 5
darkness = 2.5

# max_brightness: brightness of the brightest color (first characters of pulses) out of 255
# must be an integer between 1 and 255
max_brightness = 200

# min_brightness: brightness of the least brightest color (nonpulse characters) out of 255
# must be an integer between 1 and max_brightness
min_brightness = 100

# light_pulse_period: number of frames a column takes to create a pulse
# must be a positive integer
light_pulse_period = 50

# light_pulse_decay_time: number of frames a pulse takes to decay completely
# must be a positive integer
light_pulse_decay_time = 10

# output_height: height of the output image
# width of the output image is calculated from the input image
# must be a positive integer bigger than resolution
output_height = 720

# font_name: font name.
# possible values are: perfectdark, carbon, antimatrix, matrix, orbitron, ubuntu_bold, ubuntu_regular
# you can also use your own font: put your .ttf file into fonts folder and change the name accordingly
font_name = "perfectdark"