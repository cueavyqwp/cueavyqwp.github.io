"""
main
"""

import libs
import bs4

__all__ = []

with libs.config.parser() as config :
    config.add( "output" , "./docs" , str )
    config.add( "apipath" , "./src/api" , ( str , bool ) )
    config.add( "buildtime" , False , bool )
    config.add( "giscus" , { "src" : "https://giscus.app/client.js", "async" : None } , ( bool , dict ) )

giscus = config( "giscus" )
if isinstance( giscus , bool ) : giscus = False
if giscus : giscus = bs4.BeautifulSoup().new_tag( "script" , **giscus )# type: ignore
