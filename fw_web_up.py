# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class FwWebUp(KaitaiStruct):

    class Magic(Enum):
        type1 = 308353312
        type2 = 358684968
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_fwheader = self._io.read_bytes(24)
        _io__raw_fwheader = KaitaiStream(BytesIO(self._raw_fwheader))
        self.fwheader = FwWebUp.Fwheader(_io__raw_fwheader, self, self._root)
        self._raw_sections = self._io.read_bytes((self._io.size() - 24))
        _io__raw_sections = KaitaiStream(BytesIO(self._raw_sections))
        self.sections = FwWebUp.Sections(_io__raw_sections, self, self._root)

    class Sections(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.section = []
            i = 0
            while not self._io.is_eof():
                self.section.append(FwWebUp.Section(self._io, self, self._root))
                i += 1



    class Name(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self.is_type2:
                self.type2_magic = self._io.read_u1()

            self.content = (KaitaiStream.bytes_terminate(self._io.read_bytes((15 if self.is_type2 else 16)), 0, False)).decode(u"ASCII")

        @property
        def type2(self):
            if hasattr(self, '_m_type2'):
                return self._m_type2

            _pos = self._io.pos()
            self._io.seek(0)
            self._m_type2 = self._io.read_u1()
            self._io.seek(_pos)
            return getattr(self, '_m_type2', None)

        @property
        def is_type2(self):
            if hasattr(self, '_m_is_type2'):
                return self._m_is_type2

            self._m_is_type2 = self.type2 == 127
            return getattr(self, '_m_is_type2', None)


    class Head(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_name = self._io.read_bytes(16)
            _io__raw_name = KaitaiStream(BytesIO(self._raw_name))
            self.name = FwWebUp.Name(_io__raw_name, self, self._root)
            if self.name.is_type2:
                self.unk = self._io.read_bytes(24)

            self.data_size = self._io.read_u4be()
            if self.name.is_type2:
                self.data_md5 = self._io.read_bytes(16)



    class Section(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.head = FwWebUp.Head(self._io, self, self._root)
            _on = self.head.name.content
            if _on == u"REBOOT":
                self._raw_data = self._io.read_bytes(self.head.data_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = FwWebUp.Rebootdata(_io__raw_data, self, self._root)
            elif _on == u"WGPKG":
                self._raw_data = self._io.read_bytes(self.head.data_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = FwWebUp.Wgpkgdata(_io__raw_data, self, self._root)
            elif _on == u"info":
                self._raw_data = self._io.read_bytes(self.head.data_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = FwWebUp.Infodata(_io__raw_data, self, self._root)
            elif _on == u"HMAC":
                self._raw_data = self._io.read_bytes(self.head.data_size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = FwWebUp.Hmacdata(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(self.head.data_size)


    class Hmacdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sha1_sign = self._io.read_bytes(20)


    class Infodata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.info = (KaitaiStream.bytes_terminate(self._io.read_bytes_full(), 0, False)).decode(u"ASCII")


    class Fwheader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.md5sum = self._io.read_bytes(16)
            self.file_size = self._io.read_u4be()
            self.magic_sign = KaitaiStream.resolve_enum(FwWebUp.Magic, self._io.read_u4be())


    class Rebootdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_perm = self._io.read_bytes(8)
            _io__raw_perm = KaitaiStream(BytesIO(self._raw_perm))
            self.perm = FwWebUp.EncodedPerm(_io__raw_perm, self, self._root)


    class Wgpkgdata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.meta_info = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.magic = self._io.read_bytes(6)
            if not self.magic == b"\x57\x47\x50\x4B\x47\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x57\x47\x50\x4B\x47\x00", self.magic, self._io, u"/types/wgpkgdata/seq/1")
            self.unk = self._io.read_bytes(2)
            self.unkdw1 = self._io.read_u4be()
            self.data_size = self._io.read_u4be()
            self.compressed_wpkg = self._io.read_bytes(self.data_size)


    class EncodedPerm(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dw0 = self._io.read_u4be()
            self.dw1 = self._io.read_u4be()



