from dataclasses import dataclass


@dataclass
class Publication:
    title: str
    kind: str
    author: str
    series: str | None = None
    volume_number: int | None = None
    is_owned: bool = False
    reading_status: str = (
        "not_started"  # Options: "not_started", "in_progress", "completed"
    )

    def __post_init__(self):
        self.title = self.title.strip()
        if not self.title:
            raise ValueError("Название не может быть пустым.")

        self.author = self.author.strip()
        if not self.author:
            raise ValueError("Поле 'Автор' не может быть пустым.")

        if self.kind not in ("book", "comic"):
            raise ValueError("Недопустимый тип публикации.")

        if self.reading_status not in ("not_started", "reading", "finished"):
            raise ValueError("Недопустимый статус чтения.")

        if self.volume_number is not None and self.volume_number <= 0:
            raise ValueError("Номер тома должен быть положительным числом.")

        if self.series is not None:
            self.series = self.series.strip()
            if not self.series:
                self.series = None
