# pylint: disable=import-error
import os

from cassandra.cluster import Cluster
from cassandra.policies import TokenAwarePolicy, RoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider

from cassandra import ConsistencyLevel, ReadTimeout
from cassandra.query import (
    BatchStatement,
    PreparedStatement,
    SimpleStatement,
    dict_factory,
)

CQLVERSION = "3.4.4"


class Cassandra:

    cluster = None
    session = None
    logger = None

    def __init__(self, nodes, user, pwd, port=9042, logger=None):
        """
            Build a cluster connection cassandra cluster with auth provider
            :param nodes: nodes list to connect
            :param user: username
            :param pwd: password for username
            :param port: port for connection Default is 9042
        """
        self.logger = logger
        auth_provider = PlainTextAuthProvider(username=user, password=pwd)
        self.cluster = Cluster(
            nodes,
            port=port,
            cql_version=CQLVERSION,
            auth_provider=auth_provider,
            load_balancing_policy=TokenAwarePolicy(RoundRobinPolicy()),
        )

    def connect(self):
        """
            Start session with cluster. Set the row_factory to "dict". If session already started, only change keyspace.
            :param keyspace: Keyspace name for the current session
        """
        if self.session is None:
            self.session = self.cluster.connect()
            self.session.row_factory = dict_factory
        return self.session

    def execute(self, statements):
        for i in statements:
            stmt = i.strip()
            if stmt != '':
                self.logger.info('Executing "' + stmt + '"')
                self.session.execute(stmt)