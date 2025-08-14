import re

def extract_weblinks(text):
    # Regex to match http, https, and www links
    pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    links = re.findall(pattern, text)
    return links

if __name__ == "__main__":
    print("Enter the block of text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = "\n".join(lines)
    weblinks = extract_weblinks(text)
    print("Extracted weblinks:")
    for link in weblinks:
        print(link)
