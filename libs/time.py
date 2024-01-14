"""
time
"""

import time

__all__ = [ "get_time" , "get_mstime" , "load" , "to_string" , "get_strtime" ]

def get_time() -> int :
    return int( time.time() )

def get_mstime() -> int :
    return int( time.time() * 1000 )

def load( secs : int | float ) -> time.struct_time :
    return time.localtime( float( secs ) )

def to_string( secs : int | float ) -> str :
    return time.strftime( "%Y-%m-%d %H:%M:%S" , load( secs ) )

def get_strtime() -> str :
    return to_string( get_time() )
