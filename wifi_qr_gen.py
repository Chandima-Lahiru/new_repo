import qrcode

def generate_wifi_qr():
    """
    Prompts the user for WiFi details and generates a QR code PNG.
    """
    ssid = input("Enter WiFi Name (SSID): ")
    password = input("Enter WiFi Password: ")
    security_type = input("Enter Security Type (WPA/WEP/None) [default: WPA]: ") or "WPA"

    # Standard WiFi QR code format: WIFI:S:<SSID>;T:<TYPE>;P:<PASSWORD>;;
    wifi_config = f"WIFI:S:{ssid};T:{security_type};P:{password};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = "wifi_qrcode.png"
    img.save(filename)
    print(f"\nQR code saved successfully as {filename}")

if __name__ == "__main__":
    generate_wifi_qr()
