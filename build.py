# SPDX-FileCopyrightText: 2026 Stefan Palan
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build dist/<id>-<version>.smplugin and its .sha256 from plugin.toml, the package and LICENSE."""
import hashlib
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
FIXED_TIME = (1980, 1, 1, 0, 0, 0)  # same bytes for the same files, so a rebuild gives the same hash


def files(meta):
    yield ROOT / "plugin.toml"
    yield ROOT / "LICENSE"
    for path in sorted((ROOT / meta["id"]).rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            yield path


def main():
    meta = tomllib.loads((ROOT / "plugin.toml").read_text(encoding="utf-8"))
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    asset = dist / f"{meta['id']}-{meta['version']}.smplugin"
    with zipfile.ZipFile(asset, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files(meta):
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    digest = hashlib.sha256(asset.read_bytes()).hexdigest()
    (dist / f"{asset.name}.sha256").write_text(f"{digest}  {asset.name}\n", encoding="utf-8")
    print(f"{asset.name}  {digest}")


if __name__ == "__main__":
    main()
