from os import environ

from firebolt.common.settings import Settings
from firebolt.service.manager import ResourceManager

if __name__ == "__main__":
    rm = ResourceManager(Settings())

    if "db_name" not in environ:
        raise RuntimeError("db_name environment variable should be defined")
    database_name = environ.get("db_name")
    engine_name = database_name
    database = rm.databases.get_by_name(database_name)
    engine = rm.engines.create(engine_name, scale=1, spec="m5d.4xlarge")
    engine.attach_to_database(database, True)
    engine.start()
    print(engine.name, engine.endpoint)
