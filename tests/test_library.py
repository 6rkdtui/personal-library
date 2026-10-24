import pytest
from library import Library
from publication import Publication


def test_library_is_initially_empty():
    library = Library()
    assert library.get_all_publications() == []


def test_library_adds_publication():
    library = Library()
    publication = Publication(
        title="The Great Gatsby", kind="book", author="F. Scott Fitzgerald"
    )
    library.add_publication(publication)
    assert library.get_all_publications() == [publication]


def test_libraries_have_independent_collections():
    library1 = Library()
    library2 = Library()
    publication = Publication(
        title="The Great Gatsby", kind="book", author="F. Scott Fitzgerald"
    )
    library1.add_publication(publication)
    assert len(library2.get_all_publications()) == 0
    assert library1.get_all_publications() == [publication]


def test_get_all_publications_returns_list_copy():
    library = Library()
    publication = Publication(
        title="The Great Gatsby", kind="book", author="F. Scott Fitzgerald"
    )
    library.add_publication(publication)
    publications_copy = library.get_all_publications()
    publications_copy.clear()
    assert library.get_all_publications() == [publication]


def test_find_by_title_matches_substring():
    library = Library()
    publication1 = Publication(
        title="The Great Gatsby", kind="book", author="F. Scott Fitzgerald"
    )
    publication2 = Publication(
        title="Great Expectations", kind="book", author="Charles Dickens"
    )
    library.add_publication(publication1)
    library.add_publication(publication2)

    results = library.find_by_title("great")
    assert results == [publication1, publication2]


def test_find_by_title_ignores_case_and_outer_spaces():
    library = Library()
    publication = Publication(
        title="The Great Gatsby", kind="book", author="F. Scott Fitzgerald"
    )
    library.add_publication(publication)

    results = library.find_by_title("  gReAt  ")
    assert results == [publication]


def test_find_by_title_returns_empty_list_when_no_matches():
    library = Library()
    publication = Publication(
        title="The Great Gatsby", kind="book", author="F. Scott Fitzgerald"
    )
    library.add_publication(publication)

    results = library.find_by_title("nonexistent")
    assert results == []


def test_find_by_title_rejects_blank_query():
    library = Library()

    with pytest.raises(ValueError, match="Запрос не может быть пустым"):
        library.find_by_title("   ")
