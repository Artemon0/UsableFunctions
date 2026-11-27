import hashlib
import pickle
import tempfile
import unittest
from importlib.metadata import version
from pathlib import Path

from PIL import Image

from UsableFunctions import UsableFunctions, __version__
from UsableFunctions.UF import UsableFunctions as LegacyUsableFunctions
from UsableFunctions.UF import __version__ as legacy_version


class PackageTests(unittest.TestCase):
    def test_public_imports_and_version(self):
        self.assertIs(UsableFunctions, LegacyUsableFunctions)
        self.assertEqual(__version__, legacy_version)
        self.assertEqual(__version__, version("UsableFunctions"))
        self.assertEqual(UsableFunctions.calculator(5, 7, "+"), 12)
        self.assertEqual(UsableFunctions().factorial(5), 120)

    def test_legacy_circle_pickle_reference(self):
        legacy_circle = b"\x80\x04cUsableFunctions.UF\nUsableFunctions.Circle\n."
        self.assertIs(pickle.loads(legacy_circle), UsableFunctions.Circle)
        self.assertEqual(UsableFunctions.Circle().calculate_N(3, 4), 12)

    def test_file_helpers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.txt"
            self.assertEqual(
                UsableFunctions.create_new_file(path.name, "example", directory),
                "Success",
            )
            self.assertEqual(UsableFunctions.read_file_content(str(path)), "example")
            self.assertEqual(
                UsableFunctions.get_file_hash(str(path)),
                hashlib.sha256(b"example").hexdigest(),
            )
            with (Path(directory) / "data.bin").open("wb") as data:
                data.truncate(1024**2)
            self.assertEqual(UsableFunctions.get_folder_size(directory), "1.0 MB")

    def test_image_converter(self):
        with tempfile.TemporaryDirectory() as directory:
            png = Path(directory) / "example.png"
            jpg = Path(directory) / "example.jpg"
            Image.new("RGB", (2, 2)).save(png)

            UsableFunctions.FileConverter.png_to_jpg(str(png), str(jpg))
            with Image.open(jpg) as image:
                self.assertEqual(image.format, "JPEG")
                self.assertEqual(image.size, (2, 2))
