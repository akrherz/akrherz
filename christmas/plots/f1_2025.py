"""Venn diagram of time."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, ConnectionPatch, PathPatch, Rectangle
from matplotlib.path import Path


def main():
    # 1. Setup the figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))

    # 2. Define parameters for circles
    R = 1.0  # Radius
    # Distance D must be slightly less than 2*R for a small overlap
    D = 1.95

    center_A = (-D / 2, 0)  # Center of circle A
    center_B = (D / 2, 0)  # Center of circle B

    # 3. Draw the two circles
    circle_A = Circle(
        center_A,
        R,
        facecolor="skyblue",
        edgecolor="blue",
        alpha=0.6,
        label="Set A",
    )
    circle_B = Circle(
        center_B,
        R,
        facecolor="lightcoral",
        edgecolor="red",
        alpha=0.6,
        label="Set B",
    )

    ax.add_patch(circle_A)
    ax.add_patch(circle_B)

    # Add purple overlap region to main diagram
    # Calculate intersection points of the two circles
    y_intersect = np.sqrt(R**2 - (D / 2) ** 2)

    # Create the lens-shaped intersection using two arcs
    theta = np.linspace(
        -np.arcsin(y_intersect / R), np.arcsin(y_intersect / R), 50
    )
    # Right arc (from circle A centered at -D/2)
    arc_A_x = center_A[0] + R * np.cos(theta)
    arc_A_y = R * np.sin(theta)
    # Left arc (from circle B centered at D/2)
    arc_B_x = center_B[0] - R * np.cos(theta[::-1])
    arc_B_y = R * np.sin(theta[::-1])

    # Combine into a closed path
    overlap_x = np.concatenate([arc_A_x, arc_B_x])
    overlap_y = np.concatenate([arc_A_y, arc_B_y])

    # Create path for the overlap
    vertices = np.column_stack([overlap_x, overlap_y])
    codes = (
        [Path.MOVETO] + [Path.LINETO] * (len(vertices) - 2) + [Path.CLOSEPOLY]
    )
    overlap_path = Path(vertices, codes)

    # Add the overlap patch to main plot
    overlap_patch_main = PathPatch(
        overlap_path,
        facecolor="purple",
        edgecolor="darkviolet",
        alpha=0.8,
        linewidth=1,
        zorder=10,
    )
    ax.add_patch(overlap_patch_main)

    # 4. Create the zoomed-in inset axes for the callout
    # [left, bottom, width, height] as a fraction of the figure size
    # Aspect ratio matches highlight rectangle (0.85:1.15)
    inset_height = 0.30
    inset_width = inset_height * (0.85 / 1.15)
    ax_inset = fig.add_axes((0.50, 0.08, inset_width, inset_height))

    # Redraw the circles in the inset (using the original coordinates)
    circle_A_inset = Circle(
        center_A, R, facecolor="skyblue", edgecolor="blue", alpha=0.6
    )
    circle_B_inset = Circle(
        center_B, R, facecolor="lightcoral", edgecolor="red", alpha=0.6
    )

    ax_inset.add_patch(circle_A_inset)
    ax_inset.add_patch(circle_B_inset)

    # Create a colored wedge for the overlap region in the inset
    # Calculate intersection points of the two circles
    # For circles with centers at (-D/2, 0) and (D/2, 0) with radius R
    # The intersection points are at x = 0, y = ±sqrt(R^2 - (D/2)^2)
    y_intersect = np.sqrt(R**2 - (D / 2) ** 2)

    # Create the lens-shaped intersection using two arcs
    theta = np.linspace(
        -np.arcsin(y_intersect / R), np.arcsin(y_intersect / R), 50
    )
    # Right arc (from circle A centered at -D/2)
    arc_A_x = center_A[0] + R * np.cos(theta)
    arc_A_y = R * np.sin(theta)
    # Left arc (from circle B centered at D/2)
    arc_B_x = center_B[0] - R * np.cos(theta[::-1])
    arc_B_y = R * np.sin(theta[::-1])

    # Combine into a closed path
    overlap_x = np.concatenate([arc_A_x, arc_B_x])
    overlap_y = np.concatenate([arc_A_y, arc_B_y])

    # Create path for the overlap
    vertices = np.column_stack([overlap_x, overlap_y])
    codes = (
        [Path.MOVETO] + [Path.LINETO] * (len(vertices) - 2) + [Path.CLOSEPOLY]
    )
    overlap_path = Path(vertices, codes)

    # Add the overlap patch to the inset with a distinct color
    overlap_patch = PathPatch(
        overlap_path,
        facecolor="purple",
        edgecolor="darkviolet",
        alpha=0.8,
        linewidth=2,
        zorder=10,
    )
    ax_inset.add_patch(overlap_patch)

    # Set limits for the inset to zoom in on the overlap (x=0)
    # Match aspect ratio to highlight rectangle
    zoom_width = 0.3 * 0.85
    zoom_height = 0.3 * 1.15
    ax_inset.set_xlim(-zoom_width, zoom_width)
    ax_inset.set_ylim(-zoom_height, zoom_height)
    ax_inset.set_xticks([])
    ax_inset.set_yticks([])
    ax_inset.set_xlabel(
        "The lone 67 seconds on a random October day\n"
        "when both were home together",
        fontsize=14,
        fontweight="bold",
        color="darkviolet",
    )
    # Ensure the box is visible
    ax_inset.spines["top"].set_visible(True)
    ax_inset.spines["right"].set_visible(True)
    ax_inset.spines["bottom"].set_visible(True)
    ax_inset.spines["left"].set_visible(True)

    # 5. Draw a rectangle on the main plot showing the zoomed region
    zoom_width = 0.3 * 0.85  # 15% narrower
    zoom_height = 0.3 * 1.15  # 15% taller
    zoom_rect = Rectangle(
        (-zoom_width, -zoom_height),
        2 * zoom_width,
        2 * zoom_height,
        fill=False,
        edgecolor="black",
        linestyle="--",
        linewidth=1.5,
    )
    ax.add_patch(zoom_rect)

    # 6. Add connection lines from the zoom rectangle to the inset
    # Connect bottom-left corner of zoom rect to bottom-left of inset
    con1 = ConnectionPatch(
        xyA=(-zoom_width, -zoom_height),
        coordsA="data",
        axesA=ax,
        xyB=(0, 0),
        coordsB="axes fraction",
        axesB=ax_inset,
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=25,
    )
    ax.add_artist(con1)

    # Connect bottom-right corner of zoom rect to bottom-right of inset
    con2 = ConnectionPatch(
        xyA=(zoom_width, -zoom_height),
        coordsA="data",
        axesA=ax,
        xyB=(1, 0),
        coordsB="axes fraction",
        axesB=ax_inset,
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=25,
    )
    ax.add_artist(con2)

    # Connect top-left corner of zoom rect to top-left of inset
    con3 = ConnectionPatch(
        xyA=(-zoom_width, zoom_height),
        coordsA="data",
        axesA=ax,
        xyB=(0, 1),
        coordsB="axes fraction",
        axesB=ax_inset,
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=25,
    )
    ax.add_artist(con3)

    # Connect top-right corner of zoom rect to top-right of inset
    con4 = ConnectionPatch(
        xyA=(zoom_width, zoom_height),
        coordsA="data",
        axesA=ax,
        xyB=(1, 1),
        coordsB="axes fraction",
        axesB=ax_inset,
        color="gray",
        linestyle="--",
        linewidth=1,
        zorder=25,
    )
    ax.add_artist(con4)

    # 7. Add annotation boxes for the center of each large circle
    # Position them higher to avoid collision with callout lines
    ax.annotate(
        "Daryl\nhauling 1+ children\naround town",
        xy=(center_A[0], center_A[1] + 0.3),
        xycoords="data",
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.9, ec="blue"),
        fontsize=14,
        horizontalalignment="center",
        verticalalignment="center",
        zorder=20,
    )

    ax.annotate(
        "Liz\nhauling remaining\nchildren around town\nand random others",
        xy=(center_B[0], center_B[1] + 0.3),
        xycoords="data",
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.9, ec="red"),
        fontsize=14,
        horizontalalignment="center",
        verticalalignment="center",
        zorder=20,
    )

    # Set limits and aspect for the main plot
    ax.set_xlim(-R - D / 2 - 0.1, R + D / 2 + 0.1)
    ax.set_ylim(-R - 0.6, R + 0.3)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")  # Hide axes for a cleaner diagram

    ax.set_title(
        "Venn Diagram of Parental Unit Evening Time Allocation", fontsize=16
    )

    plt.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.02)
    plt.savefig("f1_2025.eps")


if __name__ == "__main__":
    main()
