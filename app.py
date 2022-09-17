# Formatting output into a PDF fle
from fpdf import FPDF
import os

def create_pdf():
    # object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # Fetching txt file
    f = open("team.txt", "r")

    # aligning  positions in PDF
    for x in f:
        pdf.cell(200, 8, txt=x, ln=1, align='L')

    pdf.output("weather6.pdf")
    os.system("weather6.pdf")

