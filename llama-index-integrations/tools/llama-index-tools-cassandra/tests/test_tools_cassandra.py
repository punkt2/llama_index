from llama_index.core.tools.tool_spec.base import BaseToolSpec
from llama_index.tools.cassandra.base import CassandraDatabaseToolSpec


def test_class() -> None:
    names_of_base_classes = [b.__name__ for b in CassandraDatabaseToolSpec.__mro__]
    assert BaseToolSpec.__name__ in names_of_base_classes