from setuptools import setup, find_namespace_packages

setup(
    name="UsableFunctions",
    version="1.4.2",
    description="Very useful functions",
    url="https://github.com/Artemon0/UsableFunctions.git",
    download_url='https://github.com/Artemon0/UsableFunctions/archive/refs/tags/1.4.2.tar.gz',
    author="Artem Onyshchenko",
    author_email="artemon888.com@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["tqdm", "PyInstaller", "pygame"],
    # entry_points={"console_scripts": ["quest = UsableFunctions.UF:quest"]},
)
