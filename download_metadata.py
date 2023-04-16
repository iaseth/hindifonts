import json
import requests



def main():
	GOOGLE_FONTS_METADATA_URL = "https://fonts.google.com/metadata/fonts"
	GOOGLE_FONTS_METADATA_FILEPATH = "data/googlefonts.json"
	res = requests.get(GOOGLE_FONTS_METADATA_URL)

	jo = json.loads(res.text)
	with open(GOOGLE_FONTS_METADATA_FILEPATH, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"saved: {GOOGLE_FONTS_METADATA_FILEPATH}")


if __name__ == '__main__':
	main()
