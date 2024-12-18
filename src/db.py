from decouple import config
from prisma import Prisma
from prisma.types import DatasourceOverride

DATABASE = None


def application_database_connection():
    global DATABASE  # pylint: disable=global-statement

    if DATABASE is None:
        database_url = config("DATABASE_URL")
        assert isinstance(database_url, str)

        # prisma datasource, not our datasource
        datasource = DatasourceOverride(url=database_url)
        DATABASE = Prisma(use_dotenv=False, datasource=datasource)
        DATABASE.connect()
    return DATABASE
