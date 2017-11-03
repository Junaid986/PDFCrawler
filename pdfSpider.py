import fileHelper as fh
import sys
from PyPDF2 import PdfFileReader, PdfFileMerger

class PDFSpider:

    module_name = ""
    base_path = ""

    def __init__(self, module, base_path):
        sys.setrecursionlimit(100000)
        PDFSpider.module_name = module
        PDFSpider.base_path = base_path
        PDFSpider.boot()

    @staticmethod
    def boot():
        fh.create_project_dir(PDFSpider.module_name)
        merger = PdfFileMerger()
        files = fh.get_pdf_list_from_directory(PDFSpider.base_path)
        for f in files:
            print(f)
            file = open(f, "rb")
            merger.append(PdfFileReader(file))
            file.close()
        with open(PDFSpider.module_name + "/" + PDFSpider.module_name + ".pdf", 'wb') as modDir:
            merger.write(modDir)




