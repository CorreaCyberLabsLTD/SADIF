from pymongo import MongoClient

from sadif.config.soar_config import SadifConfiguration
from sadif.frameworks_drivers.crawler.crawler_data_import import CrawlerManagerImporter
from sadif.frameworks_drivers.gitmanager import GitManager

if __name__ == "__main__":
    config = SadifConfiguration()

    git_repo_url = config.get_configuration("GIT_REPO_CLIENT_CRAWLER_MONITORING")
    access_token = config.get_configuration("GIT_REPO_TOKEN")
    db_url = config.get_configuration("MONGODB_URL")
    git_manager = GitManager(git_repo_url, access_token)
    db_real = MongoClient(db_url)
    crawler_manager = CrawlerManagerImporter(db_real, git_manager)
    crawler_manager.import_collections(meta_update=True)
