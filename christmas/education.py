"""Kids progression."""

import matplotlib.pyplot as plt


def main():
    """Go Main Go."""
    r_years = list(range(2020, 2033))
    m_years = list(range(2019, 2032))
    c_years = list(range(2023, 2036))

    (fig, ax) = plt.subplots(1, 1)
    ax.plot(m_years, range(0, 13), ls="--")
    ax.plot(m_years[:3], range(0, 3), lw=3, color="k")
    ax.annotate(
        f"Maggie {m_years[-1]}",
        xy=(m_years[-1], 12),
        xycoords="data",
        xytext=(-50, 30),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=-45,angleB=90,rad=1"
        ),
    )

    ax.plot(r_years, range(0, 13), ls="--")
    ax.plot(r_years[:2], range(0, 2), lw=3, color="k")
    ax.annotate(
        f"Robert {r_years[-1]}",
        xy=(r_years[-1], 12),
        xycoords="data",
        xytext=(10, 15),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=0,angleB=90,rad=1"
        ),
    )
    ax.plot(c_years, range(0, 13), ls="--")
    ax.annotate(
        f"Charlotte {c_years[-1]}",
        xy=(c_years[-1], 12),
        xycoords="data",
        xytext=(-80, -90),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="0.8"),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=45,angleB=90,rad=1"
        ),
    )
    ax.grid(True)
    ax.set_title("Actual + Extrapolated Grade K-12 Completion by Child")
    ax.set_ylabel("Grade")
    ax.set_xlabel("Year of our Lord")
    ax.set_yticks(range(0, 13))
    ax.set_yticklabels(
        ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    )
    ax.set_ylim(-0.1, 15)

    plt.show()
    fig.savefig("plots/education.eps")


if __name__ == "__main__":
    main()
