from turtle import *
begin_fill()
color('red', 'yellow')
speed(0)
while True:
	forward(500)
	left(170)
	if abs(pos()) < 1:
		break
end_fill()
hideturtle()
done()
