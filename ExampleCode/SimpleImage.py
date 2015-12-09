import numpy as np
from PIL import Image

temp_image = Image.open("image-1.png")
image_array = np.asarray(temp_image)

#image_array is read-only so make a copy
# This also acts as a buffer for swapping pixel layers
array_copy = np.copy(image_array)

#Replace Red layer with Green layer
array_copy[:,:,0] = image_array[:,:,1]

#Replace Green layer with Blue layer
array_copy[:,:,1] = image_array[:,:,2]

#Replace Blue layer with Red layer
array_copy[:,:,2] = image_array[:,:,0]

output_image = Image.fromarray(np.uint8(array_copy)) #convert back to PIL Image
output_image.save("processed_image-1.png")