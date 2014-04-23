# -*- coding: utf-8 -*-
'''
Created on 15 mar 2014

@author: dominika
'''
from py2neo import node, rel, neo4j
from andip.default import DefaultProvider


class Neo4JProvider(DefaultProvider):
    def __init__(self, url, backoff = None):
        """Provider which browse data in neo4j graph database.

        :param url: database connection url
        :type url: str
        :param backoff: optional backoff
        """

        DefaultProvider.__init__(self, backoff)
        self.url = url
        self.__nodeCounter = 0
        self.conn = None
        self.connect()

    def __isLeaf(self, node):
        """Method which verifies if node is a leaf.

        :param node: checked node
        :type node: tuple
        """
        if len(self.getChildren(node)):
            return False
        return True

    def __getNodeConf(self, origin):
        """Method which gets configuration for given word.

        :param origin: checked node
        :type origin: tuple
        """
        node = origin
        if node is None:
            return None
        result = [node[1]]
        hasParent = True
        pos = None
        resultDict = {}
        value = None
        while hasParent:
            hasParent = False
            parent = self.getParent(node)
            if len(parent):
                node = parent[0]
                result.append(node[1])
                pos = node[1]
                hasParent = True
                if value is None:
                    value = node[1]
                else:
                    resultDict[node[1]] = value
                    value = None
        lemma = resultDict["word"]
        del resultDict["word"]
        return (pos, lemma, resultDict)

    def _get_conf(self, word):
        nodes = self.getNodes(word)
        if len(nodes) == 0:
            raise LookupError("word=%s" % word)
        leaves = [c for c in nodes if self.__isLeaf(c)]
        if len(leaves) == 0:
            raise LookupError("word=%s" % word)
        result = [self.__getNodeConf(leaf) for leaf in leaves]
        return result

    def __getLeaf(self, node, criteria):
        """Method which gets leaf for given criteria and in subtree in which
        the root is given node.
        :param node: subtree root
        :type node: tuple
        :param criteria: criteria of searching
        :type criteria: dict
        """
        if len(criteria) == 0:
            return self.getChildren(node)[0][1]
        for nodeChild in self.getChildren(node):
            if nodeChild[1] in criteria:
                for child in self.getChildren(nodeChild):
                    if child[1] == criteria[nodeChild[1]]:
                        del criteria[nodeChild[1]]
                        return self.__getLeaf(child, criteria)
        return None

    def __getWordNode(self, posNode, word):
        """Method which gets subtree root for given part of speech and
        canonical form of word.
        :param posNode: root which represents part of speech
        :type posNode: tuple
        :param word: word for which node is looked
        :type word: str
        """
        for wNode in self.getChildren(posNode):
            if wNode[1] == "word":
                for node in self.getChildren(wNode):
                    if node[1] == word:
                        return node
        return None

    def _get_word(self, conf):
        pos = conf[0]
        word = conf[1]
        criteria = conf[2]
        nodes = self.getNodes(pos)
        if len(nodes) == 0:
            raise LookupError("conf=%s" % str(conf))
        posNode = nodes[0]
        if posNode is None:
            raise LookupError("conf=%s" % str(conf))
        wordNode = self.__getWordNode(posNode, word)
        if wordNode is None:
            raise LookupError("conf=%s" % str(conf))
        return self.__getLeaf(wordNode, criteria)

    def connect(self):
        """Method which creates connection with database.
        """
        self.conn = neo4j.GraphDatabaseService(self.url)

    def close(self):
        """Method which deletes handler to connection with database.
        """
        self.conn = None

    def node(self, id, data):
        """Method which adds node to graph.

        :param id: identifier of node
        :type id: str
        :param data: name of node
        :type data: str
        """
        self.nodes.append(node(name=data))

    def getNodes(self, criteria):
        """Method which gets node whose name is given in criteria

        :param criteria: name of node
        :type criteria: str
        """
        nodes = neo4j.CypherQuery(self.conn,
        "MATCH (a) WHERE a.name='%s' RETURN a" % criteria)
        result = []
        for elem in nodes.stream():
            node = (elem[0]._id, elem[0]["name"])
            result.append(node)
        return result

    def rel(self, startNode, endNode, data):
        """Method which creates relation between given nodes.

        :param startNode: starting node
        :type startNode: tuple
        :param endNode: ending node
        :type endNode: tuple
        :param data: name of relation
        :type data: string
        """
        rels = [rel(startNode, data, endNode)]
        rels.extend(self.rels)
        self.rels = rels

    def graph(self):
        """Method which initialize empty graph
        """
        self.nodes = []
        self.rels = []

    def commit(self):
        """Method which creates graph -  pushes data into database
        """
        args = []
        args.extend(self.nodes)
        args.extend(self.rels)
        self.conn.create(*args)

    def dropAll(self):
        """Method which deletes all nodes and relations from database
        """
        neo4j.CypherQuery(self.conn,
        "MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r").execute()

    def getParent(self, node):
        """Method which gets node which is parent of given node.

        :param node: child node
        :type node: tuple
        """
        nodes = neo4j.CypherQuery(self.conn,
        "MATCH (a)-[:PARENT]->(b) WHERE ID(a)=%s RETURN b" % node[0])
        result = []
        for elem in nodes.stream():
            node = (elem[0]._id, elem[0]["name"])
            result.append(node)
        return result

    def getChildren(self, node):
        """Method which gets all children of given node.

        :param node: parent node
        :type node: tuple
        """
        nodes = neo4j.CypherQuery(self.conn,
        "MATCH (a)-[:CHILD]->(b) WHERE ID(a)=%s RETURN b" % node[0])
        result = []
        for elem in nodes.stream():
            node = (elem[0]._id, elem[0]["name"])
            result.append(node)
        return result

    def _importDict(self, name, dataDict):
        """Method which imports tree for given part of speech.

        :param name: name of part of speech
        :type name: str
        :param dataDict: data dictionary
        :type dataDict: dict
        """
        self.node(self.__nodeCounter, name)
        nodeId = self.__nodeCounter
        self.__nodeCounter += 1
        for key in dataDict:
            if type(dataDict[key]) is dict:
                childId = self._importDict(key, dataDict[key])
            else:
                valueId = self.__nodeCounter
                self.node(valueId, dataDict[key])
                self.__nodeCounter += 1
                childId = self.__nodeCounter
                self.node(childId, key)
                self.__nodeCounter += 1
                self.rel(childId, valueId, "CHILD")
                self.rel(valueId, childId, "PARENT")
            self.rel(nodeId, childId, "CHILD")
            self.rel(childId, nodeId, "PARENT")
        return nodeId

    def importData(self, dataDict):
        """Methods which imports data into database.

        :param dataDict: data dictionary (the same as for fileProvider)
        :type dataDict: dict

        """
        for elem in dataDict:
            self.__nodeCounter = 0
            self.graph()
            self._importDict(elem, dataDict[elem])
            self.commit()
