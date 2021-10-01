from turtle import *
begin_fill()
color('red', 'yellow')
while True:
	forward(500)
	if abs(pos()) < 1:
		continue
end_fill()
done()
