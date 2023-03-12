#!/usr/bin/env python2

import zlib
from fw_web_up import FwWebUp
import argparse
from kaitaistruct import KaitaiStream


parser = argparse.ArgumentParser()
parser.add_argument('file', help='sysa-dl file')
parser.add_argument("out", help="unpacked hdd ext file")
args = parser.parse_args()

fw = FwWebUp.from_file(args.file)
for s in fw.sections.section:
    if s.head.name.name == "sysa_gzip":
        dec = zlib.decompressobj(32 + zlib.MAX_WBITS)
        hdd = dec.decompress(s.data)
        with open(args.out, "wb") as fd:
            fd.write(hdd)
