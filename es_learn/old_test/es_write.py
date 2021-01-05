type_dict = {
    "text": {"type": "text"},
    "keyword": {"type": "keyword"},
    "ip": {"type": "ip"},
    "long": {"type": "long"},
    "double": {"type": "double"},
    "boolean": {"type": "boolean"},
    "integer": {"type": "integer"}

}
mappings = {
    "web_log": {
        "_source": {
            "enabled": True
        },
        "properties": {
            "remote_addr": type_dict["ip"],
            "time_local": {
                "type": "date",
                "format": "dd/MMM/yyyy:HH:mm:ss Z"

            },
            "body_bytes_sent": type_dict["long"],
            "request_length": type_dict["long"],
            "bytes_sent": type_dict["long"],
            "request_time": type_dict["double"],
            "idss_action": type_dict["integer"],
        }
    }
}
template = {
    "index_patterns": ["web_bubble_index*"],
    "settings": {
        "index": {
            "refresh_interval": "30s",
            "number_of_shards": "12",
            "number_of_replicas": "2"
        },
        "translog": {
            "sync_interval": "30s",
            "durability": "async",
            "flush_threshold_size": "1000mb"
        }
    },
    "mappings": mappings

}
from elasticsearch_dsl import connections
from elasticsearch.client import IndicesClient


class BaseES():
    def __init__(self):
        self.es = connections.create_connection(hosts="127.0.0.1:9200", timeout=60, http_compress=True,
                                                sniff_on_connection_fail=True)


class BaseTemplate():
    def __init__(self):
        self.es = BaseES().es

    def set_template(self, name, body):
        IndicesClient(self.es).put_mapping(name, body)

    def get_template(self, name):
        IndicesClient(self.es).get_template(name)

    def delete_template(self, name):
        IndicesClient(self.es).delete_template(name)

    def create_data_template(self):
        template = {

        }
