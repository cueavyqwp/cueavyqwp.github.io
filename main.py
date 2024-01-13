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
libs.copytree( "./src" , output )
