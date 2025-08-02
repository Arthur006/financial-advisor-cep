import zlib
import requests
import argparse
from pathlib import Path

def deflate_and_encode(plantuml_text):
    compressed = zlib.compress(plantuml_text.encode('utf-8'))
    compressed = compressed[2:-4]
    return encode_base64(compressed)

def encode_base64(data):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    result = ''
    buffer = 0
    bits_left = 0
    for byte in data:
        buffer = (buffer << 8) | byte
        bits_left += 8
        while bits_left >= 6:
            bits_left -= 6
            result += alphabet[(buffer >> bits_left) & 0x3F]
    if bits_left > 0:
        result += alphabet[(buffer << (6 - bits_left)) & 0x3F]
    return result


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Convert PlantUML to SVG via docker server")
    parser.add_argument("input_file", help="Path to .puml file")
    parser.add_argument("--output", "-o", default="diagram.svg", help="Output SVG file name")
    parser.add_argument("--server", "-s", default="http://plantuml:8080/svg/")

    args = parser.parse_args()

    input_path = Path(args.input_file)

    if not input_path.exists():
        print(f"Error: File '{input_path}' not found")

    output_path = Path(args.output)

    if not output_path.exists():
        print("Creating output file")
        output_path.touch()

    base_url = args.server

    with input_path.open() as f:
        content = f.read()
        encoded = deflate_and_encode(content)
       
        url = f"{base_url}{encoded}"
        print("Getting: ", url)

        resp = requests.get(url)

        content = resp.content

    with output_path.open("w") as o:
        o.write(content.decode())

    print(f"Done! Wrote image to: {output_path}")

