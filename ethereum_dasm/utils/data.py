#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
import binascii


def hex_decode(s):
    try:
        return bytes.fromhex(s).decode('ascii')
    except (NameError, AttributeError):
        return s.decode("hex")
    except UnicodeDecodeError:
        return ''  # invalid


def is_ascii_subsequence(s, min_percent=0.51):
    if len(s) == 0:
        return False
    if isinstance(s, bytes):
        s = s.rstrip(b'\x00')  # ignore zero padding
        if not len(s):
            return False
        return [128 > c > 0x20 for c in s].count(True) / float(len(s)) >= min_percent
    return [128 > ord(c) > 0x20 for c in s].count(True) / float(len(s)) >= min_percent


def is_all_ascii(s):
    if isinstance(s, bytes):
        return all(128 > c > 0x20 for c in s)
    return all(128 > ord(c) > 0x20 for c in s)


def str_to_bytes(s):
    """
    Convert 0xHexString to bytes
    :param s: 0x hexstring
    :return:  byte sequence
    """
    try:
        return bytes.fromhex(s.replace("0x", ""))
    except (NameError, AttributeError):
        return s.decode("hex")


def bytes_to_str(s, prefix="0x"):
    return "%s%s" % (prefix,binascii.hexlify(s).decode("utf-8"))
