from pathlib import Path

from PIL import Image


class Steganography:
    @staticmethod
    def _convert_to_binary(secret: str) -> str:
        message = "".join(format(ord(char), "08b") for char in secret)
        secret_length = format(len(message), "016b")
        return secret_length + message

    @staticmethod
    def _convert_to_string(binary: str) -> str:
        octet_array = [binary[i: i + 8] for i in range(0, len(binary), 8)]
        return "".join(chr(int(octet, 2)) for octet in octet_array)

    def hide_message(self, image_path: str, output_path: str, secret: str):
        img = Image.open(image_path)

        binary_message = self._convert_to_binary(secret)
        message_index = 0
        message_length = len(binary_message)
        modified_pixels = []

        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((j, i))

                if message_index < message_length:
                    r = (r & ~1) | int(binary_message[message_index])
                    message_index += 1

                    if message_index < message_length:
                        g = (g & ~1) | int(binary_message[message_index])
                        message_index += 1

                    if message_index < message_length:
                        b = (b & ~1) | int(binary_message[message_index])
                        message_index += 1

                modified_pixels.append((r, g, b))

        if message_index < message_length:
            raise ValueError(
                "The image doesn't have enough pixels to hide the entire message."
            )

        output_file_path = Path(output_path).joinpath(f"secret-{Path(image_path).stem}.png")
        img.putdata(modified_pixels)
        img.save(output_file_path)
        return output_file_path

    def extract(self, image_path: str) -> str:
        print("Extracting message...")
        img = Image.open(image_path).convert("RGB")

        binary_message = ""
        message_length = None

        for i in range(img.width):
            for j in range(img.height):
                pixel = img.getpixel((j, i))
                for color in pixel:
                    binary_message += str(color & 1)

                    if message_length is None and len(binary_message) == 16:
                        message_length = int(binary_message, 2)
                        binary_message = ""  # reset to stock binary secret

                    if message_length is not None and len(binary_message) == message_length:
                        return self._convert_to_string(binary_message)

        print("No hidden message found or corrupted data.")
