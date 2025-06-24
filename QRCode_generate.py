import qrcode
from PIL import Image
from IPython.display import display
import matplotlib.pyplot as plt

# The link to encode
link = "https://byu.box.com/s/e8hqfemmxx9h2auyp27uu2h01o4h1c9m"

# Generate the QR code
qr = qrcode.make(link)

# Save the QR code to a file
qr_path = "byu_box_qr.png"
qr.save(qr_path)
# Display the QR code

display(Image.open(qr_path))  # Display the QR code image

qr.show()  # Display the QR code

# plt.imshow(qr, cmap='gray', interpolation='nearest')
# plt.axis('off')  # Hide the axes
# Display the QR code image
plt.show()  # Show the QR code image
