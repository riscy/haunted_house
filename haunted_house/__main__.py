"""Haunted house HTML file generator for Hacktoberfest.
Usage: python haunted_house
"""
import importlib.util
import inspect
import os
import shutil
import types

_CONTAINING_DIR = os.path.dirname(__file__)


def _generate_html() -> None:
    scene_files = [
        f"{_CONTAINING_DIR}/{pyfile}"
        for pyfile in os.listdir(_CONTAINING_DIR)
        if pyfile.startswith('scene_') and pyfile.endswith('.py')
    ]
    for scene_file in scene_files:
        spec = importlib.util.spec_from_file_location('scene', scene_file)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _translate_module_to_html(module)

    # the index.html file should just be the entrance:
    shutil.copy('scene_entrance.py.html', 'index.html')


def _translate_module_to_html(module: types.ModuleType) -> None:
    assert module.__doc__ and module.__file__
    basename = os.path.basename(module.__file__) + '.html'
    filename = os.path.relpath(os.path.join(_CONTAINING_DIR, '..', basename))
    with open(filename, 'w', encoding='utf-8') as out:
        out.write('<!DOCTYPE html>\n')
        out.write('<link rel="stylesheet" type="text/css" href="haunted_house.css"/>\n')

        out.write('<div id="text">')
        out.write('<h3>' + module.__doc__ + '</h3>')
        out.write('<ul>')
        for function_name, function in inspect.getmembers(module):
            if not function_name.startswith('do_'):
                continue

            description, destination = function()
            description = description.replace("'", r"\'")
            script = (
                f"document.getElementById('text').innerHTML = '<h4>{description}</h4>';"
                + "setTimeout(function() {"
                + f"  location.replace('{destination}.py.html')"
                + "}, 3000);"
            )

            out.write('<li>')
            out.write(f'''<a href="#" onclick="javascript:{script}">''')
            out.write(function.__doc__)
            out.write('</a>')
            out.write('</li>')

        out.write('</ul>')
        out.write('</div>')
        print(f"Wrote {out.name}")


if __name__ == '__main__':
    _generate_html()
