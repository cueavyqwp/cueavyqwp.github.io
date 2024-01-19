"""
renderer
"""
import pygments.formatters
import pygments.lexers
import traceback
import pygments
import mistune
import bs4

__all__ = [ "HTMLRenderer" ]

class HTMLRenderer( mistune.HTMLRenderer ) :

    def block_code( self, code : str , info : str | None = None ) -> str :
        try :
            if info == "mermaid" : return f"\n<pre class=\"mermaid\">{ code }</pre>"
            elif isinstance( info , str ) :
                lexer = pygments.lexers.get_lexer_by_name( info )
                formatter = pygments.formatters.HtmlFormatter()
                return pygments.highlight( code , lexer , formatter )
        except Exception :
            traceback.print_exc()
        return f"\n<div class=\"highlight\"><pre>{ code }</pre></div>"

    def heading( self , *args : tuple[ str ] , level : int ) -> str :
        title = bs4.BeautifulSoup( "".join( *args ) , "html.parser" )
        soup = bs4.BeautifulSoup( "" , "html.parser" )
        heading = bs4.BeautifulSoup().new_tag( f"h{ level }" , id = title.string )
        heading[ "class" ] = "heading"
        heading.append( title )
        soup.append( heading )
        return soup.prettify( "utf-8" ).decode()
