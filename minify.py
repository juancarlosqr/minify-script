#!/usr/bin/python

import httplib, urllib, sys

def getMinify( web_service, endpoint, params, method = 'POST' ):
    headers = { "Content-type" : "application/x-www-form-urlencoded" }
    conn = httplib.HTTPConnection( web_service )
    conn.request( method, endpoint, params, headers )
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def writeMinify( minify ):
    f = open( sys.argv[3], 'w' )
    f.write( minify )
    f.close()

def readCode():
    f = open( sys.argv[2], 'r' )
    code = f.read()
    f.close()
    return code

file_type = sys.argv[1]

if file_type == "js":
    params = urllib.urlencode([
        ( 'js_code', readCode() ),
        ( 'compilation_level', 'SIMPLE_OPTIMIZATIONS' ),
        ( 'output_format', 'text' ),
        ( 'output_info', 'compiled_code' ),
    ])
    minify = getMinify( 'closure-compiler.appspot.com', '/compile', params )
    writeMinify( minify )

if file_type == "css":
    params = urllib.urlencode([
        ( 'input', readCode() ),
    ])
    minify = getMinify( 'cssminifier.com', '/raw', params )
    writeMinify( minify )