# datafoo.py

DATA_FILENAME = 'usgs-quakes.csv'
SAMPLE_FILENAME = 'sample-quakes.csv'

def get_quakes_data(filename):
    """
    Returns:
        <list> of <dict>s
    """
    quakes = []
    records = load_quake_data_file(filename)
    for row in records:
        q = extract_quake(row)
        quakes.append(q)

    return quakes



######################################
def load_quake_records(filename):
    """
    Returns:
        <list> of <dict>s
    """


def extract_quake(record):
    """
    Returns:
        <dict>
    """






