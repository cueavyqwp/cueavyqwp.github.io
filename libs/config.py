"""
config
"""

import typing
import libs

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
            with open( file , "r" , encoding = "utf-8" ) as fp : self.data = libs.json.load( fp )
        except :
            self.dump()

    def dump( self ) -> None :
        with open( self.file , "w" , encoding = "utf-8" ) as fp : libs.dump( self.data , fp )

    def add( self , name : str , default : typing.Any , type : typing.Any | tuple[ typing.Any ] ) -> None :
        if not isinstance( type , tuple ) or not len( type ) : type = ( type , )
        if name not in self.data or not ( any( obj is None and self.data[ name ] is None or isinstance( self.data[ name ] , obj ) for obj in type ) ) : self.data[ name ] = default
