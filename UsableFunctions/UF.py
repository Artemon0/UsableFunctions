"""Public class used by both package import paths."""

from . import (
    auth,
    converters,
    files,
    games,
    math_utils,
    network,
    packages,
    scripts,
    system,
)
from ._metadata import (
    __author__ as __author__,
    __download_url__ as __download_url__,
    __email__ as __email__,
    __license__ as __license__,
    __url__ as __url__,
    __version__ as __version__,
)


class UsableFunctions:
    """A collection of utility functions for various programming tasks."""

    calculator = staticmethod(math_utils.calculator)
    even_odd = staticmethod(math_utils.even_odd)
    factorial = staticmethod(math_utils.factorial)
    math_factorial = staticmethod(math_utils.math_factorial)
    while_calculator = staticmethod(math_utils.while_calculator)
    Circle = math_utils.Circle

    quest = staticmethod(games.quest)
    game = staticmethod(games.game)
    say_hello = staticmethod(games.say_hello)
    say_goodbye = staticmethod(games.say_goodbye)
    is_pressed = staticmethod(games.is_pressed)

    write_in_new_file = staticmethod(files.write_in_new_file)
    read_from_file = staticmethod(files.read_from_file)
    delete_file = staticmethod(files.delete_file)
    rename_file = staticmethod(files.rename_file)
    move_file = staticmethod(files.move_file)
    create_new_file = staticmethod(files.create_new_file)
    read_file_content = staticmethod(files.read_file_content)
    download_file = staticmethod(files.download_file)
    compress_folder = staticmethod(files.compress_folder)
    get_file_hash = staticmethod(files.get_file_hash)
    extract_archive = staticmethod(files.extract_archive)
    get_folder_size = staticmethod(files.get_folder_size)

    FileConverter = converters.FileConverter

    install_package = staticmethod(packages.install_package)
    uninstall_package = staticmethod(packages.uninstall_package)
    install_package_git = staticmethod(packages.install_package_git)
    update_this_program = staticmethod(packages.update_this_program)
    update_this_program_visual = staticmethod(packages.update_this_program_visual)

    py_to_exe = staticmethod(scripts.py_to_exe)
    run_py_file = staticmethod(scripts.run_py_file)
    run_py_file_with_args = staticmethod(scripts.run_py_file_with_args)
    run_python_code = staticmethod(scripts.run_python_code)
    get_progress_bar = staticmethod(scripts.get_progress_bar)
    function_time = staticmethod(scripts.function_time)

    get_random_password = staticmethod(auth.get_random_password)
    token = staticmethod(auth.token)
    users = staticmethod(auth.users)
    register = staticmethod(auth.register)
    check_password = staticmethod(auth.check_password)

    get_ip_address = staticmethod(network.get_ip_address)
    get_mac_address = staticmethod(network.get_mac_address)
    get_external_ip = staticmethod(network.get_external_ip)
    ping_host = staticmethod(network.ping_host)

    get_machine_info = staticmethod(system.get_machine_info)
    get_memory_info = staticmethod(system.get_memory_info)
    get_disk_info = staticmethod(system.get_disk_info)
    get_cpu_info = staticmethod(system.get_cpu_info)
    optimize_system = staticmethod(system.optimize_system)
    system_panel = staticmethod(system.system_panel)
