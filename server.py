#!/usr/bin/env python
# coding:utf-8

import os
import sys
import time
from concurrent import futures

import grpc
from lib.motions import MotionServer

sys.path.append(os.path.join(os.path.dirname(__file__), "lib/grpc"))
import motion_server_pb2_grpc


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    motion_server_pb2_grpc.add_MotionServerServiceServicer_to_server(
        MotionServer(), server
    )
    port = "50055"
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
