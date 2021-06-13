def exercise_5(inputs): # DO NOT CHANGE THIS LINE
    """
    from p2pnetwork.node import Node
    from p2pnetwork.nodeconnection import NodeConnection

    class ExerciseConnection (NodeConnection):
        # Python class constructor
         def __init__(self, main_node, sock, id, host, port):
            super(ExerciseConnection, self).__init__(main_node, sock, id, host, port)



    class ExercisePeer2PeerNode(Node):
        # Python class constructor
        def __init__(self, host, port):
            super(ExercisePeer2PeerNode, self).__init__(host, port, None)

        def outbound_node_connected(self, connected_node):
            print("outbound_node_connected: " + connected_node.id)

        def inbound_node_connected(self, connected_node):
            print("inbound_node_connected: " + connected_node.id)

        def inbound_node_disconnected(self, connected_node):
            print("inbound_node_disconnected: " + connected_node.id)

        def outbound_node_disconnected(self, connected_node):
            print("outbound_node_disconnected: " + connected_node.id)

        def node_message(self, connected_node, data):
            print("node_message from " + connected_node.id + ": " + str(data))

        def node_disconnect_with_outbound_node(self, connected_node):
            print("node wants to disconnect with oher outbound node: " + connected_node.id)

        def node_request_to_stop(self):
            print("node is requested to stop!")

        def create_new_connection(self, connection, id, host, port):
            return ExerciseConnection(self, connection, id, host, port)


    """
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
