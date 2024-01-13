import shutil
import os

os.chdir( os.path.dirname( __file__ ) )
import theme
import libs

# load configs
with libs.config.parser() as config :
    config.add( "blacklist_clear" , [ "CNAME" ] , list )
    config.data[ "blacklist_clear" ] = [ str( value ) for value in config( "blacklist_clear" ) ]
output = str( config( "output" ) )
# create dirs
[ os.makedirs( path ) for path in [ "./src" , output ] if not os.path.exists( path ) ]
# clear up
for path in os.listdir( output ) :
    if path in config( "blacklist_clear" ) : continue
    if os.path.isfile( s := ( os.path.join( output , path ) ) ) : os.remove( s )
    else : shutil.rmtree( s )
# copy files
for root , dirs , files in os.walk( "./src" ) :
    for file in files :
        file = s = os.path.join( root , file )
        paths : list[ str ] = []
        while len( paths ) < 2 or not paths[ 0 ] == paths[ 1 ] :
            paths = list( os.path.split( s ) ) + paths
            s = paths.pop( 0 )
        paths = paths[ 4 : ] if paths[ 2 ] == "." else paths[ 3 : ]
        path = os.path.join( output , *paths )
        os.makedirs( os.path.split( path )[ 0 ] , exist_ok = True )
        shutil.copyfile( file , os.path.join( output , *paths ) )
