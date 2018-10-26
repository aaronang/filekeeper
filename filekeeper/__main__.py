from filekeeper import get_files, delete_files

delete_files([f['id'] for f in get_files()[:10]])
