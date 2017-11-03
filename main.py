import threading;
from pdfSpider import PDFSpider;
import sys;

def main():
    params = sys.argv
    if (len(params) > 2):
        PDFSpider(params[1], params[2])
    else:
        print("Enter Module Name and Folder Directory")
        moduleName = input("Enter Module Name: ")
        path = input("Enter path of Pdfs: ")
        PDFSpider(moduleName, path)

if __name__ == "__main__":
    main()