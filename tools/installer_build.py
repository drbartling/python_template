# pylint: disable=fixme

import os
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path

import app_build
import click
import pkg_resources


@click.command()
def main():
    pd = ProjectDirectory()
    dist = pkg_resources.get_distribution("hello")

    app_build.main()
    pd.build_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(pd.build_dir)

    subprocess.run(
        " ".join(
            [
                "candle.exe",
                str(pd.wxs_path),
                '-dcompany_name="Acme Co"',
                '-dproduct_name="hello"',
                f'-dupgrade_code="{uuid.uuid4()}"',  # TODO: Hard code a permanent uuid
                f'-dpath_code="{uuid.uuid4()}"',  # TODO: Hard code a permanent uuid
                f'-dproduct_version="{dist.version}"',
                '-ddescription="Hello Greeter Application"',
                f'-dlicense_file="{pd.license_path}"',
                f'-dicon_path="{pd.icon_path}"',
                f'-dexecutable_path="{pd.executable_path}"',
                f'-dexecutable_name="{pd.executable_path.name}"',
            ]
        ),
        capture_output=False,
        check=True,
    )

    subprocess.run(
        " ".join(
            [
                "light.exe",
                f'-out "{pd.msi_path}"',
                "hello.wixobj",
                "-cultures:en-US",
                "-ext WixUIExtension",  # Adds installer GUI support
            ]
        ),
        capture_output=False,
        check=True,
    )


@dataclass
class ProjectDirectory:
    @property
    def script_dir(self) -> Path:
        return Path(__file__).parent

    @property
    def wxs_path(self) -> Path:
        return self.script_dir / "hello.wxs"

    @property
    def icon_path(self) -> Path:
        return self.script_dir / "icon.ico"

    @property
    def root_dir(self) -> Path:
        return self.script_dir.parent

    @property
    def license_path(self) -> Path:
        return self.root_dir / "license.rtf"

    @property
    def dist_dir(self) -> Path:
        return self.root_dir / "dist"

    @property
    def executable_path(self) -> Path:
        return self.dist_dir / "hello.exe"

    @property
    def msi_path(self) -> Path:
        return self.dist_dir / "hello.msi"

    @property
    def build_dir(self) -> Path:
        return self.root_dir / "build"


if __name__ == "__main__":
    main()
