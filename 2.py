
import matplotlib.pyplot as plt
x1=[1,2,3,4]
y1=[1,4,9,16]
#x2=[1,2,3,4]
y2=[12,9,0,17]
lines = plt.plot(x1, y1, x1, y2)
plt.xlabel("Over")
plt.ylabel("Score runs")
plt.title("Score comparison")
plt.show()

