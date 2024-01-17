"""
path
"""

import shutil
import os

__all__ = [ "checkdir" , "checkfile" , "copytree" ]

def checkdir( path : str ) -> None :
    os.makedirs( path , exist_ok = True )

def checkfile( path : str ) -> None :
    if os.path.exists( path ) :
        if os.path.isdir( path ) : shutil.rmtree( path )
        else : return
    checkdir( os.path.split( path )[ 0 ] )
    with open( path , "wb" ) : pass

def copytree( src : str , dst : str ) -> None :
    src = os.path.relpath( src )
    for root , _ , files in os.walk( src ) :
        for file in files :
            file = s = os.path.join( root , file )
            paths : list[ str ] = []
            while len( paths ) < 2 or not paths[ 0 ] == paths[ 1 ] :
                paths = list( os.path.split( s ) ) + paths
                s = paths.pop( 0 )
            path = os.path.join( dst , *( paths[ ( 4 if len( paths ) > 4 else 3 ) : ]) )
            os.makedirs( os.path.dirname( path ) , exist_ok = True )
            shutil.copyfile( file , path )
