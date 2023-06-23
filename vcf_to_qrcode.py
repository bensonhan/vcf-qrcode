import qrcode
import os

for item in os.listdir('contacts'):
    # Read the VCF contact file
    with open('contacts/' + item, 'r') as vcf_file:
        vcf_data = vcf_file.read()

    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    qr.add_data(vcf_data)
    qr.make(fit=True)

    # Save the QR code as an image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(item.rstrip(".vcf") + ".png")