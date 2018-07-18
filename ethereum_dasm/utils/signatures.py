#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>


try:
    import ethereum_input_decoder
except ImportError:
    ethereum_input_decoder = None


cache_lookup_function_signature = {}  # memcache for lookup_function_signature


def lookup_function_signature(sighash):
    if not ethereum_input_decoder:
        return []
    cache_hit = cache_lookup_function_signature.get(sighash)
    if cache_hit:
        return cache_hit
    cache_lookup_function_signature[sighash] = list(ethereum_input_decoder.decoder.FourByteDirectory.lookup_signatures(sighash))
    return cache_lookup_function_signature[sighash]
