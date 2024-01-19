"""
main
"""

import mistune
import libs
import bs4
import os

from . import renderer

__all__ = [ "main" ]

def main( configs : str = "./config.json" ) -> None :
    with libs.config.parser( configs ) as config :
        config.add( "birthday" , libs.get_time() , int )
        config.add( "giscus" , { "src" : "https://giscus.app/client.js", "async" : None } , ( bool , dict ) )
        config.add( "mistune_plugins" , [] , list )
    src = config( "source" )
    posts : str = config( "posts" )
    output : str = config( "output" )
    # giscus
    giscus = config( "giscus" )
    if isinstance( giscus , bool ) : giscus = False
    if giscus : giscus = bs4.BeautifulSoup().new_tag( "script" , **giscus )
    # load index.html
    theme_src = os.path.join( os.path.dirname( __file__ ) , "src" )
    libs.copytree( theme_src , output )
    if not os.path.exists( path := os.path.join( src , "theme" , "page.html" ) ) : path = os.path.join( theme_src , "theme" , "page.html" )
    with open( path , "r" , encoding = "utf-8" ) as file : data_theme = file.read()
    # posts
    post = []
    for path in os.listdir( posts ) :
        # load
        path = os.path.join( posts , path )
        if not all( os.path.exists( os.path.join( path , s ) ) for s in ( "index.md" , "info.json" ) ) : continue
        info = libs.config.parser( os.path.join( path , "info.json" ) )
        libs.checkdir( output_path := os.path.join( output , "post" , info( "id" ) ) )
        info.data[ "edit_time" ] = int( os.stat( path := os.path.join( path , "index.md" ) ).st_mtime )
        info.dump()
        with open( path , "r" , encoding = "utf-8" ) as fp : data = fp.read()
        # markdown -> html
        markdown = mistune.create_markdown( renderer = renderer.HTMLRenderer() , plugins = config( "mistune_plugins" ) )
        soup_post = bs4.BeautifulSoup( data_theme , "html.parser" )
        div_post = soup_post.find( "div" , id = "post" )
        div_title = soup_post.find( "div" , id = "title" )
        div_commit = soup_post.find( "div" , id = "commit" )
        head = soup_post.find( "head" )
        title = bs4.BeautifulSoup().new_tag( "title" )
        title.string = info( "title" )
        head.append( title )
        title = bs4.BeautifulSoup().new_tag( "h1" )
        title.string = info( "title" )
        div_title.append( title )
        if ( description := info( "description" ) ) is not None :
            p = bs4.BeautifulSoup().new_tag( "p" , id = "description" )
            p.string = description
            div_title.append( p )
        div_post.append( bs4.BeautifulSoup( markdown( data ) , "html.parser" ) )
        if giscus and info( "commint" ) : div_commit.append( giscus )
        else : div_commit.decompose()
        with open( os.path.join( output_path , "index.html" ) , "wb" ) as fp : fp.write( soup_post.prettify( "utf-8" ) )
    # api
    libs.checkfile( file := os.path.join( output , "api" , "info.json" ) )
    with libs.config.parser( file ) as info :
        info.add( "birthday" , config( "birthday" ) , int )
        info.add( "buildtime" , libs.get_time() , int )
        info.add( "post" , [] , list )
