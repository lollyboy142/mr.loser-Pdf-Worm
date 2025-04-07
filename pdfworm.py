import os
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Function to create a PDF with the text "hello"
def create_text_pdf(output_path, text="hello"):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.drawString(100, 750, text)  # Position the text on the page
    c.save()

# Iterate through all PDF files in the Downloads folder
for filename in os.listdir(downloads_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(downloads_folder, filename)
        
        # Read the existing PDF
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Copy all pages from the original PDF
        for page in reader.pages:
            writer.add_page(page)
        
        # Create a temporary PDF with the text "hello"
        temp_pdf_path = os.path.join(downloads_folder, "temp_hello.pdf")
        create_text_pdf(temp_pdf_path, text="hello, mr.loser was here 2025")
        
        # Read the temporary PDF and append it to the writer
        temp_reader = PdfReader(temp_pdf_path)
        for page in temp_reader.pages:
            writer.add_page(page)
        
        # Save the modified PDF
        output_path = os.path.join(downloads_folder, f"modified_{filename}")
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        
        # Remove the temporary PDF
        os.remove(temp_pdf_path)

print("Text appended to all PDF files in the Downloads folder!")

from reportlab.pdfgen import canvas
import os

# Path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Path to the output PDF file
output_pdf_path = os.path.join(downloads_folder, "mr_loser_was_here_2025.pdf")

# Create the PDF
c = canvas.Canvas(output_pdf_path)
c.drawString(100, 750, "mr.loser was here 2025")  # Position the text on the page
c.save()

print(f"PDF created at {output_pdf_path}")

# Path to the PDF file you want to open at startup
pdf_file_path = os.path.expanduser("~/Downloads/mr_loser_was_here_2025.pdf")

# Path to the autostart directory
autostart_dir = os.path.expanduser("~/.config/autostart")
os.makedirs(autostart_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Path to the .desktop file
desktop_file_path = os.path.join(autostart_dir, "open_pdf_at_startup.desktop")

# Content of the .desktop file
desktop_file_content = f"""[Desktop Entry]
Type=Application
Exec=xdg-open "{pdf_file_path}"
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Open PDF at Startup
Comment=Opens a specific PDF file at startup
"""

# Write the .desktop file
with open(desktop_file_path, "w") as desktop_file:
    desktop_file.write(desktop_file_content)

print(f"Startup entry created to open {pdf_file_path} at startup.")