import zipfile

# Create a zip file containing the GPT architecture figure
zip_path = "/mnt/data/Figure_3_4_GPT_Architecture.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write("/mnt/data/Figure_3_4_GPT_Architecture_Vertical.png", arcname="Figure_3_4_GPT_Architecture_Vertical.png")

zip_path
