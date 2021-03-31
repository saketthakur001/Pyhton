import matplotlib.pyplot as plt

x = []
y = []
censious = 0
for i in range(50+1):
    x.append(censious)#(32°F − 32) × 5/9 = 0°C
    y.append((censious * 9 / 5) + 32)#(0°C × 9/5) + 32 = 32°F
    censious += 1

plt.plot(x, y)
plt.show()