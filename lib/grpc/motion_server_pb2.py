# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: motion_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13motion_server.proto\x12\rmotion_server\"\x82\x01\n\x10SetMotionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\x08priority\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06repeat\x18\x03 \x01(\x08H\x01\x88\x01\x01\x12\x12\n\x05\x63lear\x18\x04 \x01(\x08H\x02\x88\x01\x01\x42\x0b\n\t_priorityB\t\n\x07_repeatB\x08\n\x06_clear\"!\n\x0eSetMotionReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x14\n\x12\x43learMotionRequest\"#\n\x10\x43learMotionReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"`\n\x0eSetWaitRequest\x12\x0c\n\x04time\x18\x01 \x01(\x02\x12\x15\n\x08priority\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05\x63lear\x18\x03 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_priorityB\x08\n\x06_clear\"\x1f\n\x0cSetWaitReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x82\x02\n\x13MotionServerService\x12M\n\tSetMotion\x12\x1f.motion_server.SetMotionRequest\x1a\x1d.motion_server.SetMotionReply\"\x00\x12S\n\x0b\x43learMotion\x12!.motion_server.ClearMotionRequest\x1a\x1f.motion_server.ClearMotionReply\"\x00\x12G\n\x07SetWait\x12\x1d.motion_server.SetWaitRequest\x1a\x1b.motion_server.SetWaitReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'motion_server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SETMOTIONREQUEST']._serialized_start=39
  _globals['_SETMOTIONREQUEST']._serialized_end=169
  _globals['_SETMOTIONREPLY']._serialized_start=171
  _globals['_SETMOTIONREPLY']._serialized_end=204
  _globals['_CLEARMOTIONREQUEST']._serialized_start=206
  _globals['_CLEARMOTIONREQUEST']._serialized_end=226
  _globals['_CLEARMOTIONREPLY']._serialized_start=228
  _globals['_CLEARMOTIONREPLY']._serialized_end=263
  _globals['_SETWAITREQUEST']._serialized_start=265
  _globals['_SETWAITREQUEST']._serialized_end=361
  _globals['_SETWAITREPLY']._serialized_start=363
  _globals['_SETWAITREPLY']._serialized_end=394
  _globals['_MOTIONSERVERSERVICE']._serialized_start=397
  _globals['_MOTIONSERVERSERVICE']._serialized_end=655
# @@protoc_insertion_point(module_scope)
