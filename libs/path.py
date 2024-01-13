"""
path
"""

import shutil
import os

__all__ = [ "copytree" ]

def copytree( src : str , dst : str ) -> None :
    for root , _ , files in os.walk( src ) :
        for file in files :
            file = s = os.path.join( root , file )
            paths : list[ str ] = []
            while len( paths ) < 2 or not paths[ 0 ] == paths[ 1 ] :
                paths = list( os.path.split( s ) ) + paths
                s = paths.pop( 0 )
            path = os.path.join( dst , *( paths[ 4 : ] if paths[ 2 ] == "." else paths[ 3 : ] ) )
            os.makedirs( os.path.split( path )[ 0 ] , exist_ok = True )
            shutil.copyfile( file , path )
