import fileHelper as fh
import sys
from PyPDF2 import PdfFileReader, PdfFileMerger

class PDFSpider:

    module_name = ""
    base_path = ""
    is_blank_page_divided = False
    blank_path = "blank.pdf"
    emptyPdf = None

    def __init__(self, module, base_path, is_blank_page_divided = '0'):
        sys.setrecursionlimit(100000)
        PDFSpider.module_name = module
        PDFSpider.base_path = base_path
        if is_blank_page_divided:
            if is_blank_page_divided == '1':
                PDFSpider.is_blank_page_divided = True
            elif is_blank_page_divided == '0':
                PDFSpider.is_blank_page_divided = False
        PDFSpider.boot()

    @staticmethod
    def boot():
        fh.create_project_dir(PDFSpider.module_name)
        merger = PdfFileMerger()
        files = fh.get_pdf_list_from_directory(PDFSpider.base_path)
        if(PDFSpider.is_blank_page_divided):
            # with open(PDFSpider.blank_path, "rb") as f:
            PDFSpider.emptyPdf = PdfFileReader(open(PDFSpider.blank_path, "rb"))
        for f in files:
            print(f)
            file = open(f, "rb")
            merger.append(PdfFileReader(file))
            if (PDFSpider.is_blank_page_divided):
                merger.append(PDFSpider.emptyPdf)
            file.close()
        with open(PDFSpider.module_name + "/" + PDFSpider.module_name + ".pdf", 'wb') as modDir:
            merger.write(modDir)




