from turtle import *

color('red', 'yellow')
begin_fill()
#turtle.circle(120, 180)  # draw a semicircle
while True:
    forward(455)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
done()