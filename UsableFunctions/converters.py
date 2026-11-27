"""Image and document conversion with a Tkinter launcher."""

import os


class FileConverter:
    """Helper class for file conversion operations."""

    @staticmethod
    def png_to_jpg(png_file: str, jpg_file: str) -> str:
        """Convert PNG image to JPG format."""
        from PIL import Image

        try:
            with Image.open(png_file) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(jpg_file, "JPEG")
                return "Success"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def jpg_to_png(jpg_file: str, png_file: str) -> str:
        """Convert JPG image to PNG format."""
        from PIL import Image

        try:
            with Image.open(jpg_file) as img:
                img.save(png_file, "PNG")
                return "Success"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def txt_to_pdf(txt_file: str, pdf_file: str) -> str:
        """Convert TXT file to PDF format."""
        from fpdf import FPDF

        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            with open(txt_file, "r", encoding="utf-8") as file:
                for line in file:
                    pdf.cell(
                        0,
                        10,
                        txt=line.encode("latin-1", "replace").decode("latin-1"),
                        ln=True,
                    )
            pdf.output(pdf_file)
            return "Success"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def pdf_to_txt(pdf_file: str, txt_file: str) -> str:
        """Convert PDF file to TXT format."""
        from PyPDF2 import PdfReader

        try:
            reader = PdfReader(pdf_file)
            with open(txt_file, "w", encoding="utf-8") as file:
                for page in reader.pages:
                    file.write(page.extract_text() + "\n")
            return "Success"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def jpgs_to_pdf(*jpg_files, pdf_file: str) -> str:
        """Convert multiple JPG images to a single PDF file."""
        from PIL import Image

        try:
            if not jpg_files:
                return "Error: No files provided"

            if len(jpg_files) == 1 and "\n" in jpg_files[0]:
                actual_files = jpg_files[0].split("\n")
            else:
                actual_files = jpg_files

            image_list = [Image.open(img).convert("RGB") for img in actual_files]

            if image_list:

                image_list[0].save(
                    pdf_file, save_all=True, append_images=image_list[1:]
                )
                return "Success"
            return "Error: No files provided"
        except Exception as e:
            return f"Error: {e}"

    class gui:
        """GUI for all File Converter operations."""

        @staticmethod
        def converter(mode="png_to_jpg"):
            """Universal GUI Launcher for Converters."""
            import tkinter as tk
            from tkinter import Toplevel, filedialog, messagebox

            configs = {
                "png_to_jpg": {
                    "title": "PNG to JPG",
                    "ext": ".png",
                    "out": ".jpg",
                    "f": FileConverter.png_to_jpg,
                },
                "jpg_to_png": {
                    "title": "JPG to PNG",
                    "ext": ".jpg",
                    "out": ".png",
                    "f": FileConverter.jpg_to_png,
                },
                "txt_to_pdf": {
                    "title": "TXT to PDF",
                    "ext": ".txt",
                    "out": ".pdf",
                    "f": FileConverter.txt_to_pdf,
                },
                "pdf_to_txt": {
                    "title": "PDF to TXT",
                    "ext": ".pdf",
                    "out": ".txt",
                    "f": FileConverter.pdf_to_txt,
                },
                "jpgs_to_pdf": {
                    "title": "JPGs to PDF",
                    "ext": ".jpg",
                    "out": ".pdf",
                    "f": FileConverter.jpgs_to_pdf,
                },
            }

            conf = configs.get(mode)
            # Use Toplevel so it doesn't create a second main application instance
            root = Toplevel()
            root.title(conf["title"])
            root.geometry("450x200")

            path_var = tk.StringVar()

            def browse():
                if mode == "jpgs_to_pdf":
                    fn = filedialog.askopenfilenames(
                        filetypes=[(f"{conf['title']} files", f"*{conf['ext']}")]
                    )
                    if fn:
                        path_var.set("\n".join(fn))
                else:
                    fn = filedialog.askopenfilename(
                        filetypes=[(f"{conf['title']} files", f"*{conf['ext']}")]
                    )
                    if fn:
                        path_var.set(fn)

            def run():
                inp = path_var.get()
                if not inp:
                    messagebox.showwarning(
                        "Warning", "Please select an input file."
                    )
                    return

                # Determine the output path based on the first selected file
                first_file = inp.split("\n")[0]
                out = os.path.splitext(first_file)[0] + conf["out"]

                try:
                    # Logic for multiple JPGs to one PDF
                    if mode == "jpgs_to_pdf":
                        files_list = inp.split("\n")
                        # Pass list as *args and out as a keyword argument
                        res = conf["f"](*files_list, pdf_file=out)
                    else:
                        # Standard conversion for single files
                        res = conf["f"](inp, out)

                    if res == "Success":
                        messagebox.showinfo("Done", f"Saved to: {out}")
                    else:
                        messagebox.showerror("Error:", res)
                except Exception as e:
                    messagebox.showerror("Exception", str(e))

            tk.Label(root, text=conf["title"], font=("Arial", 12, "bold")).pack(
                pady=10
            )
            frame = tk.Frame(root)
            frame.pack()
            tk.Entry(frame, textvariable=path_var, width=35).pack(
                side=tk.LEFT, padx=5
            )
            tk.Button(frame, text="Browse", command=browse).pack(side=tk.LEFT)
            tk.Button(
                root, text="Convert Now", bg="green", fg="white", command=run
            ).pack(pady=20)

        # Methods to call the GUI
        @staticmethod
        def png_to_jpg():
            FileConverter.gui.converter("png_to_jpg")

        @staticmethod
        def jpg_to_png():
            FileConverter.gui.converter("jpg_to_png")

        @staticmethod
        def txt_to_pdf():
            FileConverter.gui.converter("txt_to_pdf")

        @staticmethod
        def pdf_to_txt():
            FileConverter.gui.converter("pdf_to_txt")

        @staticmethod
        def jpgs_to_pdf():
            FileConverter.gui.converter("jpgs_to_pdf")

        @staticmethod
        def gui():
            """Launches the universal GUI launcher."""
            import tkinter as tk

            root = tk.Tk()
            root.title("File Converter")
            root.geometry("450x200")
            root.resizable(False, False)
            tk.Label(
                root, text="Select Operation:", font=("Arial", 12, "bold")
            ).pack(pady=10)
            frame = tk.Frame(root)
            frame.pack()
            tk.Button(
                frame,
                text="PNG to JPG",
                command=lambda: FileConverter.gui.converter(
                    "png_to_jpg"
                ),
                bg="#FFC7CE",
                fg="black",
            ).grid(row=0, column=0, padx=5, pady=5)
            tk.Button(
                frame,
                text="JPG to PNG",
                command=lambda: FileConverter.gui.converter(
                    "jpg_to_png"
                ),
                bg="#BFEFFF",
                fg="black",
            ).grid(row=0, column=1, padx=5, pady=5)
            tk.Button(
                frame,
                text="TXT to PDF",
                command=lambda: FileConverter.gui.converter(
                    "txt_to_pdf"
                ),
                bg="#FFFFB3",
                fg="black",
            ).grid(row=1, column=0, padx=5, pady=5)
            tk.Button(
                frame,
                text="PDF to TXT",
                command=lambda: FileConverter.gui.converter(
                    "pdf_to_txt"
                ),
                bg="#D3F0E8",
                fg="black",
            ).grid(row=1, column=1, padx=5, pady=5)
            tk.Button(
                frame,
                text="JPGs to PDF",
                command=lambda: FileConverter.gui.converter(
                    "jpgs_to_pdf"
                ),
                bg="#F0E8F0",
                fg="black",
            ).grid(row=2, column=0, padx=5, pady=5)
            tk.Button(
                frame, text="Quit", command=root.quit, bg="#FFCCCB", fg="black"
            ).grid(row=2, column=1, padx=5, pady=5)
            root.mainloop()
