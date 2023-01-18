def generate_pixelmap(filename: str, maximum_rows: int):
    """
    Creates a pixel map in the spreadsheet from a picture.
    :param filename: Relative or absolute path to the picture.
    :param maximum_rows: The maximum amount of rows in the spreadsheet.
    :return: Creates a "pxmap.csv" file in the current directory.
    """
    pixelmap_file = open('pxmap.csv', 'w')
    from wand.image import Image
    with Image(filename=filename) as image:
        image.transform(resize=f'x{maximum_rows}')
        pixelmap = Image.export_pixels(image, channel_map='I')
        for i in range(len(pixelmap)):
            seperator = '\n' if i % image.width == (image.width - 1) else '\t'
            pixelmap_file.write(f'{pixelmap[i]}{seperator}')
