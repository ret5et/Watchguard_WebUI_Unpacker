# Watchguard Fireware web update (Sysa-dl) file unpacker

+ unpack_watchguard is a tool that unpacks this file format.
+ watchguard_sysa_dl.ksy contains [Kaitai](https://kaitai.io/) description of Watchguard Fireware web update file format.

## Example

```
./unpack_watchguard M440.sysa-dl /tmp/hdd.ext2 #will extract firmware hdd ext2 file
```

Also you can explore Sysa-dl by ksv ( kaitai struct visualizer)

```
ksv M440.sysa-dl watchguard_sysa_dl.ksy
```

![](ksv.png "")

