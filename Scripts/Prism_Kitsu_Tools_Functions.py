import os
import errno

from qt_compat import *


def printText(text, name="Print"):
    QMessageBox.warning(QWidget(), str(name), str(text))


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
