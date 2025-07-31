import pandas as pd
import qrcode
import urllib.parse
import os

# Create folder if it doesn't exist
output_folder = "QR_Codes"
os.makedirs(output_folder, exist_ok=True)

# Load your Excel file
df = pd.read_excel('pumps.xlsx')

# Base URL of your hosted form
base_url = "https://luckydraw-pied.vercel.app/"

for _, row in df.iterrows():
    pump_id = str(row['pumpID']).strip()
    ro_name = str(row['roName']).strip()

    # URL encode parameters
    pump_encoded = urllib.parse.quote(pump_id)
    ro_encoded = urllib.parse.quote(ro_name)

    # Construct URL
    url = f"{base_url}?pump={pump_encoded}&ro={ro_encoded}"

    # Generate QR code
    qr = qrcode.make(url)

    # Save QR code image inside QR_Codes folder
    filename = os.path.join(output_folder, f"QR_{pump_id}_{ro_name}.png")
    qr.save(filename)

    print(f"QR code generated and saved at: {filename}")
