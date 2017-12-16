import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import scipy.stats
import numpy as np

levels = [0, 0.25, 0.5, 0.75, 1]
charlotte = [0]*18 + list(np.random.choice(levels, 36)) + [0]*18 
x = np.arange(0, 72)

(fig, ax) = plt.subplots(1,1)
ax.plot(x, np.ones(72) * 0.8, '-', lw=3, label='Snoopy')
ax.plot(x, np.ones(72) * 0.1, '-.', lw=3, label="Liz & Daryl")
ax.plot(x, charlotte, '-.', lw=3, label="Charlotte")

ax.set_ylabel("Sleep Quality")
ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(['No', 'Nap', 'REM'])
ax.set_ylim(-0.1, 1.1)

ax.set_xticks(range(0, 73, 18))
ax.set_xticklabels(['Noon', '6 PM', 'Mid', '6 AM', 'Noon'])
ax.set_xlim(0, 72)
ax.grid(True)
ax.legend(loc=(0.0, -0.1), ncol=4)

plt.show()
fig.savefig('plots/sleep.eps')
