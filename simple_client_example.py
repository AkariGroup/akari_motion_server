#!/usr/bin/env python
# coding:utf-8

import os
import sys
import time

import grpc

sys.path.append(os.path.join(os.path.dirname(__file__), "lib/grpc"))
import motion_server_pb2
import motion_server_pb2_grpc

motion_server_port = "localhost:50055"
channel = grpc.insecure_channel(motion_server_port)
stub = motion_server_pb2_grpc.MotionServerServiceStub(channel)


def main():
    motion = "bow"
    print(f"1.Send motion {motion}")
    reply = stub.SetMotion(motion_server_pb2.SetMotionRequest(name=motion, priority=3))
    time.sleep(3)

    motion = "nod"
    print(f"2.Send motion {motion} with repeat")
    reply = stub.SetMotion(
        motion_server_pb2.SetMotionRequest(name=motion, priority=3, repeat=True)
    )
    time.sleep(3)

    print("3.Clear motion")
    reply = stub.ClearMotion(motion_server_pb2.ClearMotionRequest())
    time.sleep(3)

    motion = "swing"
    print(f"4.Send motion {motion}")
    reply = stub.SetMotion(motion_server_pb2.SetMotionRequest(name=motion, priority=3))
    time.sleep(1)

    motion = "sleep"
    print(f"5.Send motion {motion} with canceling previous motion")
    reply = stub.SetMotion(
        motion_server_pb2.SetMotionRequest(name=motion, priority=3, clear=True)
    )
    time.sleep(3)

    motion = "happy"
    print(f"6.Set wait 2 sec and set motion {motion}")
    reply = stub.SetWait(motion_server_pb2.SetWaitRequest(time=2.0, priority=3))
    reply = stub.SetMotion(motion_server_pb2.SetMotionRequest(name=motion, priority=3))
    time.sleep(3)

    motion = "lough"
    print(f"7.Set motion {motion} but it's priority is lower so it's ignored")
    reply = stub.SetMotion(motion_server_pb2.SetMotionRequest(name=motion, priority=2))
    time.sleep(3)

    pan = 8.0
    tilt = 8.0
    print(f"8.Set velocity pan: {pan}, tilt: {tilt}")
    reply = stub.SetVel(motion_server_pb2.SetVelRequest(pan=pan, tilt=tilt, priority=3))
    time.sleep(3)

    pan = 0.4
    tilt = 0.0
    print(f"9.Set pos pan: {pan}, tilt: {tilt}")
    reply = stub.SetPos(motion_server_pb2.SetPosRequest(pan=pan, tilt=tilt, priority=3))
    time.sleep(3)

    pan = 0.0
    print(f"10.Set pos pan: {pan}")
    reply = stub.SetPos(motion_server_pb2.SetPosRequest(pan=pan, priority=3))
    time.sleep(3)

    print("Finished!")


if __name__ == "__main__":
    main()
