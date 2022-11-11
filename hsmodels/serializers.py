import warnings
from typing import IO, Optional

from rdflib.graph import Graph
from rdflib.namespace import XSD
from rdflib.plugins.shared.jsonld.util import json
from rdflib.plugins.serializers.jsonld import JsonLDSerializer, from_rdf

__all__ = ["PrettyJsonLDSerializer", "from_rdf"]


PLAIN_LITERAL_TYPES = {XSD.boolean, XSD.integer, XSD.double, XSD.string}


class PrettyJsonLDSerializer(JsonLDSerializer):
    def __init__(self, store: Graph):
        super(PrettyJsonLDSerializer, self).__init__(store)

    def serialize(
        self,
        stream: IO[bytes],
        base: Optional[str] = None,
        encoding: Optional[str] = None,
        **kwargs,
    ):
        # TODO: docstring w. args and return value
        encoding = encoding or "utf-8"
        if encoding not in ("utf-8", "utf-16"):
            warnings.warn(
                "JSON should be encoded as unicode. " f"Given encoding was: {encoding}"
            )

        context_data = kwargs.get("context")
        use_native_types = (kwargs.get("use_native_types", False),)
        use_rdf_type = kwargs.get("use_rdf_type", False)
        auto_compact = kwargs.get("auto_compact", False)

        indent = kwargs.get("indent", 2)
        separators = kwargs.get("separators", (",", ": "))
        sort_keys = kwargs.get("sort_keys", True)
        ensure_ascii = kwargs.get("ensure_ascii", False)

        obj = from_rdf(
            self.store,
            context_data,
            base,
            use_native_types,
            use_rdf_type,
            auto_compact=auto_compact,
        )

        '''Here is where the compaction takes place!'''
        distribute_nodes(obj)

        data = json.dumps(
            obj,
            indent=indent,
            separators=separators,
            sort_keys=sort_keys,
            ensure_ascii=ensure_ascii,
        )

        stream.write(data.encode(encoding, "replace"))


def distribute_nodes(jld):
    # group nodes to be distributed into roots
    # nodes are identified by a dictionary with {'@id': "_:N..."}
    nodes_by_id = {d.pop('@id'): d for d in jld['@graph'] if d['@id'].startswith("_:N")}
    roots = [d for d in jld['@graph'] if '@id' in d and not d['@id'].startswith("_:N")]

    # code for walking dictionaries and lists to replace node identifiers with the nodes
    def is_node_id(d) -> bool:
        if isinstance(d, dict):
            if "@id" in d and d["@id"].startswith("_:N"):
                return True
        return False

    def get_node(d: dict):
        return nodes_by_id[d["@id"]]

    def parse_list(l: list):
        nodes = []
        for item in l:
            if is_node_id(item):
                nodes.append((item, get_node(item)))
            if isinstance(item, list):
                parse_list(item)
            if isinstance(item, dict):
                parse_dict(item)
        for node in nodes:
            l.remove(node[0])
            l.append(node[1])

    def parse_dict(d: dict):
        nodes = []
        for key, value in d.items():
            if is_node_id(value):
                nodes.append((key, get_node(value)))
            if isinstance(value, list):
                parse_list(value)
            if isinstance(value, dict):
                parse_dict(value)
        for node in nodes:
            d[node[0]] = node[1]
    # run the node replacements for each root
    for d in roots:
        parse_dict(d)


