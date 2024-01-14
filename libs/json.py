"""
json
"""

import typing
import json

__all__ = [ "dump" , "dumps" ]

kwargs : dict[ typing.Any , typing.Any ] = { "indent" : 4 , "ensure_ascii" : False , "separators" : ( "," , ": " ) }

def dump( obj : typing.Any , fp : typing.TextIO ) -> None :
    json.dump( obj , fp , **kwargs )

def dumps( obj : typing.Any ) -> str :
    return json.dumps( obj , **kwargs ) 
