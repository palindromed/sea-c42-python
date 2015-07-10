#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """ Renders HTML elements """
    name = 'html'
    IND_LEVEL = '    '
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.attr = ''
        for attr_key, attr_val in self.attributes.items():
            self.attr += " {key}=\"{val}\"".format(key=attr_key, val=attr_val)

        self.children = [content] if content else []

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, outfile, indent=''):
        outfile.write(self.indent + "<" + self.name + self.attr + ">\n")

        for child in self.children:
            try:
                child.render(outfile, self.indent + Element.IND_LEVEL)
            except AttributeError:
                outfile.write(self.indent + Element.IND_LEVEL + child + "\n")

        outfile.write(self.indent + "</" + self.name + ">\n")


class Html(Element):
    """Create an HTML tag"""
    name = 'html'
    indent = ''

    def render(self, outfile, indent=''):
        outfile.write("<!DOCTYPE html>\n")
        Element.render(self, outfile)


class Head(Element):
    """Create a head tag"""
    name = 'head'


class Body(Element):
    """ Create a body tag """
    name = 'body'


class P(Element):
    """Create a p tag """
    name = 'p'
    indent = '        '


class OneLineTag(Element):
    """Render tags that stay on one line"""
    def render(self, outfile, content):
        outfile.write(self.indent + '<' + self.name + self.attr + '>')

        for child in self.children:
            try:
                child.render(outfile, self.indent)
            except AttributeError:
                outfile.write(child)

        outfile.write("</" + self.name + ">\n")


class Title(OneLineTag):
    """Create the one line element 'title' """
    name = 'title'

    def __init__(self, content=''):
        Element.__init__(self, name='title', content=content)


class A(OneLineTag):
    """(a)nchor tag"""
    name = "a"

    def __init__(self, link, content):
        """override init create working 'a' tag"""
        self.link = link
        self.content = content
        Element.__init__(self, href=link, content=content)


class SelfClosingTag(Element):
    """render a self closing tag"""
    def render(self, outfile, indent=""):
        outfile.write(self.indent + "<" + self.name + self.attr + "/>\n")


class Hr(SelfClosingTag):
    """hr tag"""
    name = "hr"


class Br(SelfClosingTag):
    """br tag"""
    name = "br"
