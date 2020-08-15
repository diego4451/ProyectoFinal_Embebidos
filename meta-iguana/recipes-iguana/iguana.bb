LICENSE = "CLOSED"

SRC_URI = "file://Test.py \
	   file://PIN.ui \
	   file://PIN.py \
	   file://Mouse.py \
	   file://Image.ui \
	   file://Image.py \
	   file://Access.ui \
	   file://Access.py \

S="S{WORKDIR}"

do_install(){
	install -d  ${D}${base_bindir}/iguana
 	install -d  ${D}${base_bindir}/iguana/Images
	install -m 0755 Test.py ${D}${base_bindir}/iguana
	install -m 0755 PIN.ui ${D}${base_bindir}/iguana
	install -m 0755 PIN.py ${D}${base_bindir}/iguana
	install -m 0755 Image.ui ${D}${base_bindir}/iguana
	install -m 0755 Image.py ${D}${base_bindir}/iguana
	install -m 0755 Access.ui ${D}${base_bindir}/iguana
	install -m 0755 Access.py ${D}${base_bindir}/iguana
}

