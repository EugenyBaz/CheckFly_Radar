from app.db.database import get_connection


def seed_airport_groups() -> None:
    connection = get_connection()

    cursor = connection.cursor()

    # GROUPS

    airport_groups = [
        ("SPB", "Saint Petersburg"),
        ("MOSCOW", "Moscow Airports"),
        ("TURKEY_COAST", "Turkey Coast"),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO airport_groups (
            code,
            name
        )
        VALUES (?, ?)
        """,
        airport_groups,
    )

    # GROUP MEMBERS

    airport_group_members = [
        ("SPB", "LED"),
        ("MOSCOW", "SVO"),
        ("MOSCOW", "VKO"),
        ("MOSCOW", "DME"),
        ("TURKEY_COAST", "AYT"),
        ("TURKEY_COAST", "GZP"),
    ]

    airport_aliases = [
        ("москва", "MOSCOW"),
        ("moscow", "MOSCOW"),
        ("спб", "SPB"),
        ("питер", "SPB"),
        ("санкт-петербург", "SPB"),
        ("турция", "TURKEY_COAST"),
        ("анталия", "TURKEY_COAST"),
        ("газипаша", "TURKEY_COAST"),
    ]

    cursor.executemany(
        """ INSERT OR IGNORE INTO airport_group_aliases ( alias, group_code ) VALUES (?, ?) """,
        airport_aliases,
    )

    cursor.executemany(
        """ INSERT OR IGNORE INTO airport_group_members ( group_code, airport_code ) VALUES (?, ?) """,
        airport_group_members,
    )

    connection.commit()

    connection.close()

    print("Airport groups seeded.")
