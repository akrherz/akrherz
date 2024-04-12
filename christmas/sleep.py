import matplotlib.pyplot as plt
import numpy as np

levels = [0, 0.25, 0.5, 0.75, 1]
charlotte = np.array([0] * 24 + list(np.random.choice(levels, 30)) + [0] * 18)
charlotte[3:8] = 0.5
roro = np.array([0] * 24 + list(np.random.choice(levels, 30)) + [0] * 18)
roro[9:14] = 0.5
maggie = np.array([0] * 24 + list(np.random.choice(levels, 30)) + [0] * 18)
maggie[11:16] = 0.5
x = np.arange(0, 72)

(fig, ax) = plt.subplots(1, 1)
ax.set_position([0.1, 0.1, 0.85, 0.8])
ax.plot(x, np.ones(72) * 0.8, lw=3, label="Snoopy")
ax.plot(x, np.ones(72) * 0.1, lw=3, label="Liz & Daryl")
ax.plot(x, charlotte, "-.", lw=3, label="Charlotte")
ax.plot(x, roro, ":", lw=3, label="Robert")
ax.plot(x, maggie, "--", lw=3, label="Maggie")

ax.set_ylabel("Sleep Quality")
ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(["No", "Nap", "REM"])
ax.set_ylim(-0.02, 1.02)

ax.set_xticks(range(0, 73, 18))
ax.set_xticklabels(["Noon", "6 PM", "Mid", "6 AM", "Noon"])
ax.set_xlim(0, 72)
ax.grid(True)
ax.set_title("2017 Herzmann Family Sleep Quality")
ax.legend(loc=(0.81, 0.2), ncol=1)

plt.show()
fig.savefig("plots/sleep.eps")
