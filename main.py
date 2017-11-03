import threading;
from pdfSpider import PDFSpider;
import sys;

if __name__ == "__main__":
    params = sys.argv
    if(len(params) > 2):
        spider = PDFSpider(params[1], params[2])
    else:
        print("Enter Module Name and Folder Directory")