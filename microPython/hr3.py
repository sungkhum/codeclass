from machine import Pin, Signal, I2C, ADC, Timer
import ssd1306
import time

adc = ADC(0)

i2c = I2C(scl = Pin(2), sda = Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

MAX_HISTORY = 200
TOTAL_BEATS = 30

HEART = [
[ 0, 0, 0, 0, 0, 0, 0, 0, 0],
[ 0, 1, 1, 0, 0, 0, 1, 1, 0],
[ 1, 1, 1, 1, 0, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1, 1],
[ 1, 1, 1, 1, 1, 1, 1, 1, 1],
[ 0, 1, 1, 1, 1, 1, 1, 1, 0],
[ 0, 0, 1, 1, 1, 1, 1, 0, 0],
[ 0, 0, 0, 1, 1, 1, 0, 0, 0],
[ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

def calculate_bpm(beats):
    # Truncate beats queue to max, then calculate bpm.
    # Calculate difference in time from the head to the 
    # tail of the list. Divide the number of beats by 
    # this duration (in seconds)
    beats = beats[-TOTAL_BEATS:]
    beat_time = beats[-1] - beats[0]
    if beat_time:
        bpm = (len(beats) / (beat_time)) * 60
        oled.text("%d bpm" % bpm, 12, 0)

def detect():
    # Maintain a log of previous values to 
    # determine min, max and threshold.
    history = []
    beats = []
    beat = False
    bpm = None

    # Clear screen to start.
    oled.fill(0)

    while True:
        v = adc.read()
        history.append(v)

        # Get the tail, up to MAX_HISTORY length
        history = history[-MAX_HISTORY:]

        minima, maxima = min(history), max(history)

        threshold_on = (minima + maxima * 3) // 4   # 3/4
        threshold_off = (minima + maxima) // 2      # 1/2

        if v > threshold_on and beat == False:
            beat = True
            beats.append(time.time())
            # Truncate beats queue to max
            beats = beats[-TOTAL_BEATS:]
            bpm = calculate_bpm(beats)

        if v < threshold_off and beat == True:
            beat = False

        refresh(bpm, beat, v, minima, maxima)

last_y = 0

def refresh(bpm, beat, v, minima, maxima):
    global last_y

    oled.vline(0, 0, 32, 0)
    oled.scroll(-1,0) # Scroll left 1 pixel

    if maxima-minima > 0:
        # Draw beat line.
        y = 32 - int(16 * (v-minima) / (maxima-minima))
        oled.line(125, last_y, 126, y, 1)
        last_y = y

    # Clear top text area.
    oled.fill_rect(0,0,128,16,0) # Clear the top text area

    if bpm:
        oled.text("%d bpm" % bpm, 12, 0)

    # Draw heart if beating.
    if beat:
        for y, row in enumerate(HEART):
            for x, c in enumerate(row):
                oled.pixel(x, y, c)

    oled.show()

def calculate_bpm(beats):
    if beats:
        beat_time = beats[-1] - beats[0]
        if beat_time:
            return (len(beats) / (beat_time)) * 60