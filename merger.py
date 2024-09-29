import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory, output_filename):
    # Initialize the PdfMerger object
    merger = PdfMerger()

    # Get all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    pdf_files.sort()  # Sort files to merge in alphabetical order

    # Merge each PDF file
    for pdf in pdf_files:
        pdf_path = os.path.join(directory, pdf)
        merger.append(pdf_path)
        print(f"Merging {pdf}...")

    # Write out the merged PDF to the specified output file
    with open(output_filename, 'wb') as output_file:
        merger.write(output_file)

    print(f"All PDFs merged into {output_filename}")

# Usage
directory = ''  # Replace with your directory containing PDFs
output_filename = 'example.pdf'     # Replace with your desired output file name

merge_pdfs(directory, output_filename)
