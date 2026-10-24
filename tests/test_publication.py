import pytest
from publication import Publication


def test_publication_strips_title_and_author():
    pub = Publication(
        title="  The Great Gatsby  ", kind="book", author="  F. Scott Fitzgerald  "
    )
    assert pub.title == "The Great Gatsby"
    assert pub.author == "F. Scott Fitzgerald"


def test_publication_rejects_blank_title():
    with pytest.raises(ValueError):
        Publication(title="   ", kind="book", author="F. Scott Fitzgerald")


def test_publication_rejects_blank_author():
    with pytest.raises(ValueError):
        Publication(title="The Great Gatsby", kind="book", author="   ")


def test_publication_rejects_invalid_kind():
    with pytest.raises(ValueError):
        Publication(
            title="The Great Gatsby", kind="magazine", author="F. Scott Fitzgerald"
        )


def test_publication_rejects_invalid_reading_status():
    with pytest.raises(ValueError):
        Publication(
            title="The Great Gatsby",
            kind="book",
            author="F. Scott Fitzgerald",
            reading_status="unknown",
        )


def test_publication_defaults():
    pub = Publication(title="1984", kind="book", author="George Orwell")
    assert pub.series is None
    assert pub.volume_number is None
    assert pub.is_owned is False
    assert pub.reading_status == "not_started"


def test_publication_strips_series():
    pub = Publication(
        title="The Great Gatsby",
        kind="book",
        author="F. Scott Fitzgerald",
        series="  Classic Novels  ",
    )
    assert pub.series == "Classic Novels"


def test_publication_converts_blank_series_to_none():
    pub = Publication(
        title="The Great Gatsby",
        kind="book",
        author="F. Scott Fitzgerald",
        series="   ",
    )
    assert pub.series is None


def test_publication_rejects_zero_volume_number():
    with pytest.raises(ValueError):
        Publication(
            title="The Great Gatsby",
            kind="book",
            author="F. Scott Fitzgerald",
            volume_number=0,
        )


def test_publication_rejects_negative_volume_number():
    with pytest.raises(ValueError):
        Publication(
            title="The Great Gatsby",
            kind="book",
            author="F. Scott Fitzgerald",
            volume_number=-1,
        )


def test_publication_accepts_positive_volume_number():
    pub = Publication(
        title="The Great Gatsby",
        kind="book",
        author="F. Scott Fitzgerald",
        volume_number=1,
    )
    assert pub.volume_number == 1


def test_publication_can_be_finished_without_ownership():
    pub = Publication(
        title="The Great Gatsby",
        kind="book",
        author="F. Scott Fitzgerald",
        is_owned=False,
        reading_status="finished",
    )
    assert pub.is_owned is False
    assert pub.reading_status == "finished"
