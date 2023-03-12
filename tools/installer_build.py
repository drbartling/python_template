import os
import subprocess
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
                '-dupgrade_code="f1d96f59-abc1-462c-b510-0f9c3875ef58"',
                '-dpath_code="3432CC21-C125-454B-89A9-0155573E3C4B"',
                f'-dproduct_version="{dist.version}"',
                '-ddescription="Hello Greeter Application"',
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
    def root_dir(self) -> Path:
        return self.script_dir.parent

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
