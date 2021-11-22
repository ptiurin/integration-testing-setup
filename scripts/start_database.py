from time import time

from firebolt.common.settings import Settings
from firebolt.service.manager import ResourceManager

if __name__ == "__main__":
    rm = ResourceManager(Settings())
    database_name = f"integration_testing_{int(time())}"
    rm.databases.create(database_name)
    print(database_name)
