# The MIT License (MIT)
#
# Copyright (c) 2015 Fabio Niephaus <code@fniephaus.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
import xml.etree.cElementTree as ET

class RWorkflow(object):
    _items = []
    theme_background = None

    def __init__(self):
        self.theme_background = os.environ.get('alfred_theme_background')

    def add_item(self, title, subtitle='', modifier_subtitles=None, arg=None,
                 autocomplete=None, valid=False, uid=None, icon=None,
                 icontype=None, type=None, largetext=None, copytext=None):

        valid = 'yes' if valid else 'no'
        uid = uid if uid else autocomplete

        children = [
            '<title>', title, '</title>',
            '<subtitle>', subtitle, '</subtitle>'
        ]
        if icon:
            children += ['<icon>', icon, '</icon>']

        self._items += ['<item']
        if arg:
            self._items += [' arg="%s"' % arg]
        if autocomplete:
            self._items += [' autocomplete="%s"' % autocomplete]
        if uid:
            self._items += [' uid="%s"' % uid]
        self._items += [' valid="%s">' % valid]  + children + ['</item>']

    def send_feedback(self):
        print '<?xml version="1.0" encoding="utf-8"?>'
        print ''.join(['<items>'] + self._items + ['</items>'])

    def is_dark(self):
        if self.theme_background is None:
            return False

        rgba_values = self.theme_background.split('(')[1].split(')')[0]

        rgb = [int(x) for x in rgba_values.split(',')[:3]]
        return (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255 < 0.5

    def get_icon(self, name):
        name = '%s-dark' % name if self.is_dark() else name
        return 'icons/%s.png' % name

    def execute_fallback(self, cmd):
        "NOT_RPYTHON"
        from subprocess import Popen, PIPE
        return Popen(cmd, shell=True, stdout=PIPE).communicate()

    def execute(self, cmd):
        try:
            from rpython.rlib.rfile import create_popen_file
        except:
            return self.execute_fallback(cmd)

        pipe = create_popen_file(cmd, "r")
        result = pipe.read()
        err = ""
        exit_status = os.WEXITSTATUS(pipe.close())
        if exit_status != 0:
            err = result
            result = ""
        return result, err
