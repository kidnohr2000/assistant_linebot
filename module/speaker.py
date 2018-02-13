# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab


class Talking(object):

    def __init__(self, person):
        self.person = person

    def greeting(self):
        if self.person == 'kaide':
            return 'や、元気？？'
        else:
            return 'Hello, World'
