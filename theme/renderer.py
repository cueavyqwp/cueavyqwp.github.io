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
            assert isinstance( info , str )
            lexer = pygments.lexers.get_lexer_by_name( info )
            formatter = pygments.formatters.HtmlFormatter()
            return pygments.highlight( code , lexer , formatter )
        except Exception :
            traceback.print_exc()
            return f"\n<pre><code>{ code }</code></pre>"

    def heading( self , *args , **kwargs ) -> str :
        ret = super().heading( *args , **kwargs )
        soup = bs4.BeautifulSoup( ret , "html.parser" )
        head = soup.find( f"h{ kwargs[ 'level' ] }" )
        head[ "id" ] = head.text
        return soup.prettify( "utf-8" ).decode()
