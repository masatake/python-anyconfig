#
# Copyright (C) 2015 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# Ref. python -c "import msgpack; help(msgpack.Unpacker); help(msgpack.Packer)"
#
"""MessagePack file backend.

.. versionadded:: 0.0.11

- Format to support: MessagePack, http://msgpack.org
- Requirements: msgpack-python (https://pypi.python.org/pypi/msgpack-python)
- Limitations: None obvious
- Special options:

  - All options of msgpack.load{s,} and msgpack.dump{s,} except object_hook
    and file_like should work.

  - See also: http://pythonhosted.org/msgpack-python/api.html
"""
from __future__ import absolute_import

import msgpack
import anyconfig.backend.json


class Parser(anyconfig.backend.json.Parser):
    """
    Loader/Dumper for MessagePack files.
    """
    _type = "msgpack"
    _extensions = []
    _load_opts = ["read_size", "use_list", "object_pairs_hook", "list_hook",
                  "encoding", "unicode_errors", "max_buffer_size", "ext_hook",
                  "max_str_len", "max_bin_len", "max_array_len", "max_map_len",
                  "max_ext_len", "object_pairs_hook"]
    _dump_opts = ["default", "encoding", "unicode_errors", "use_single_float",
                  "autoreset", "use_bin_type"]
    _open_flags = ('rb', 'wb')
    _funcs = dict(loads=msgpack.unpackb, load=msgpack.unpack,
                  dumps=msgpack.packb, dump=msgpack.pack)

# vim:sw=4:ts=4:et:
