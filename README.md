# Watchguard Fireware Web UI updates file unpacker
+ unpack_watchguard is a tool that unpacks this file format (sysa-dl).
+ watchguard_sysa_dl.ksy contains [Kaitai](https://kaitai.io/) description of Watchguard Fireware web update file format.

## Info
This update format is used by WatchGuard Firebox firewalls. The unpacker has been tested on firmware for the M400 and M500 series. An example of an update file can be found [here](https://software.watchguard.com/SoftwareDownloads?current=true&familyId=a2RF00000009S0FMAU)

## Example
```
./unpack_watchguard M440.sysa-dl /tmp/hdd.ext2
```
## File struct viewer
Also you can explore Sysa-dl by ksv ( kaitai struct visualizer)

```
ksv M440.sysa-dl watchguard_sysa_dl.ksy
```

![](ksv.png "")

