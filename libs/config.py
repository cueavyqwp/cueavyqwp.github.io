"""
config
"""

import typing
import json

__all__ = [ "parser" ]

class parser :

    def __enter__( self ) -> "parser" :
        return self

    def __exit__( self , *args : tuple[ typing.Any ] ) -> None :
        self.dump()

    def __str__( self ) -> str :
        return str( self.data )

    def __call__( self , name : str ) -> typing.Any :
        return self.data[ name ]

    def __init__( self , file : str = "./config.json" ) -> None :
        self.data : dict[ typing.Any , typing.Any ] = {}
        self.file : str = file
        try :
            with open( file , "r" , encoding = "utf-8" ) as fp : self.data = json.load( fp )
        except :
            self.dump()

    def dump( self ) -> None :
        with open( self.file , "w" , encoding = "utf-8" ) as fp : json.dump( self.data , fp , indent = 4 , ensure_ascii = False , separators = ( "," , ": " ) )

    def add( self , name : str , default : typing.Any , type : typing.Any ) -> None :
        if name not in self.data or not isinstance( self.data[ name ] , type ) : self.data[ name ] = default
