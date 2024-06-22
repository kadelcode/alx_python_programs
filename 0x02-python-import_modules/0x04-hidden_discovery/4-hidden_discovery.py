import sys
import importlib.util

def print_module_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get all names defined in the module
    names = dir(module)

    # Filter names that don't start with __
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort names alphabetically
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)

if __name__ == '__main__':
    # Provide the path to the hidden_4.pyc file
    module_path = "hidden_4.pyc"
    print_module_names(module_path)
