"""Christmas 2023 figure 2."""
import calendar

import matplotlib.pyplot as plt
import numpy as np

# Enable XKCD mode
with plt.xkcd():
    # Data
    (fig, ax) = plt.subplots()
    net_worth = np.ones(12) * 0.1

    # Create XKCD-style bar chart
    ax.bar(range(1, 13), net_worth, bottom=np.ones(12) * -0.1, color='skyblue')
    for i in range(1, 13):
        ax.text(i, 0.05, '0', ha='center', va='center')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(calendar.month_abbr[1:], rotation=45)
    ax.set_title('Marathons Run by Daryl during 2023')
    ax.set_xlabel('Month')
    ax.set_ylabel('Marathons Run')
    ax.set_ylim(-0.1, 1.0)
    # Remove top and right spline
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Save the figure
    fig.savefig('f2_2023.eps')
    fig.savefig('f2_2023.png')
