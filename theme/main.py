"""
main
"""

import libs

__all__ = []

with libs.config.parser() as config :
    config.add( "output" , "./docs" , str )
    config.add( "apipath" , "./src/api" , ( str , bool ) )
    config.add( "buildtime" , False , bool )
