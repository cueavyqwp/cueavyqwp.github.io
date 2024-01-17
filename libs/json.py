"""
json
"""

import typing
import json

__all__ = [ "load" , "loads" , "dump" , "dumps" ]

kwargs : dict[ typing.Any , typing.Any ] = { "indent" : 4 , "ensure_ascii" : False , "separators" : ( "," , ": " ) }

def load( fp : typing.TextIO ) -> dict[ typing.Any , typing.Any ] :
    return json.load( fp )

def loads( s : str ) -> dict[ typing.Any , typing.Any ] :
    return json.loads( s )

def dump( obj : typing.Any , fp : typing.TextIO ) -> None :
    json.dump( obj , fp , **kwargs )

def dumps( obj : typing.Any ) -> str :
    return json.dumps( obj , **kwargs ) 
