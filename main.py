import subprocess
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

def clear( output : str ) -> None :
    for path in os.listdir( output ) :
        if path in config( "blacklist_clear" ) : continue
        if os.path.isfile( s := ( os.path.join( output , path ) ) ) : os.remove( s )
        else : shutil.rmtree( s )

def build( output : str , src : str ) -> None :
    # copy files
    libs.copytree( src , output )

if __name__ == "__main__" :
    # load configs
    lang = langful.lang()
    with libs.config.parser() as config :
        config.add( "output" , "./docs" , str )
        config.add( "posts" , "./posts" , str )
        config.add( "source" , "./src" , str )
        config.add( "blacklist_clear" , [ "CNAME" ] , list )
        config.data[ "blacklist_clear" ] = [ str( value ) for value in config( "blacklist_clear" ) ]
        config.add( "git_local" , None , ( str , None ) )
        config.add( "git_remote" , None , ( str , None ) )
    git_local , git_remote = config( "git_local" ) , config( "git_remote" )
    git_state = bool( git_local and git_remote and os.path.exists( git_local ) )
    repo = git.Repo( git_local ) if git_state else None
    git_exec = git.Git.git_exec_name
    output = str( config( "output" ) )
    posts = str( config( "posts" ) )
    src = str( config( "source" ) )
    # create dirs
    [ os.makedirs( path ) for path in ( src , posts , output ) if not os.path.exists( path ) ]
    # create a argument parser
    parser = ArgumentParser( "parser.name", "parser.description" , "help.help" , lang )
    parser.add_argument( "-b" , "--build" , required = False , action = "store_true" , help = lang.get( "help.build" ) )
    parser.add_argument( "-c" , "--clear" , required = False , action = "store_true" , help = lang.get( "help.clear" ) )
    parser.add_argument( "-p" , "--push" , required = False , action = "store_true" , help = lang.get( "help.push" ) )
    args = parser.parse_args()

    if args.build or args.clear :
        print(output)
        clear( output )
        if args.clear : exit()
    if args.build :
        build( output , src )
        exit()
    if args.push :
        if repo is None :
            print( lang.get( "info.git.cannot_use" ) )
        else :
            subprocess.check_call( [ git_exec , "pull" ] )
            subprocess.check_call( [ git_exec , "add" , "." ] )
            repo.index.commit( f"update `{ libs.time.get_strtime() }`" )
            repo.remote().push()
        exit()
