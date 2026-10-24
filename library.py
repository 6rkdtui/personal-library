from publication import Publication


class Library:
    def __init__(self) -> None:
        self._publications: list[Publication] = []

    def add_publication(self, publication: Publication) -> None:
        self._publications.append(publication)

    def get_all_publications(self) -> list[Publication]:
        return self._publications.copy()

    def find_by_title(self, query: str) -> list[Publication]:
        query = query.strip().casefold()
        if not query:
            raise ValueError("Запрос не может быть пустым.")

        return [
            publication
            for publication in self._publications
            if query in publication.title.casefold()
        ]
