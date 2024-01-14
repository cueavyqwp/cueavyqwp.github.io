"""
main
"""

import libs
import bs4

__all__ = []

with libs.config.parser() as config :
    config.add( "birthday" , libs.get_time() , int )
    config.add( "giscus" , { "src" : "https://giscus.app/client.js", "async" : None } , ( bool , dict ) )

giscus = config( "giscus" )
if isinstance( giscus , bool ) : giscus = False
if giscus : giscus = bs4.BeautifulSoup().new_tag( "script" , **giscus )
