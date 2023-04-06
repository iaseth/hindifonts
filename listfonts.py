import os

FONT_FILE_EXTENSIONS = ["ttf", "otf"]
user_font_dirpath = os.path.expanduser("~/.local/share/fonts")
system_font_dirpath = os.path.expanduser("/usr/share/fonts")

def get_font_filepaths(dirpath):
	entry_paths = [os.path.join(dirpath, f) for f in os.listdir(dirpath)]
	filepaths = [f for f in entry_paths if os.path.isfile(f)]
	dirpaths = [f for f in entry_paths if os.path.isdir(f)]
	for dp in dirpaths:
		filepaths += get_font_filepaths(dp)

	font_filepaths = [f for f in filepaths if f.split(".")[-1] in FONT_FILE_EXTENSIONS]
	return font_filepaths

def main():
	user_font_filepaths = get_font_filepaths(user_font_dirpath)
	system_font_filepaths = get_font_filepaths(system_font_dirpath)
	font_filepaths = user_font_filepaths + system_font_filepaths

	for idx, font_filepath in enumerate(font_filepaths):
		filename = os.path.basename(font_filepath)
		print(f"{idx+1:3}. {filename:25}")

if __name__ == '__main__':
	main()
