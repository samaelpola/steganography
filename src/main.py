import click
from pathlib import Path
from steganography import Steganography


@click.group()
def stegano():
    """CLI program to hide and reveal a secret message in an image."""
    pass


@stegano.command()
@click.argument("path_input_image", type=click.Path(exists=True))
@click.argument("path_output_image", type=click.Path())
@click.argument("secret")
def hide(path_input_image, path_output_image, secret):
    """Hide a secret in a picture."""
    try:
        if not Path(path_output_image).is_dir():
            return click.secho(
                f"ERROR: output directory {path_output_image} does not exist or is not a directory.",
                fg="red",
                bold=True,
            )

        steganography = Steganography()
        output_image = steganography.hide_message(
            path_input_image, path_output_image, secret
        )
        click.secho(
            f"Message successfully hidden in image: {output_image}",
            fg="green",
            bold=True,
        )
    except Exception as e:
        click.secho(f"Error: {e}", err=True, fg="red")


@stegano.command()
@click.argument("image_path", type=click.Path(exists=True))
def reveal(image_path):
    """Reveal the secret hidden in a picture."""
    try:
        steganography = Steganography()
        message = steganography.extract(image_path)
        click.secho(f"Message revealed: {message}", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Error: {e}", err=True, fg="red")


if __name__ == "__main__":
    stegano()
