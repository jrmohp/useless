import fitz

def get_total_pages(file_path):
    doc = fitz.open(file_path)
    total_pages = doc.page_count
    doc.close()
    return total_pages

def get_page(file_path, page_number):
    doc = fitz.open(file_path)
    page = doc.load_page(page_number)
    return page

def read_sample_pdf_pages(file_path, num_pages):
    doc = fitz.open(file_path)
    text = ''
    for page_num in range(num_pages):
        page = doc.loadPage(page_num)
        text += page.getText()
    doc.close()
    return text



def read_pdf_pages(file_path):
    doc = fitz.open(file_path)
    num_pages = doc.page_count
    text_list = []

    segment_size = 2000
    start_page = 0
    end_page = min(segment_size, num_pages)

    while start_page < num_pages:
        text = ''
        for page_num in range(start_page, end_page):
            page = doc.load_page(page_num)
            text += page.get_text()
        text_list.append(text)

        start_page = end_page
        end_page = min(end_page + segment_size, num_pages)

    doc.close()
    return text_list


