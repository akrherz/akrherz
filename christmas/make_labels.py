"""Label generation from code, yippee..."""

import pandas as pd
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, KeepInFrame, Paragraph


def coord(x, y, height, unit=1):
    """magic."""
    x, y = x * unit, height - y * unit
    return x, y


def condition_name(val):
    """Make prettier."""
    return (
        val.replace("\n", "")
        .replace("family", "Family")
        .replace("and Family", "<br />&nbsp; &nbsp; &nbsp; &amp; Family")
        .replace(" and ", " + ")
    )


def main():
    """Go Main Go."""
    df = pd.read_excel("/tmp/addresses.xlsx").fillna("")
    """
    df = pd.DataFrame({
        "Name": ["The Herzmann Family"] * 30,
        "Address": ["1506 NE Cornerstone Ct"] * 30,
        "City, State Zip": ["Ankeny, IA 50021"] * 30,
    })
    """
    c = canvas.Canvas("labels.pdf", pagesize=LETTER)
    _width, height = LETTER  # in pixels
    # in inch
    paper_margin_left = 0.19
    paper_margin_top = 0.4
    label_padding_left = 0.125
    label_padding_top = 0
    label_width = 2.625
    label_height = 1
    # Some vertical jitter to account for printer deficiencies
    jitter = 0.015
    style = ParagraphStyle(name="IEM", fontSize=13, leading=16)

    for i, drow in df.iterrows():
        if i > 0 and i % 30 == 0:
            c.showPage()

        col = int((i % 30) / 10)
        row = i % 10
        xpos = paper_margin_left + col * (label_padding_left + label_width)
        ypos = paper_margin_top + row * (
            label_padding_top + label_height + jitter
        )
        frame1 = Frame(
            *coord(xpos + 0.1, ypos + 1, height, inch),
            2.4 * inch,
            0.9 * inch,
            showBoundary=0,
        )
        story = [
            Paragraph(
                f"<i>{condition_name(drow['Name'])}</i><br />"
                f"{drow['Address']}<br />"
                f"{drow['City, State Zip']}",
                style=style,
            )
        ]
        story_inframe = KeepInFrame(2.5 * inch, 1 * inch, story)
        frame1.addFromList([story_inframe], c)
    c.showPage()
    c.save()


if __name__ == "__main__":
    main()
