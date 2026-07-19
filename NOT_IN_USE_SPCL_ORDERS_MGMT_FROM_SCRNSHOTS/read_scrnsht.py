import easyocr

def extract_raw_text(image_path):
    # Initialize the OCR reader for English
    reader = easyocr.Reader(['en'], gpu=False)
    
    print("Extracting raw text from image... Please wait.\n")
    results = reader.readtext(image_path)
    
    # Sort the results from top to bottom of the screen based on their Y-coordinate
    results.sort(key=lambda x: x[0][0][1])
    
    # Print each detected text block on a separate line
    for bbox, text, confidence in results:
        text_clean = text.strip()
        if text_clean:
            print(text_clean)

if __name__ == "__main__":
    # Ensure this matches your exact filename
    image_filename = "media/trd.jpeg" 
    
    extract_raw_text(image_filename)