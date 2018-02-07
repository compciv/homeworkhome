from pathlib import Path
import requests

###
# This is functionally the same as data_helper.py, but it
# uses the fancy pathlib library to do file operations and paths
# ...just here for educational purposes...
###

# a static/archived copy of Texas's "Offenders on Death Row"
DATA_SRC_URL = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
# the filename of the saved page
DATA_FILEPATH = Path('tx-deathrow-webpage.html')

def fetch_data_from_web():
    """
    This is meant to only run once. It fetches the page and
    saves it to a specified filepath. Basically, a function
    that guarantees that the working directory has what it needs
    (a copy of the data) for the other functions to use.

    The upshot is that checker.py doesn't have to worry about
     making a web request (i.e downloading)

    Args:
        None
    Returns:
        <str>: The name of the file saved to
    """
    print("Requesting:", DATA_SRC_URL)
    resp = requests.get(DATA_SRC_URL)
    if resp.status_code != 200:
        errmsg = 'Did not get an OK status when requesting: {u}'.format(u= DATA_SRC_URL)
        raise RuntimeError(errmsg)
    else:
        print("Requested page successfully.")
        txt = resp.text
        print("Length of text:", len(txt))
        print('Saving to:', DATA_FILEPATH)
        DATA_FILEPATH.write_text(txt)
        return str(DATA_FILEPATH) # a Path object is technically not a string...

def get_html():
    """
    Reads the file at DATA_FILEPATH and returns it as a string

    The upshot is that checker.py doesn't have to worry about
       either downloading a file, or opening an existing file on disk.

    Pre-reqs:
        Expects DATA_FILEPATH to exist. If not, throws an error.
    Args:
        None
    Returns:
        <str>: the contents of the file at DATA_FILEPATH as a big text string
    """

    if not DATA_FILEPATH.exists():
        fetch_data_from_web()
    return DATA_FILEPATH.read_text()




