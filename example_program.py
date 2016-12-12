import stressless as sl
import turtle


def tuple_to_color(tup):
    col = '#%02x%02x%02x' % tup
    return col

# ball = sl.StressLess()
i = 0
while True:
    i = (i + 0.01) % 2
    try:
        # freq = ball.getFrequency(25)
        freq = min(2, i)
    except:
        continue
    wn=turtle.Screen()
    wn.bgcolor(tuple_to_color((int(freq * 127), int(127 * (2-freq)), 127)))
    wn.title("This is my screen title!")


