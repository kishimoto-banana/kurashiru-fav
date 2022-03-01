from dataclasses import dataclass


@dataclass
class Recipe:
    url: str
    title: str
    image_url: str
