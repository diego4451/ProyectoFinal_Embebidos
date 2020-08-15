
SUMMARY = "This is a python module for mouse automatization "
LICENSE = "CLOSED"

SRC_URI[md5sum] = "c71a5ab0bc833a760e1fdf68b36558fd"
SRC_URI[sha256sum] = "d34bb9548890089fcb11988400e26f55c624e6c7b741fff75fedfdfbd37c0016"

PYPI_PACKAGE = "mouse"

inherit pypi setuptools3

RDEPENDS_${PN} += " \
    python3-psutil \
"
EOF
