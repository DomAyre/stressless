import stressless as sl
import turtle
import colorsys

def inRange(range, newValue, threshold):
    del range[-1]
    maxValue = max(range)
    minValue = min(range)
    return newValue-threshold < maxValue and newValue+threshold > minValue

def tuple_to_color(tup):
    col = '#%02x%02x%02x' % tup
    return col

startColour = [25, 255, 128]
endColour = [141, 236, 190]
startToEndVector = [y - x for x, y in zip(startColour, endColour)]
targetFrequency = 1
ball = sl.StressLess()
startFrequency = ball.getFrequency(250)
frequency += startFrequency
i = 0

# Direct Pulsing
while True :

    # Get the current frequency
    frequency += ball.getFrequency(250)

    # Get the current colour to pulse
    progress = (frequency[-1] - startFrequency) / (targetFrequency - startFrequency) 
    colourModifier = [x * progress for x in startToEndVector]
    currentColour = [x + y for x, y in zip(startColour, colourModifier)]

    # Calculate pulse strength
    directReading = ball.getGripStrength()
    pulseColour = currentColour
    pulseColour[2] *= directReading
    wn.bgcolor(tuple_to_color(colorsys.hsv_to_rgb((pulseColour))))


