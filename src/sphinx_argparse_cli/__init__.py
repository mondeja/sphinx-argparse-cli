from __future__ import annotations

from sphinx.application import Sphinx

from .version import __version__


def setup(app: Sphinx) -> None:
    app.add_css_file("custom.css")

    from ._logic import SphinxArgparseCli

    app.add_directive(SphinxArgparseCli.name, SphinxArgparseCli)


__all__ = ("__version__",)
