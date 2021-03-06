from dataclasses import dataclass, field


@dataclass(frozen=True)
class Algorithm:
    name: str
    args: list = field(default_factory=list)
