#!/usr/bin/env python
# coding:utf-8

import os
import queue
import sys
import threading
import time
from enum import Enum

sys.path.append(os.path.join(os.path.dirname(__file__), "grpc"))
import motion_server_pb2
import motion_server_pb2_grpc
from akari_client import AkariClient


class Command(Enum):
    MOVE = 1
    VEL = 2
    ACC = 3
    WAIT = 4


class MotionServer(motion_server_pb2_grpc.MotionServerServiceServicer):
    def __init__(self):
        akari = AkariClient()
        self.joints = akari.joints
        self.joints.enable_all_servo()
        self.joints.set_joint_velocities(pan=8, tilt=8)
        self.joints.move_joint_positions(sync=True, pan=0, tilt=0.3)
        self.motion_queue = queue.Queue()
        self.motion_thread = threading.Thread(target=self.player)
        self.start_time = time.time()
        self.interval: float = 0
        self.repeat: bool = False
        self.cur_motion: str = ""
        self.cur_priority: int = 0
        self.motion_thread.start()

    def __exit__(self):
        self.motion_thread.join()
        self.repeat = False
        while not self.motion_queue.empty():
            self.motion_queue.get()

    def player(self):
        while True:
            if time.time() - self.start_time >= self.interval:
                command, self.interval, *args = self.motion_queue.get()
                self.start_time = time.time()
                if command == Command.MOVE:
                    self.joints.move_joint_positions(
                        pan=args[0], tilt=args[1], sync=args[2]
                    )
                elif command == Command.VEL:
                    self.joints.set_joint_velocities(pan=args[0], tilt=args[1])
                elif command == Command.ACC:
                    self.joints.set_joint_accelerations(pan=args[0], tilt=args[1])
                elif Command.WAIT:
                    pass
            if self.motion_queue.empty():
                if self.repeat:
                    print("Repeat motion: " + self.cur_motion)
                    self.play_motion(self.cur_motion)
                self.cur_priority = 0

    def motion_nod(self):
        self.motion_queue.put((Command.VEL, 0, 9, 9))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.1, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.1, True))
        self.motion_queue.put((Command.MOVE, 1, 0, 0.3, True))

    def motion_agree(self):
        self.motion_queue.put((Command.VEL, 0, 9, 9))
        self.motion_queue.put((Command.MOVE, 0.5, 0, -0.1, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_bow(self):
        self.motion_queue.put((Command.VEL, 0, 5, 5))
        self.motion_queue.put((Command.MOVE, 1, 0, -0.4, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_swing(self):
        self.motion_queue.put((Command.VEL, 0, 9, 9))
        self.motion_queue.put((Command.MOVE, 0, -0.3, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0.3, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, -0.3, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0.3, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_happy(self):
        self.motion_queue.put((Command.VEL, 0, 9, 11))
        self.motion_queue.put((Command.MOVE, 0, 0.1, -0.2, True))
        self.motion_queue.put((Command.MOVE, 0, 0.1, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0.1, -0.2, True))
        self.motion_queue.put((Command.MOVE, 0, 0.1, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, -0.1, -0.2, True))
        self.motion_queue.put((Command.MOVE, 0, -0.1, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, -0.1, -0.2, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_lough(self):
        self.motion_queue.put((Command.VEL, 0, 8, 8))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.1, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.1, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.1, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_depressed(self):
        self.motion_queue.put((Command.VEL, 0, 4, 4))
        self.motion_queue.put((Command.MOVE, 2, 0.0, -0.3, True))
        self.motion_queue.put((Command.VEL, 0, 5, 5))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_amazed(self):
        self.motion_queue.put((Command.VEL, 0, 6, 6))
        self.motion_queue.put((Command.MOVE, 0.7, 0.2, -0.4, True))
        self.motion_queue.put((Command.MOVE, 0, -0.2, -0.4, True))
        self.motion_queue.put((Command.MOVE, 0, 0.2, -0.4, True))
        self.motion_queue.put((Command.MOVE, 0, -0.2, -0.4, True))
        self.motion_queue.put((Command.MOVE, 1, 0.2, -0.4, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_sleep(self):
        self.motion_queue.put((Command.VEL, 0, 1.25, 3))
        self.motion_queue.put((Command.MOVE, 4, 0.3, -0.4, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_lookup(self):
        self.motion_queue.put((Command.VEL, 0, 1.25, 3))
        self.motion_queue.put((Command.MOVE, 4, 0.3, 0.5, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def motion_look_around(self):
        self.motion_queue.put((Command.VEL, 0, 4, 4))
        self.motion_queue.put((Command.MOVE, 4, 0.95, 0, True))
        self.motion_queue.put((Command.MOVE, 4, -0.95, 0, True))
        self.motion_queue.put((Command.MOVE, 0, 0, 0.3, True))

    def play_motion(self, name: str):
        if name == "nod":
            self.motion_nod()
        elif name == "agree":
            self.motion_agree()
        elif name == "bow":
            self.motion_bow()
        elif name == "swing":
            self.motion_swing()
        elif name == "happy":
            self.motion_happy()
        elif name == "lough":
            self.motion_lough()
        elif name == "depressed":
            self.motion_depressed()
        elif name == "amazed":
            self.motion_amazed()
        elif name == "sleep":
            self.motion_sleep()
        elif name == "lookup":
            self.motion_lookup()
        elif name == "lookaround":
            self.motion_look_around()
        else:
            return False
        print("Set motion: " + name)
        return True

    def SetMotion(self, request: motion_server_pb2.SetMotionRequest(), context):
        priority = 0
        repeat = False
        print(f"received: {request.name}")
        if request.priority is not None:
            priority = request.priority
        if request.repeat is not None:
            repeat = request.repeat
        if request.clear is not None:
            if request.clear:
                while not self.motion_queue.empty():
                    self.motion_queue.get()
                self.interval = 0
        if priority >= self.cur_priority:
            self.cur_priority = priority
            self.cur_motion = request.name
            self.repeat = repeat
            self.play_motion(request.name)
        return motion_server_pb2.SetMotionReply(success=True)

    def StopRepeat(self, request: motion_server_pb2.StopRepeatRequest(), context):
        priority = 0
        if request.priority is not None:
            priority = request.priority
        if priority >= self.cur_priority:
            self.repeat = False
        return motion_server_pb2.StopRepeatReply(success=True)

    def ClearMotion(self, request: motion_server_pb2.ClearMotionRequest(), context):
        priority = 0
        if request.priority is not None:
            priority = request.priority
        if priority >= self.cur_priority:
            self.repeat = False
            while not self.motion_queue.empty():
                self.motion_queue.get()
            print("Clear motion queue")
        return motion_server_pb2.ClearMotionReply(success=True)

    def SetWait(self, request: motion_server_pb2.SetWaitRequest(), context):
        priority = 3
        if request.priority is not None:
            priority = request.priority
        if request.clear is not None:
            if request.clear:
                while not self.motion_queue.empty():
                    self.motion_queue.get()
                self.interval = 0
        if priority >= self.cur_priority:
            self.cur_priority = priority
            self.motion_queue.put((Command.WAIT, request.time))
            print("Set wait: " + str(request.time) + "[s]")
        return motion_server_pb2.SetWaitReply(success=True)
