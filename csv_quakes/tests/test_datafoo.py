# test_datafoo.py

import datafoo as xyz


def test_load_quake_records():
    data_filename = xyz.SAMPLE_FILENAME
    records = xyz.load_quake_records(data_filename)

    # load_quakes_file() returns a list
    assert type(records) is list

    # make sure every thing in the list is a dict
    assert all(type(d) is dict for d in records)

    # verify the count
    assert len(records) is 10

