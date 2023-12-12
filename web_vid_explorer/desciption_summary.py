from dataclasses import dataclass

@dataclass
class DescriptionSummary:
    total_count: int
    unique_count: int
    most_common_phrase: str
    freq_of_most_common_phrase: str
