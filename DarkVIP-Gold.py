import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))