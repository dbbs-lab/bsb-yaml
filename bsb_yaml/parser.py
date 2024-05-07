import yaml
from bsb.config.parsers import ReferenceParser


class YAMLConfigurationParser(ReferenceParser):
    """
    Parser plugin class to parse YAML configuration files.
    """

    data_description = "YAML"
    data_extensions = ("yaml", "yml")

    def from_str(self, filename):
        return yaml.safe_load(filename)

    def load_content(self, stream):
        return yaml.safe_load(stream)

    def generate(self, tree, pretty=False):
        return yaml.dump(tree, indent=None if not pretty else 2)


__plugin__ = YAMLConfigurationParser
