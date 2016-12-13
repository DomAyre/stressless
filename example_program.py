import stressless as sl
import turtle
import colorsys


def tuple_to_color(tup):
    col = '#%02x%02x%02x' % tup
    return col

startColour = [25, 255, 128]
endColour = [141, 236, 190]
startToEndVector = [y - x for x, y in zip(startColour, endColour)]
targetFrequency = 1
ball = sl.StressLess()
startFrequency = ball.getFrequency(250)
i = 0

# Direct Pulsing
while True:

    # Get the current frequency
    frequency = ball.getFrequency(250)

    # Get the current colour to pulse
    progress = (frequency - startFrequency) / (targetFrequency - startFrequency) 
    colourModifier = [x * progress for x in startToEndVector]
    currentColour = [x + y for x, y in zip(startColour, colourModifier)]

    # Calculate pulse strength
    directReading = ball.getGripStrength()
    pulseColour = currentColour
    pulseColour[2] *= directReading
    wn.bgcolor(tuple_to_color(colorsys.hsv_to_rgb((pulseColour))))

while True:

    i = (i + 0.01) % 2

    freq = ball.getFrequency(250)
    freq = min(2, freq)

    wn = turtle.Screen()
    wn.bgcolor(tuple_to_color((int(freq * 127), int(127 * (2-freq)), 127)))
    wn.title("Testing in progress")
    if freq < 0.05:
        wn.title("Squeezing too slow")


