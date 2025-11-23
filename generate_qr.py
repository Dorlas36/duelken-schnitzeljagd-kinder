import argparse
import os
import qrcode

# List of pages for which QR codes should be generated
pages = [
    "intro.html",
    "start.html",
    "station1.html",
    "station2.html",
    "station3.html",
    "station4.html",
    "final.html",
    "results.html"
]

# --- Argument Parser ---
parser = argparse.ArgumentParser(description="Generate QR codes for the scavenger hunt pages.")
parser.add_argument(
    "--prefix",
    required=True,
    help="The URL prefix, e.g., 'https://<user>.github.io/<repo>/'"
)
args = parser.parse_args()

# --- Directory ---
output_dir = "qr_codes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- QR Code Generation ---
for page in pages:
    # 1. Build URL
    url = args.prefix + page

    # 2. Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # 3. Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # 4. Save the image
    filename = os.path.join(output_dir, page.replace(".html", ".png"))
    img.save(filename)

    print(f"Generated QR code for {url} -> {filename}")

print(f"\nSuccessfully generated {len(pages)} QR codes in the '{output_dir}' directory.")
