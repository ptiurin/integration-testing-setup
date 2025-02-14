from sys import argv
from time import sleep

from firebolt.common.settings import Settings
from firebolt.model.engine import Engine
from firebolt.service.manager import ResourceManager
from firebolt.service.types import EngineStatusSummary

WAIT_SLEEP_SECONDS = 5


def engine_wait_stop(engine: Engine) -> None:
    engine.stop()
    while (
        engine.current_status_summary
        != EngineStatusSummary.ENGINE_STATUS_SUMMARY_STOPPED
    ):
        sleep(WAIT_SLEEP_SECONDS)
        engine = engine.get_latest()


def engine_wait_delete(engine: Engine, rm: ResourceManager) -> None:
    engine.delete()
    try:
        while rm.engines.get_by_name(engine.name):
            sleep(WAIT_SLEEP_SECONDS)
    except RuntimeError:  # Happend when we are unable to find the engine
        pass


if __name__ == "__main__":
    rm = ResourceManager(Settings())

    if len(argv) < 2:
        raise RuntimeError("database name argument  should be provided")
    database_name = argv[1]
    engine_name = database_name
    engine = rm.engines.get_by_name(engine_name)
    engine_wait_stop(engine)
    engine_wait_delete(engine, rm)
    rm.databases.get_by_name(database_name).delete()
