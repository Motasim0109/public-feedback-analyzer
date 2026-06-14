import pdfplumber
import re
import csv
import os

def extract_data(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Join all pages with newlines to preserve paragraph structure
            full_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            
            # Clean the source tags
            clean_text = re.sub(r'\\', '', full_text)
            
            # 1. Improved Extraction Logic
            # We look for 'Address:' but use a version that avoids the Council's header address
            # This regex looks for 'Address:' specifically where it isn't at the very start of the doc
            address_match = re.findall(r"Address:\s*(.*)", clean_text)
            # If there are two addresses, usually the second one (index 1) is the customer
            customer_address = address_match[1].strip() if len(address_match) > 1 else (address_match[0].strip() if address_match else "Not Found")

            # 2. Greedy Comment Extraction
            # We use re.DOTALL and a very specific start anchor
            comment_match = re.search(r"Comment:\s*(.*)", clean_text, re.DOTALL)
            comment_text = comment_match.group(1).strip() if comment_match else "Not Found"

            return {
                "File Name": os.path.basename(pdf_path),
                "Application Number": re.search(r"Application Number:\s*(.*)", clean_text).group(1).strip() if re.search(r"Application Number:\s*(.*)", clean_text) else "Not Found",
                "Address": customer_address,
                "Name": re.search(r"Name:\s*(.*)", clean_text).group(1).strip() if re.search(r"Name:\s*(.*)", clean_text) else "Not Found",
                "Stance": re.search(r"Stance:\s*(.*)", clean_text).group(1).strip() if re.search(r"Stance:\s*(.*)", clean_text) else "Not Found",
                "Comment": comment_text
            }
            
    except Exception as e:
        print(f"Skipping {os.path.basename(pdf_path)}: {e}")
        return None

# Main Execution Block
input_folder = r'C:\Users\mauth\Data Scraping for Vee\documents' 
output_csv = 'final_planning_data1.csv'

if __name__ == "__main__":
    if not os.path.exists(input_folder):
        print(f"Folder '{input_folder}' not found.")
    else:
        pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
        print(f"Processing {len(pdf_files)} files...")

        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ["File Name", "Application Number", "Address", "Name", "Stance", "Comment"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for file in pdf_files:
                data = extract_data(os.path.join(input_folder, file))
                if data:
                    writer.writerow(data)

    print(f"Done. Check {output_csv}")
