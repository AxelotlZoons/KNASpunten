from competition.competition_factory import competition_factory


def main():
    url = "https://fencingtimelive.com/events/results/468F1734BD484EB0B1A3D7F9C478BFA2"
    competition = competition_factory(url)
    competition.calculate_percentage()


if __name__ == '__main__':
    main()