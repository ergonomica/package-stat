package-status (DEPRECATED)
===========================

**THIS PROJECT HAS BEEN DEPRECATED IN FAVOR OF BUILT-IN ERGONOMICA FUNCTIONALITY.**

:code:`status` makes CPU/RAM/Disk usage statistics easily available throgh Ergonomica.

Installation (with epm)
-----------------------

First, install required dependencies through pip, like so:

.. code::
   
   pip install psutil cpuinfo

and then run

.. code::

   epm install status


Installation (without epm)
--------------------------

First, install required dependencies through pip, like so:

.. code::
   
   pip install psutil cpuinfo

Then, download :code:`status.py` from this repository and place it in :code:`~/.ergo/packages`.

Usage
-----

CPU Statistics
~~~~~~~~~~~~~~

Use the `cpu` command.

Get the percent CPU utilization:

.. code::

   $ cpu usage
   [50.6]
   
Get the number of CPU cores:

.. code::

   $ cpu count
   4

Get the advertised CPU clock speed:

.. code::

   $ cpu hz_advertized
   1.6000 GHz

Get the current CPU clock speed:

.. code::

   $ hz_actual
   1.1374 GHz

Get the CPU model name:

.. code::

   $ cpu brand
   Intel(R) Core(TM) i5-5250U CPU @ 1.60GHz

Get the CPU architecture/bits:

.. code::

   $ cpu bits
   64
   
RAM Statistics
~~~~~~~~~~~~~~

Get the amount of RAM free:

.. code::

   $ ram free
   [846372864]

   
Disk Statistics
~~~~~~~~~~~~~~~

Credits
-------

- Thanks to `@workhorsy`_ 's amazing py-cpuinfo_

.. _@workhorsy: https://github.com/workhorsy

.. _py-cpuinfo: https://github.com/workhorsy/py-cpuinfo
