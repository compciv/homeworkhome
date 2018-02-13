import requests
from pathlib import Path


DATA_SRC_URL = 'https://compciv.github.io/homeworkhome/assets/trump-tweets-twarc.json'

DATA_DIR = Path('datastash')
DATA_FILEPATH = Path(DATA_DIR, 'trump-tweets-twarc.json')

def read_data():
    """
    A convenience function that knows where the data file is saved on
    the computer, so that other programs don't have to care about
    file management.

    If the data file doesn't exist, this function downloads it from
    the specified remote URL (DATA_SRC_URL)

    Args:
        None
    Returns:
        <str>: the raw text of the specified file
    """

    if not DATA_FILEPATH.exists():
        print('------------------------------------------')
        print('Note:', DATA_FILEPATH, 'does not exist...')
        # make the subdirectory just in case
        DATA_DIR.mkdir(exist_ok=True)
        # Now download it
        print("Note: Downloading data from:", DATA_SRC_URL)
        print("May take a few minutes...")

        resp = requests.get(DATA_SRC_URL)
        print("Done downloading!")
        txt = resp.text

        print('Saving', len(txt), 'character file to:', DATA_FILEPATH)
        DATA_FILEPATH.write_text(txt)
        print('All done bootstrapping the data!')
        print('--------------------------------')

        # return the raw text
        return txt
    else:
        # the file has been downloaded and exists at
        # DATA_FILEPATH

        # open the file, read the raw text, and return it
        return DATA_FILEPATH.read_text()



