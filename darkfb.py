import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
