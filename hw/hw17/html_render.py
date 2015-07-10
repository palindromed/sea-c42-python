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
    '''Create an HTML tag'''
    name = 'html'
    def __init__(self, content=''):
        Element.__init__(self,  name='html')
        self.indent = ''


    def render(self, outfile, indent=''):
        outfile.write("<!DOCTYPE html>\n")
        Element.render(self, outfile)


class Head(Element):
    '''Create a head tag'''
    name = 'head'
  #  def __init__(self, content=''):
       # Element.__init__(self)
        #self.indent = '    '



class Body(Element):
    ''' Create a body tag '''
    name = 'body'
   # def __init__(self, content=''):
      # $ Element.__init__(self)



class P(Element):
    ''' Create a p tag '''
    name = 'p'
    indent = '        '

    #def __init__(self, content=''):
       # Element.__init__(self, content=content)
       # self.indent = '        '


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
    name = 'title'

    def __init__(self, content=''):
        Element.__init__(self, name='title', content=content)

