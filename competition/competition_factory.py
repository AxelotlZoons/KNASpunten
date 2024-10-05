from .FieCompetition import FieCompetition
from .FtlCompetition import FtlCompetition


def competition_factory(url):

    platform_classes = {
        "fie": FieCompetition,
        "ftl": FtlCompetition
    }

    platform = None
    if "fie.org" in url:
        platform = "fie"
    if "fencingtimelive.com" in url:
        platform = "ftl"

    if platform in platform_classes:
        return platform_classes[platform](url)  # Instantiate the appropriate class
    else:
        raise ValueError(f"Unsupported platform: {platform}")
