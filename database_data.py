import sqlite3


class Database:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def create_database(self):
        conn = sqlite3.connect(self.database_name)
        conn.commit()
        conn.close()

    def create_table(self):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()

        # Check to see if the table was already created
        try:
            cur.execute(f"""CREATE TABLE {self.table_name} (
                            date date,
                            rain_h float,
                            temp_c float,
                            sun_h float,
                            sunrise time,
                            sunset time
                            )""")
        except sqlite3.OperationalError:
            pass
        else:
            conn.commit()
        finally:
            conn.close()

    def record_data(self, date, rain, temp, sun, sunrise, sunset):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {self.table_name} VALUES(:date, :rain_h, :temp_c, :sun_h, :sunrise, :sunset)",
                    {
                        "date": date,
                        "rain_h": rain,
                        "temp_c": temp,
                        "sun_h": sun,
                        "sunrise": sunrise,
                        "sunset": sunset
                    })
        conn.commit()
        conn.close()
