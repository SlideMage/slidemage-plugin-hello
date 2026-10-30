# Hello

A sample plugin for testing the SlideMage plugin catalogue. It does nothing.

## Development

The plugin is registered as hidden in the website's registry: it appears only in the test catalogue
(`plugins/index-test.json`), never in SlideMage's real plugin list. Its releases exercise the catalogue builder
and the app's installer.

Build the release asset with `python build.py`. It writes `dist/<id>-<version>.smplugin` (a zip of
`plugin.toml`, the package and `LICENSE`) and its `.sha256`. Attach both to a GitHub release tagged
`v<version>`, the same version as in `plugin.toml`.

## Licence

GPL-3.0-or-later, see `LICENSE`. The plugin comes with no warranty: to the extent permitted by applicable law, it is
provided "as is", without warranty of any kind, and the copyright holders are not liable for any damage arising from
its use (GPL-3.0 sections 15 and 16).
