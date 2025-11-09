import argparse
import os
import qrcode

# Define the pages for which QR codes should be generated
PAGES = [
    "intro.html",
    "start.html",
    "station1.html",
    "station2.html",
    "station3.html",
    "station4.html",
    "final.html",
]

def generate_qr_codes(prefix):
    """
    Generates QR codes for the scavenger hunt pages.
    """
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")

    for page in PAGES:
        url = f"{prefix}{page}"
        img = qrcode.make(url)
        filename = os.path.join("qr_codes", f"{os.path.splitext(page)[0]}.png")
        img.save(filename)
        print(f"Generated QR code for {url} and saved as {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR codes for the scavenger hunt.")
    parser.add_argument("--prefix", required=True, help="The URL prefix for the GitHub Pages site.")
    args = parser.parse_args()

    generate_qr_codes(args.prefix)
