import zipfile

fname = "flag101.zip"


while True:
	data = open(fname, 'rb').read
	z = zipfile.ZipFile(fname)
	fname = z.namelist()[0]
	print fname
	z.extractall()
