LICENSE = "CLOSED"

SRC_URI = "file://Test.py \
	   file://PIN.ui \
	   file://PIN.py \
	   file://Mouse.py \
	   file://Image.ui \
	   file://Image.py \
	   file://Access.ui \
	   file://Access.py \
           file://Qtime.py \
	   file://1.png \
	   file://Blue.png \
	   file://Red.png \
	   file://Green.png"

S="${WORKDIR}"

do_install(){
    install -d  ${D}${bindir}/iguana
    install -d  ${D}${bindir}/iguana/Images
    #install -m 0755 Test.py ${D}${bindir}/iguana
    install -m 0755 PIN.ui ${D}${bindir}/iguana
    install -m 0755 PIN.py ${D}${bindir}/iguana
    install -m 0755 Image.ui ${D}${bindir}/iguana
    install -m 0755 Image.py ${D}${bindir}/iguana
    install -m 0755 Access.ui ${D}${bindir}/iguana
    install -m 0755 Access.py ${D}${bindir}/iguana
    install -m 0755 Qtime.py ${D}${bindir}/iguana
    install -m 0755 1.png ${D}${bindir}/iguana/Images
    install -m 0755 Blue.png ${D}${bindir}/iguana/Images
    install -m 0755 Red.png ${D}${bindir}/iguana/Images
    install -m 0755 Green.png ${D}${bindir}/iguana/Images
}

