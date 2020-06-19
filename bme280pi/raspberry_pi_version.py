"""
Contains the detect_raspberry_pi_version function, which
detects the version of the Raspberry Pi used.
"""
import warnings


def detect_raspberry_pi_version():
    """
    Detect the Raspberry Pi Version
    """
    known_revisions = {'0002': 'Model B R1',
                       '0003': 'Model B R1',
                       '0004': 'Model B R2',
                       '0005': 'Model B R2',
                       '0006': 'Model B R2',
                       '0007': 'Model A',
                       '0008': 'Model A',
                       '0009': 'Model A',
                       '000d': 'Model B R2',
                       '000e': 'Model B R2',
                       '000f': 'Model B R2',
                       '0010': 'Model B+',
                       '0011': 'Compute Module',
                       '0012': 'Model A+',
                       'a01041': 'Pi 2 Model B',
                       'a21041': 'Pi 2 Model B',
                       '900092': 'Pi Zero',
                       '900093': 'Pi Zero',
                       'a02082': 'Pi 3 Model B',
                       'a22082': 'Pi 3 Model B',
                       '9000c1': 'Pi Zero W',
                       'c03111': 'Pi 4 Model B',
                       'abcdef': 'TestModel',
                       '0000': 'Unknown'}
    revision = "0000"
    try:
        cpuinfo = open("/proc/cpuinfo", "r")
        for line in cpuinfo:
            if line.find("Revision") >= 0:
                revision = line.rstrip().replace(" ", "").split(":")[1]
        cpuinfo.close()
    except FileNotFoundError:
        warnings.warn("Could not find /proc/cpuinfo")
        return "Unknown"

    if revision in known_revisions:
        return known_revisions[revision]

    return "Unknown"