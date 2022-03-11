def generate_pixelmap(filename: str, height_of_pixelmap: int):
    pixelmap_file = open('pxmap.csv', 'w')
    from wand.image import Image
    with Image(filename=filename) as image:
        image.transform(resize=f'x{height_of_pixelmap}')
        pixelmap = Image.export_pixels(image, channel_map='I')
        for i in range(len(pixelmap)):
            seperator = '\n' if i % image.width == (image.width - 1) else '\t'
            pixelmap_file.write(f'{pixelmap[i]}{seperator}')
