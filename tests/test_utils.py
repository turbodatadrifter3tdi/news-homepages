from pathlib import Path

import pytz

from newshomepages import utils


def test_safe_ia_handle():
    """Test safe_ia_handle."""
    assert utils.safe_ia_handle("_leadingunderscore") == "leadingunderscore"
    assert utils.safe_ia_handle("CamelCase") == "camelcase"
    try:
        utils.safe_ia_handle("white space")
    except ValueError:
        pass


def test_write_csv(tmpdir):
    """Test write_csv."""
    p = Path(tmpdir / "write_csv")
    utils.write_csv([{"foo": "bar"}], p)
    utils.write_csv([{"foo": "bar"}], p, verbose=False)


def test_write_json(tmpdir):
    """Test write_json."""
    p = Path(tmpdir / "write_json")
    utils.write_json({"foo": "bar"}, p)
    utils.write_json([{"foo": "bar"}], p)
    utils.write_json({"foo": "bar"}, p, indent=4)
    utils.write_json({"foo": "bar"}, p, verbose=False)


def test_sites():
    """Test sites utils."""
    # Read in the list
    site_list = utils.get_site_list()
    assert len(site_list) > 0
    assert utils.get_site("latimes")["name"] == "Los Angeles Times"
    unique_handles = {i["handle"].lower() for i in site_list}
    assert len(site_list) == len(unique_handles)

    # Make sure all the required fields are filled in
    site_df = utils.get_site_df()
    assert not site_df.handle.isnull().any()
    assert not site_df.url.isnull().any()
    assert not site_df.name.isnull().any()
    assert not site_df.location.isnull().any()
    assert not site_df.timezone.isnull().any()
    assert not site_df.country.isnull().any()

    # Test timezones
    for s in site_list:
        pytz.timezone(s["timezone"])


def test_bundles():
    """Test bundles utils."""
    # Get bundles
    bundle_list = utils.get_bundle_list()
    assert len(bundle_list) > 0

    # Test timezones
    for b in bundle_list:
        pytz.timezone(b["timezone"])

    # Pull on by name
    assert utils.get_bundle("socal")["name"] == "Southern California"


def test_javascript():
    """Test javascript utils."""
    assert utils.get_javascript("latimes") is not None
    assert utils.get_javascript("foobar") is None


def test_numoji():
    """Test numoji util."""
    assert utils.numoji("1") == "1️⃣"


def test_url_parse():
    """Test the URL parser."""
    utils.parse_archive_url(
        "https://archive.org/download/100reporters-2022/100reporters-2022-07-08T23:55:17.494439-04:00.hyperlinks.json"
    )
    utils.parse_archive_url(
        "https://archive.org/download/appalachia100-2022/appalachia100-2022-07-29T19:59:50.561493-04:00.jpg"
    )


# def test_get_extract():
#    """Test the method to pull in an extract CSV."""
#    utils.get_extract_df("sites.csv")


# def test_get_url():
#    """Test utils for getting data off the web."""
#    utils.get_json_url(
#        "https://archive.org/download/signalcleveland-2022/signalcleveland-2022-11-17T02%3A50%3A58.280867-05%3A00.wayback.json"
#    )


def test_get_local_time():
    """Test method to get the local time."""
    utils.get_local_time(utils.get_site("latimes"))
    utils.get_local_time(utils.get_bundle("us-national"))
