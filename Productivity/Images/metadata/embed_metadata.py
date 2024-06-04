import json
from PIL import Image, PngImagePlugin, JpegImagePlugin
import piexif
import xml.etree.ElementTree as ET

def embed_png(image_path, output_path, metadata):
    img = Image.open(image_path)
    meta = PngImagePlugin.PngInfo()
    for key, value in metadata.items():
        meta.add_text(key, json.dumps(value))
    img.save(output_path, pnginfo=meta)

def embed_jpg(image_path, output_path, metadata):
    img = Image.open(image_path)
    exif_dict = piexif.load(img.info.get('exif', b''))
    for key, value in metadata.items():
        exif_dict['Exif'][piexif.ExifIFD.UserComment] = piexif.helper.UserComment.dump(json.dumps(value))
    exif_bytes = piexif.dump(exif_dict)
    img.save(output_path, "jpeg", exif=exif_bytes)

def embed_webp(image_path, output_path, metadata):
    img = Image.open(image_path)
    img.save(output_path, "WEBP", exif=json.dumps(metadata).encode())

def embed_svg(image_path, output_path, metadata):
    tree = ET.parse(image_path)
    root = tree.getroot()
    metadata_elem = ET.Element('metadata')
    for key, value in metadata.items():
        sub_elem = ET.SubElement(metadata_elem, key)
        sub_elem.text = json.dumps(value)
    root.insert(0, metadata_elem)
    tree.write(output_path)

def embed_metadata(image_path, output_path, metadata, image_format):
    if image_format.lower() == 'png':
        embed_png(image_path, output_path, metadata)
    elif image_format.lower() == 'jpg' or image_format.lower() == 'jpeg':
        embed_jpg(image_path, output_path, metadata)
    elif image_format.lower() == 'webp':
        embed_webp(image_path, output_path, metadata)
    elif image_format.lower() == 'svg':
        embed_svg(image_path, output_path, metadata)
    else:
        raise ValueError("Unsupported image format")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python embed_metadata.py <image_path> <output_path> <metadata_json_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2]
    metadata_json_file = sys.argv[3]

    with open(metadata_json_file, 'r') as f:
        metadata = json.load(f)

    image_format = image_path.split('.')[-1]
    embed_metadata(image_path, output_path, metadata, image_format)
