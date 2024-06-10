import requests
from bs4 import BeautifulSoup
import time
from fpdf import FPDF

# Function to execute a URL and get its content
def execute_url(main_url, url):
    combined_url = f"{main_url}{url}"
    response = requests.get(combined_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text_content = soup.get_text(separator='\n')
    return text_content

# Function to save content to a PDF using UTF-8 encoding
def save_to_pdf(contents, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    for content in contents:
        pdf.multi_cell(0, 10, content.encode('latin1', 'replace').decode('latin1'))

    pdf.output(filename)

def main():
    main_url = 'https://r.jina.ai/'
    urls = []

    print("Enter URLs to be executed, one per line. Enter 'done' when finished:")
    while True:
        user_input = input()
        if user_input.lower() == 'done':
            break
        urls.append(user_input)

    contents = []
    for url in urls:
        print(f'Executing URL: {main_url}{url}')
        content = execute_url(main_url, url)
        contents.append(content)
        time.sleep(7)

    save_to_pdf(contents, 'scraped_contents.pdf')
    print('PDF document created: scraped_contents.pdf')

if __name__ == "__main__":
    main()
