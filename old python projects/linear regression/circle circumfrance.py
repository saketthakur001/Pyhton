import matplotlib.pyplot as plt

radious = []
area = []
r = 0
for i in range(10):
    radious.append(r)
    area.append(2 * 22/7 * r)
    r += 1

plt.grid(True, linewidth=0.5, color='#ff0000', linestyle='-')
plt.plot(radious, area)
plt.show()