import yaml
from bsb.config.parsers import ConfigurationParser, ParsesReferences


class YAMLConfigurationParser(ParsesReferences, ConfigurationParser):
    """
    Parser plugin class to parse YAML configuration files.
    """

    data_description = "YAML"
    data_extensions = ("yaml", "yml")

    def parse(self, content, path=None):
        content = yaml.safe_load(content)
        meta = {"path": path}
        return content, meta

    def generate(self, tree, pretty=False):
        return yaml.dump(tree, indent=None if not pretty else 2)


__plugin__ = YAMLConfigurationParser
