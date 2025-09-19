from PIL import Image
import matplotlib.pyplot as plt

# Load the image to inspect what is being rendered
image_path = "/mnt/data/Figure_3_4_GPT_Architecture_Centered.png"
image = Image.open(image_path)

# Display the image for verification
plt.figure(figsize=(8, 12))
plt.imshow(image)
plt.axis('off')
plt.title("Rendered Figure 3.4: GPT Architecture (Centered)")
plt.show()
