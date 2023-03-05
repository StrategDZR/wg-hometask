from dataclasses import dataclass


@dataclass
class WebsiteInfo:
    name: str
    popularity: int
    frontend: str
    backend: str
