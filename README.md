# iCalc
advanced cli calculator building off simple eval by Daniel Fairhead

## To install

Git clone the repo or download as a zip and move it to where you see fit. <br><br>
###Option 1
iCalc requires virtualenv since your python version may differ. First, if you don't already have it, get pip. Pip for *nix machines can be installed via <code>$ sudo easy_install pip</code>. For windows consult http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip and download the pip pkg. Once that is done, get virtualenv by running <code>$ sudo pip install virtualenv </code> Ignore sudo if you're using Windows. You can then run the following: <pre>$ cd iCalc <br>$ virtualenv venv <br>$ source venv/bin/activate <br>$ pip install -r requirements.txt </pre> If this runs into an error with downloading the icalc package run (with sudo if on *NIX machines)<code>$ pip install -e git+https://github.com/JonW27/iCalc.git#egg=icalc</code><br>
Run <code>icalc --help</code> to show the page.<br>
Documentation is provided via --help.

## To contribute

Fork and do whatever you want.

## License

This repo is under the MIT license; see the LICENSE page for the complete license.
