#!/usr/bin/env python
# coding:utf-8

import os
import sys
import time
from typing import List

import grpc
from akari_client import AkariClient
from akari_client.position import Positions

sys.path.append(os.path.join(os.path.dirname(__file__), "lib/grpc"))
import motion_server_pb2
import motion_server_pb2_grpc

motion_server_port = "localhost:50055"
channel = grpc.insecure_channel(motion_server_port)
stub = motion_server_pb2_grpc.MotionServerServiceStub(channel)
motion_input_interval = 0.1
motion_list: List[str] = [
    "nod",
    "agree",
    "bow",
    "swing",
    "happy",
    "lough",
    "depressed",
    "amazed",
    "sleep",
    "lookup",
    "lookaround",
]


def main():
    motion_index: int = 0
    with AkariClient() as akari:
        # m5と通信するクラスを呼び出す
        m5 = akari.m5stack
        last_time = time.time()
        m5.set_display_text(text=motion_list[motion_index], size=5)
        m5.set_display_text(
            text="prev",
            pos_x=Positions.LEFT,
            pos_y=Positions.BOTTOM,
            size=3,
            refresh=False,
        )
        m5.set_display_text(
            text="send",
            pos_x=Positions.CENTER,
            pos_y=Positions.BOTTOM,
            size=3,
            refresh=False,
        )
        m5.set_display_text(
            text="next",
            pos_x=Positions.RIGHT,
            pos_y=Positions.BOTTOM,
            size=3,
            refresh=False,
        )
        while True:
            data = m5.get()
            if data["button_a"] and (time.time() - last_time >= motion_input_interval):
                motion_index -= 1
                if motion_index < 0:
                    motion_index = len(motion_list) - 1
                # 行の表示をリフレッシュする
                m5.set_display_text(text="                  \n", size=5, refresh=False)
                m5.set_display_text(
                    text=motion_list[motion_index], size=5, refresh=False
                )

                last_time = time.time()
            if data["button_b"] and (time.time() - last_time >= motion_input_interval):
                stub.SetMotion(
                    motion_server_pb2.SetMotionRequest(
                        name=motion_list[motion_index],
                        priority=3,
                        repeat=False,
                        clear=True,
                    )
                )
                last_time = time.time()
            if data["button_c"] and (time.time() - last_time >= motion_input_interval):
                motion_index += 1
                if motion_index > len(motion_list) - 1:
                    motion_index = 0
                # 行の表示をリフレッシュする
                m5.set_display_text(text="                  \n", size=5, refresh=False)
                m5.set_display_text(
                    text=motion_list[motion_index], size=5, refresh=False
                )
                last_time = time.time()


if __name__ == "__main__":
    main()
