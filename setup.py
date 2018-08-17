import setuptools

with open("README.md") as fh:
  README_CONTENTS = fh.read()

config = {
  'name': 'PairBot',
  'version': '0.1',
  'author': 'Kiwidamien',
  'author_email': 'damien@bugmenot.com',
  'long_description': README_CONTENTS,
  'url': 'https://github.com/kiwidamien/pairbot/',
  'packages': setuptools.find_packages()
}

setuptools.setup(**config)
