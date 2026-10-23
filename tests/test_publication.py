import pytest
from publication import Publication

def test_publication_strips_title_and_author():
    pub = Publication(title="  The Great Gatsby  ", kind="book", author="  F. Scott Fitzgerald  ")
    assert pub.title == "The Great Gatsby"
    assert pub.author == "F. Scott Fitzgerald"