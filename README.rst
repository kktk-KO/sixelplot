sixelplot
=========

A thin wrapper for pysixel and matplotlib

Usage
-----

.. code:: python

    import matplotlib.pyplot as plt
    import sixelplot
    plt.plot([1, 2, 3])
    sixelplot.show()

SIXEL is the ancient black magic to render a graphical raster image on a
terminal screen.

``sixelplot.show`` function writes the SIXEL format image into a file
like object, by default stdout. Though you need a terminal which
understands the SIXEL format, modern terminal emulators support the
SIXEL format.

For more information about SIXEL, see
https://github.com/saitoha/libsixel.

License
-------

These codes are licensed under
`CC0 <https://creativecommons.org/publicdomain/zero/1.0/deed>`__.

Tips
----
