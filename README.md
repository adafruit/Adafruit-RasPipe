Adafruit-RasPipe
================

A small-display Raspberry Pi pipeline viewer using Python and Pygame.

See [RasPipe: A Raspberry Pi Pipeline Viewer, Part 1][1] for context and
detailed documentation.

contents
--------

* `raspipe.py` - scroll lines of standard input or display stars proportionally
  sized to each line.  Both a standalone script and a class, RasPipe.
* `raspipe_pitft.sh`
* `raspipe_tee` - a pipeline utility for sending things to a Pi running a RasPipe
  listener
* `listener.js` - a very brief node.js wrapper for listening on a network socket and
  sending things to stdout
* `listener_pitft.sh` - a shell script for using `netcat` to listen on a socket and pass
  things to `raspipe_pitft.sh`
* `flask_listener.py` - a simple web app using Flask to talk to the RasPipe class.
* `machine_stars.py` - standard input goes into a little machine and comes out
   as stars.

[1]: https://learn.adafruit.com/raspipe-a-raspberry-pi-pipeline-viewer
