from pathlib import Path

import PyInstaller.__main__


def main():
    project_root = (Path(__file__) / "../..").resolve()
    src_folder = project_root / "src"

    script = src_folder / "hello/hello.py"
    assert script.is_file()

    PyInstaller.__main__.run([str(script), "--onefile"])


main()
