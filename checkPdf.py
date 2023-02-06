import os
import pdfplumber

file_path = 'E:/Book/Journals/SIAM Journal on Optimization'
for path, subdirs, files in os.walk(file_path):    
    for file in files:
        print(file)
        if file.endswith(".pdf"):
            filepath = os.path.join(path, file)
            bDelete = False
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    strtext = page.extract_text().lower()
                    if "korea" in strtext:
                        bDelete = True
                        break
            if bDelete:
                os.remove(filepath)
                print("Removed =====   ", file)