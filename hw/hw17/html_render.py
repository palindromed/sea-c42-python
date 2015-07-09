#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """ Renders HTML """
    tag = 'html'
    indent = ''

    def __init__(self, name='', content=''):
        self.name = name
        self.content = content

    def append(self, new_text):
        self.content += new_text

    def render(self, file, indent=''):
        file.write(self.indent + '<' + self.tag + '>' + self.content + '</' +
                   self.tag + '>')


class Html(Element):
    '''Create an HTML tag'''
    tag = 'html'
    indent = ''


class Body(Element):
    ''' Create a body tag '''
    tag = 'body'
    indent = '  '


class P(Element):
    ''' Create a p tag '''
    tag = 'p'
    indent = '      '
