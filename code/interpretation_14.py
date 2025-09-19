from PIL import Image
import matplotlib.pyplot as plt

# Load the reference image
image_path = "/mnt/data/Document (12)_0.png"
img = Image.open(image_path)

# Display the image to confirm
plt.figure(figsize=(10, 8))
plt.imshow(img)
plt.axis('off')
plt.title("Reference GPT Architecture Diagram (Current Layout)")
plt.show()
