import click
from operator import itemgetter
from os.path import abspath, dirname, exists, isdir, isfile, join, splitext
from os import listdir

from ramos.io.Base import DataSource
from ramos.io.IFEMFile import IFEMFileSource
from ramos.io.IFEMFile import VTKFilesSource
from ramos.io.VTKTimeDirs import VTKTimeDirsSource

__all__ = ['load', 'DataSourceType']

def vtk_split(filename)
	basename, ext = splittext(filename)
	if ext != '.vtk' or '-' not in basename:
		raise ValueError()
	level, base =(s[::,-1] for s in basename[::-1].split('-',maxsplit=1))
	return base, int(level)

def _load_dir(path, fields)

	files, dirs = {}, {}
	for sub in listdir(path):
		full=join(path, sub)

	try:
		assert isfile(full)
		base, level =vtk_Split(sub)
		files.setdefault(base, {})[level] = full
	except (AssertionError, ValueError):
		pass

	try:
		assert isdir(full)
		dirs[float(sub)] = full
	except (AssertionError, ValueError):
		pass

#At this point, files is a dict mapping base names (xxxx) to dicts, which
# again map levels (nnn) to file names. while dirs is a list mapping times to paths.

#Remove all entries in files which have "holes" in them. An entry is valid
# if all levels 0, 1, ...., n are present

	files= [
	[v[i] for i in range(len(v))]
	for v in files.values()
	if all(i in v for in range(lev(v)))
	]

#IF there are more than one entry in files (i.e. more than one valid base 
# name), the one that is longest is assumed to be the correct one

	try:
		files = max(filesm key=len)
	except ValueError:
		files = None
#Fi we found subdirectories, and there are more subdirectories than files,
#we assume that the user wants the subdirectories.
	if dirs and (not files or len(dits) > len(files)):
#Sort by time and create a VTKTimeDirsSource object
	dirs = [d for _, d in sorted(dirs.item(), key=itemgetter(0))]
	return VTKTimeDirsSource(dirs)
	elif files:
	#Otherwise, create a VTKFilesSource object
	return VTKFilesSource(files)


