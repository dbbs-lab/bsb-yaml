from bsb import config
from bsb.storage import FileDependencyNode

from .parser import YAMLParser


@config.node
class YamlDependencyNode(FileDependencyNode):
    """
    Configuration dependency node to load yaml files.
    """

    def load_object(self):
        content, encoding = self.file.get_content(check_store=hasattr(self, "scaffold"))
        return YAMLParser().parse(content)[0]
