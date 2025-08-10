import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ====== Image size ======
w, h = 800, 800  # width x height

# ====== Coordinate grid ======
x = np.linspace(0, 4 * np.pi, w)
y = np.linspace(0, 4 * np.pi, h)
X, Y = np.meshgrid(x, y)

# ====== Pattern layers ======
layer1 = np.sin(X * 3.0 + 0.5 * Y)            # wavy pattern
layer2 = np.cos(Y * 2.0 - 0.3 * X)            # crossing waves
r = np.sqrt((X - 2*np.pi)**2 + (Y - 2*np.pi)**2)
radial = np.exp(-0.25 * (r**2))               # radial blob in center
noise = (np.random.RandomState(42).rand(h, w) - 0.5) * 0.3  # stable random noise

# ====== Combine layers ======
combined = layer1 * 0.6 + layer2 * 0.4 + radial * 1.2 + noise
combined = (combined - combined.min()) / (combined.max() - combined.min())  # normalize 0..1

# ====== RGB image creation ======
img = np.zeros((h, w, 3), dtype=np.float32)
img[..., 0] = np.clip(combined + 0.00*np.sin(X*1.2), 0, 1)  # Red channel
img[..., 1] = np.clip(combined + 0.15*np.cos(Y*1.1), 0, 1)  # Green channel
img[..., 2] = np.clip(combined + 0.25*np.sin((X+Y)*0.6), 0, 1)  # Blue channel

# ====== Save image ======
img_uint8 = (img * 255).astype(np.uint8)
Image.fromarray(img_uint8).save("generated_image.png")

# ====== Display image ======
plt.figure(figsize=(6,6))
plt.axis('off')
plt.imshow(img_uint8)
plt.show()
