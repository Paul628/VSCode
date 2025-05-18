from PIL import Image
filename = r"C:\Users\paull\Pictures\IMGP5286.png"
im = Image.open(filename)
im.load()
print(im.info)    # Metadata
print(im.size)    # (width, height)
print(im.mode)    # e.g., 'RGB', 'RGBA'
print(im.format)  # e.g., 'PNG'
im.show()  # Display the image

# Resize the image to a lower resolution (e.g., 200x150)
low_res_size = (200, 150)
im_low_res = im.resize(low_res_size, Image.NEAREST)  # NEAREST is a simple mapping
im_low_res.show()  # Display the lower resolution image
im_low_res.save(r"C:\Users\paull\Pictures\IMGP5286_lowres.png")  # Optional: save the result
