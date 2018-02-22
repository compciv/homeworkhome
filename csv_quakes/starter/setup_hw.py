"""
setup_hw.py

How to use:

    $  python setup_hw.py

Downloads files needed for this project.

    ├── data_helper.py
    ├── format_helper.py
    ├── scraper.py
    └── tests/
        ├── test_calc_years_diff.py
        ├── test_make_absolute_url.py
        ├── test_scraper.py
        ├── test_txdate_to_iso.py
        └── test_wrangle_inmate_data.py

##########################################################
"""

from pathlib import Path
import requests
from time import sleep
from urllib.parse import urljoin

GH_DOMAIN = 'https://compciv.github.io'
GH_SUBDIR = 'homeworkhome'
GH_REPO = 'csv_quakes'

GH_BASEURL = '/'.join([GH_DOMAIN , GH_SUBDIR, GH_REPO])

SRC_URLPATHS = [
    Path('starter', 'aggy.py'),
    Path('starter', 'sorty.py'),
    Path('tests','test_aggy.py'),
    Path('tests', 'test_sorty.py'),
    Path('data', 'usgs-quakes.csv'),
]


def get_and_save_url(src_url, dest_fname):
    dest_fname = Path(dest_fname)
    ## now download
    thebytes = get_url(src_url)
    dest_fname.write_bytes()
    # return Path object
    return dest_fname

def get_url(url):
    """
    Wrapper around requests.get()

    Arguments:
        url: <str>, the URL for something on the web

    Returns:
        <bytes>: Uses the Request.Response.bytes property --
           instead of the .text property, so that the
           downloaded data is returned as <bytes> and not <str>
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError("The server at", url, "had a status code of", resp.status_code)
    else:
        return resp.content


def does_file_exist(fname):
    if fname.exists():
        # check to see file is empty
        bsize = dest_fname.stat().st_size
        if bsize > 0:
            # if not, ask to overwrite
            msg = "{n} exists; Overwrite? (Y/N)".format(n=fname)
            omsg = input(msg).strip().upper()
            if omsg != 'Y':
                return True  # return True -- i.e. fname exists and don't overwrite
    # otherwise we return False, i.e. fname should be written to
    return False

##################################

if __name__ == '__main__':
    """
    This routine defines what is executed when this script is run from
    the command-line, i.e.

        $ python setup_hw.py

    """
    print("********************************************")
    print("This script downloads a bunch of files from:")
    print(GH_BASEURL, "\n")
    print("And saves them to the current working directory, which is:")
    cwd = Path(__file__).parent.absolute()
    print(cwd, '\n')

    sleep(1)

    for pth in SRC_URLPATHS:
        dest_fname = cwd.joinpath(pth)

        # check file existence
        if not does_file_exist(dest_fname):
            url = urljoin(GH_BASEURL, str(pth))

            # download and save
            print("Downloading:", url)
            get_and_save_url(url, dest_fname)
            print("Wrote to:", dest_Fname)

