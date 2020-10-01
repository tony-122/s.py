import turtle
cap=turtle
i=0
j=1
col=['red','white','red','blue','white']
for x in range(100,10,-20):
    cap.begin_fill()
    cap.penup()
    cap.goto(0,20*j)
    j=j+1
    cap.pendown()
    cap.circle(x)
    cap.fillcolor(col[i])
    i=i+1
    cap.end_fill()
cap.mainloop()
