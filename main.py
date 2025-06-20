from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
page_number = 0

## set header
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

    for y in range(20, 292, 8):
        pdf.line(10, y, 200, y)


    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=f"{row['Topic']} - Page {page_number}", align="R")
    page_number += 1

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=f"{row['Topic']} - Page {page_number}", align="R")
        page_number += 1

        for y in range(20, 292, 8):
            pdf.line(10, y, 200, y)
pdf.output("output.pdf")





