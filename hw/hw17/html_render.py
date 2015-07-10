#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """ Renders HTML elements """

    IND_LEVEL = '    '

    def __init__(self, name='', content=''):
        self.name = name
        self.children = [content] if content else []
        self.indent = '    '

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, outfile, indent=''):
        outfile.write("{}<{}>\n".format(self.indent, self.name))

        for child in self.children:
            try:
                child.render(outfile, self.indent + Element.IND_LEVEL)
            except AttributeError:
                outfile.write(self.indent + Element.IND_LEVEL + child + "\n")

        outfile.write(self.indent + "</" + self.name + ">\n")


class Html(Element):
    '''Create an HTML tag'''
    def __init__(self, content=''):
        Element.__init__(self,  name='html')
        self.indent = ''

    def render(self, outfile, indent=''):
        outfile.write("<!DOCTYPE html>\n")
        Element.render(self, outfile)


class Head(Element):
    '''Create a head tag'''
    def __init__(self, content=''):
        Element.__init__(self, name='head')
        #self.indent = '    '


class Body(Element):
    ''' Create a body tag '''
    def __init__(self, content=''):
        Element.__init__(self, name='body')


class P(Element):
    ''' Create a p tag '''

    def __init__(self, content=''):
        Element.__init__(self, name='p', content=content)
        self.indent = '        '


class OneLineTag(Element):
    """Render tags that stay on one line"""
    def render(self, outfile, content):
        outfile.write(self.indent + '<' + self.name + '>')

        for child in self.children:
            try:
                child.render(outfile, self.indent)
            except AttributeError:
                outfile.write(child)

        outfile.write("</" + self.name + ">\n")


class Title(OneLineTag):
    '''Create the one line element 'title' '''

    def __init__(self, content=''):
        Element.__init__(self, name='title', content=content)
        #self.name = 'title'
