import threading;
from pdfSpider import PDFSpider;
import sys;

def main():
    params = sys.argv
    if (len(params) > 2):
         PDFSpider(*params[1:])
    else:
        print("Enter Module Name and Folder Directory")
        moduleName = input("Enter Module Name: ")
        path = input("Enter path of Pdfs: ")
        ifBlankDivided = input("Enter if pdfs is empty page divided(0/1): ")
        PDFSpider(moduleName, path, ifBlankDivided)

if __name__ == "__main__":
    main()