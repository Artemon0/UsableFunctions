from tqdm import tqdm
from subprocess import Popen, PIPE
import sys


def update_package():
    """
    Updates the UsableFunctions package from GitHub using pip.
    Shows progress with a tqdm progress bar.

    Returns:
        dict: A dictionary containing:
            - 'success' (bool): Whether the update was successful
            - 'message' (str): Status message or error details
    """
    stages = {
        "Cloning": 20,
        "Installing dependencies": 30,
        "Installing package": 40,
        "Finalizing": 10,
    }

    with tqdm(total=100, desc="Updating package", ncols=60) as pbar:
        try:
            process = Popen(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    "git+https://github.com/Artemon0/UsableFunctions.git",
                ],
                stdout=PIPE,
                stderr=PIPE,
                text=True,
            )

            current_stage = None
            progress = 0
            error_output = []

            while True:
                output = process.stdout.readline()
                error = process.stderr.readline()

                if error:
                    error_output.append(error.strip())

                if output == "" and error == "" and process.poll() is not None:
                    break

                if output:
                    output = output.strip()
                    # Определяем текущий этап
                    if "Cloning" in output and current_stage != "Cloning":
                        current_stage = "Cloning"
                        pbar.set_description(f"Updating package: {current_stage}")
                        pbar.update(stages[current_stage])
                        progress += stages[current_stage]
                    elif (
                        "Installing build dependencies" in output
                        and current_stage != "Installing dependencies"
                    ):
                        current_stage = "Installing dependencies"
                        pbar.set_description(f"Updating package: {current_stage}")
                        pbar.update(stages[current_stage])
                        progress += stages[current_stage]
                    elif (
                        "Installing" in output
                        and "dependencies" not in output
                        and current_stage != "Installing package"
                    ):
                        current_stage = "Installing package"
                        pbar.set_description(f"Updating package: {current_stage}")
                        pbar.update(stages[current_stage])
                        progress += stages[current_stage]

            # Завершаем прогресс
            if progress < 100:
                current_stage = "Finalizing"
                pbar.set_description(f"Updating package: {current_stage}")
                pbar.update(100 - progress)

            return_code = process.poll()
            if return_code == 0:
                return {"success": True, "message": "Update successful"}
            else:
                error_message = (
                    "\n".join(error_output)
                    if error_output
                    else "Unknown error occurred"
                )
                return {"success": False, "message": f"Update failed: {error_message}"}
        except Exception as e:
            return {"success": False, "message": f"Update failed: {str(e)}"}


if __name__ == "__main__":
    result = update_package()
    print(result["message"])
    if not result["success"]:
        sys.exit(1)
