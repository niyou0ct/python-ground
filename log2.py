import yaml
from logging import config, getLogger
config.dictConfig(yaml.load(open("logconf.yml", encoding='UTF-8').read()))
logger = getLogger(__name__)
logger.error("エラーが発生しました")
