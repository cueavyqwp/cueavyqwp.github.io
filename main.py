import http.server
import subprocess
import tempfile
import argparse
import langful
import shutil
import typing
import git
import os

os.chdir( os.path.dirname( __file__ ) )
import theme
import libs

class ArgumentParser( argparse.ArgumentParser ) :

    def __init__( self , prog : str , description : str , help : str , lang : langful.lang , **kwargs : typing.Any ) -> None :
        super().__init__( lang.get( prog ) , description = lang.get( description ) , add_help = False , **kwargs )
        self.add_argument( "-h" , "--help" , action = "help" , help = lang.get( help ) )
        self.lang = lang

if __name__ == "__main__" :
    # load configs
    config_src = "./config.json"
    lang = langful.lang()
    with libs.config.parser( config_src ) as config :
        config.add( "output" , "./docs" , str )
        config.add( "posts" , "./posts" , str )
        config.add( "source" , "./src" , str )
        config.add( "blacklist_clear" , [ "CNAME" ] , list )
        config.data[ "blacklist_clear" ] = [ str( value ) for value in config( "blacklist_clear" ) ]
        config.add( "repo" , None , ( str , None ) )
    repo = git.Repo( git_local ) if ( git_local := config( "repo" ) ) and os.path.exists( git_local ) else None
    output = str( config( "output" ) )
    posts = str( config( "posts" ) )
    src = str( config( "source" ) )
    # create dirs
    [ os.makedirs( path ) for path in ( src , posts , output ) if not os.path.exists( path ) ]
    # create a argument parser
    parser = ArgumentParser( "parser.name", "parser.description" , "help.help" , lang )
    parser.add_argument( "-s" , "--server" , required = False , action = "store_true" , help = lang.get( "help.server" ) )
    parser.add_argument( "--port" , required = False , default = 8080 , type = int , help = lang.get( "help.server.port" ) )
    parser.add_argument( "-b" , "--build" , required = False , action = "store_true" , help = lang.get( "help.build" ) )
    parser.add_argument( "-c" , "--clear" , required = False , action = "store_true" , help = lang.get( "help.clear" ) )
    parser.add_argument( "-p" , "--push" , required = False , action = "store_true" , help = lang.get( "help.push" ) )
    parser.add_argument( "--commit" , required = False , default = None , type = str , help = lang.get( "help.push.commit" ) )
    parser.add_argument( "-n" , "--new" , required = False , action = "store_true" , help = lang.get( "help.new" ) )
    args = parser.parse_args()
    # call
    if args.server :
        httpd = http.server.HTTPServer( ( "127.0.0.1" , port := args.port ) , http.server.SimpleHTTPRequestHandler )
        print( f"http://0.0.0.0{ f':{ port if port != 80 else '' }' }" )
        os.chdir( output )
        try : httpd.serve_forever()
        except KeyboardInterrupt : ...
        exit()
    if args.clear or args.build or args.push :
        for path in os.listdir( output ) :
            if path in config( "blacklist_clear" ) : continue
            if os.path.isfile( s := ( os.path.join( output , path ) ) ) : os.remove( s )
            else : shutil.rmtree( s )
        if args.clear : exit()
    if args.build or args.push :
        theme.main( config_src )
        libs.copytree( src , output )
        if args.build : exit()
    if args.push :
        if repo is None :
            print( lang.get( "info.git.cannot_use" ) )
        else :
            with tempfile.TemporaryFile( "w+" ) as tmp :
                print( lang.get( "info.git.cli.pull" ) )
                subprocess.check_call( [ git_exec := git.Git.git_exec_name , "pull" ] , stdout = tmp )
                print( lang.get( "info.git.cli.add" ) )
                subprocess.check_call( [ git_exec , "add" , "." ] )
                tmp.seek( 0 )
                l = tmp.readlines()
            s = f"update `{ libs.time.get_strtime() }`" if args.commit is None else args.commit
            print( f"{ lang.get( 'info.git.cli.commit.name' ) } \"{ s }\"" )
            print( lang.get( "info.git.cli.commit" ) )
            repo.index.commit( s )
            print( lang.get( "info.git.cli.push" ) )
            repo.remote().push()
            print( lang.get( "info.git.cli.info" ) )
            print( f"{ '=' * 32 }\n{ '\n'.join( f"| { s }" for s in l ) }{ '=' * 32 }" )
            print( lang.get( "info.git.cli.done" ) )
        exit()
    if args.new :
        post_time = libs.time.get_time()
        libs.checkdir( post := os.path.join( posts , str( post_time ) ) )
        libs.checkfile( os.path.join( post , "index.md" ) )
        with libs.config.parser( os.path.join( post , "info.json" ) ) as info :
            info.add( "id" , hex( post_time )[ 2 : ] , str )
            info.add( "time" , post_time , int )
            info.add( "title" , "untitled" , str )
            info.add( "type" , None , ( None , str ) )
            info.add( "tags" , [] , list )
        exit()
