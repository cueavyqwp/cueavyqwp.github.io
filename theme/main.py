"""
main
"""

import pycmarkgfm
import libs
import bs4
import os

__all__ = [ "main" ]

def main( src : str = "./config.json" ) -> None :
    with libs.config.parser( src ) as config :
        config.add( "birthday" , libs.get_time() , int )
        config.add( "giscus" , { "src" : "https://giscus.app/client.js", "async" : None } , ( bool , dict ) )
    src = config( "source" )
    posts : str = config( "posts" )
    output : str = config( "output" )
    # giscus
    giscus = config( "giscus" )
    if isinstance( giscus , bool ) : giscus = False
    if giscus : giscus = bs4.BeautifulSoup().new_tag( "script" , **giscus )
    # load index.html
    with open( os.path.join( src , "index.html" ) , "r" , encoding = "utf-8" ) as file : data = file.read()
    index = bs4.BeautifulSoup( data , "html.parser" )
    div = index.find( "div" , id = "main" )
    # posts
    post = []
    for path in os.listdir( posts ) :
        path = os.path.join( posts , path )
        if not all( os.path.exists( os.path.join( path , s ) ) for s in ( "index.md" , "info.json" ) ) : continue
        info = libs.config.parser( os.path.join( path , "info.json" ) )
        libs.checkdir( output_path := os.path.join( output , "post" , info( "id" ) ) )
        with open( os.path.join( path , "index.md" ) , "r" , encoding = "utf-8" ) as fp : data = pycmarkgfm.gfm_to_html( fp.read() )
        soup = bs4.BeautifulSoup( data , "html.parser" )
        soup.append( giscus )
        with open( os.path.join( output_path , "index.html" ) , "wb" ) as fp : fp.write( soup.prettify( "utf-8" ) )
    # api
    libs.checkfile( file := os.path.join( output , "api" , "info.json" ) )
    with libs.config.parser( file ) as info :
        info.add( "birthday" , config( "birthday" ) , int )
        info.add( "buildtime" , libs.get_time() , int )
        info.add( "post" , [] , list )
