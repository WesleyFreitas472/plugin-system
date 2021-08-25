import importlib
import os
import sys


PLUGIN_FOLDER = "plugins"
MAIN = "__init__"


def load_plugins() -> dict:
    plugins = {}
    possible_plugins = os.listdir(PLUGIN_FOLDER)
    for i in possible_plugins:
        location = os.path.join(PLUGIN_FOLDER, i)
        if not (not os.path.isdir(location)
                or not f"{MAIN}.py" in os.listdir(location)):
            plugin = importlib.import_module(f"{PLUGIN_FOLDER}.{i}", ".")
            plugins.update({i: plugin})
    return plugins


if __name__ == "__main__":
    plugins = load_plugins()
    plugin = sys.argv[1]
    try:
        plugins[plugin].Plugin().execute()
    except:
        raise Exception("Plugin não encontrado")
