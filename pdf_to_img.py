from pdf2image import convert_from_path

def to_img(poppler, pdf):
    poppler_path = poppler

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf, poppler_path = poppler_path)

    image_paths = []  # Create an empty list to store paths

    for i in range(len(images)):
        # Save pages as images in the pdf
        image_path = 'page' + str(i) + '.jpg'
        images[i].save(image_path, 'JPEG')
        image_paths.append(image_path)  # Append the path to the list
    return image_paths