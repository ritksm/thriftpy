ThriftPy Changelog
==================

Version 0.1.10
--------------

Released on September 4, 2014.

- fix memory free bug in cython buffered transport, via `#35`_.
- new thrift parser by PLY, removed cache since the performance is much more
  faster now, via `#36`_.

.. _`#35`: https://github.com/eleme/thriftpy/pull/35
.. _`#36`: https://github.com/eleme/thriftpy/pull/36


Version 0.1.9
-------------

Released on September 1, 2014.

- refine cython binary protocol, add cython buffered transport, via `#32`_.
- param name change, rename transport_factory to trans_factory in rpc.

.. _`#32`: https://github.com/eleme/thriftpy/pull/32


Version 0.1.8
-------------

Released on August 28, 2014.

- faster thrift file parse speed, via `#30`_.
- bugfix for cybin buffer read, via `#31`_.

.. _`#30`: https://github.com/eleme/thriftpy/pull/30
.. _`#31`: https://github.com/eleme/thriftpy/pull/31


Version 0.1.7
-------------

Released on August 19, 2014.

- use args instead of kwargs in api calling to match upstream behavior.
- cython binary protocol auto grow buffer size, via `#29`_.
- bugfix for void api exception handling in processor.
- bugfix for cybin protocol buffer overflow and memcpy, via `#27`_ and `#28`_.

.. _`#27`: https://github.com/eleme/thriftpy/pull/27
.. _`#28`: https://github.com/eleme/thriftpy/pull/28
.. _`#29`: https://github.com/eleme/thriftpy/pull/29


Version 0.1.6
-------------

Released on August 14, 2014.

- json protocol, via `#21`_.
- more standard module for loaded sdk, now generated TPayload objects can
  be pickled when module_name provided, via `#22`_.
- gunicorn_thrift integration pingpong example, via `#24`_.
- token cache now only checks python's major and minor version.
- bugfix for exception handling in void api in RPC request.
- bugfix for negative number value not recognized.
- bugfix for cybin protocol to allow None value in struct.
- bugfix for double free or corruption in cybin protocol, via `#26`_.

.. _`#21`: https://github.com/eleme/thriftpy/pull/21
.. _`#22`: https://github.com/eleme/thriftpy/pull/22
.. _`#24`: https://github.com/eleme/thriftpy/pull/24
.. _`#26`: https://github.com/eleme/thriftpy/pull/26


Version 0.1.5
-------------

Released on July 25, 2014.

- tornado client, server and framed transport support with tornado 4.0,
  via `#15`_.
- immediately read from TMemoryBuffer after writing to it, via `#20`_.
- cache `load` function to avoid duplicate module generation.
- support client with socket timeout
- enum struct now has VALUES_TO_NAMES and NAMES_TO_VALUES.

.. _`#15`: https://github.com/eleme/thriftpy/pull/15
.. _`#20`: https://github.com/eleme/thriftpy/pull/20


Version 0.1.4
-------------

Released on July 17, 2014.

- parser token cache, speed boost for thrift file parsing, via `#12`_.
- new cython binary protocol with speed very close to c ext, via `#16`_.

.. _`#12`: https://github.com/eleme/thriftpy/pull/14
.. _`#16`: https://github.com/eleme/thriftpy/pull/14


Version 0.1.3
-------------

Released on June 19, 2014.

- support for union, binary fields, support for empty structs,
  support for Apache Storm thrift file, via `#14`_.
- bugfix for import hook
- bugfix for skip function in binary protocols

.. _`#14`: https://github.com/eleme/thriftpy/pull/14


Version 0.1.2
-------------

Released on June 7, 2014.

- disabled the magic import hook by default. and add install/remove
  function to switch the hook on and off.
- reworked benchmark suit and add benchmark results.
- new `__init__` function code generator. get a noticable speed boost.
- bug fixes


Version 0.1.1
-------------

First public release.
