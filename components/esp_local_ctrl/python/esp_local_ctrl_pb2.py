# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: esp_local_ctrl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import constants_pb2 as constants__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x65sp_local_ctrl.proto\x1a\x0f\x63onstants.proto\"\x15\n\x13\x43mdGetPropertyCount\">\n\x14RespGetPropertyCount\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"a\n\x0cPropertyInfo\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\r\x12\r\n\x05\x66lags\x18\x04 \x01(\r\x12\r\n\x05value\x18\x05 \x01(\x0c\"\'\n\x14\x43mdGetPropertyValues\x12\x0f\n\x07indices\x18\x01 \x03(\r\"N\n\x15RespGetPropertyValues\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\x1c\n\x05props\x18\x02 \x03(\x0b\x32\r.PropertyInfo\"-\n\rPropertyValue\x12\r\n\x05index\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x0c\"5\n\x14\x43mdSetPropertyValues\x12\x1d\n\x05props\x18\x01 \x03(\x0b\x32\x0e.PropertyValue\"0\n\x15RespSetPropertyValues\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\"\xfb\x02\n\x10LocalCtrlMessage\x12\x1e\n\x03msg\x18\x01 \x01(\x0e\x32\x11.LocalCtrlMsgType\x12\x32\n\x12\x63md_get_prop_count\x18\n \x01(\x0b\x32\x14.CmdGetPropertyCountH\x00\x12\x34\n\x13resp_get_prop_count\x18\x0b \x01(\x0b\x32\x15.RespGetPropertyCountH\x00\x12\x32\n\x11\x63md_get_prop_vals\x18\x0c \x01(\x0b\x32\x15.CmdGetPropertyValuesH\x00\x12\x34\n\x12resp_get_prop_vals\x18\r \x01(\x0b\x32\x16.RespGetPropertyValuesH\x00\x12\x32\n\x11\x63md_set_prop_vals\x18\x0e \x01(\x0b\x32\x15.CmdSetPropertyValuesH\x00\x12\x34\n\x12resp_set_prop_vals\x18\x0f \x01(\x0b\x32\x16.RespSetPropertyValuesH\x00\x42\t\n\x07payload*\xc7\x01\n\x10LocalCtrlMsgType\x12\x1b\n\x17TypeCmdGetPropertyCount\x10\x00\x12\x1c\n\x18TypeRespGetPropertyCount\x10\x01\x12\x1c\n\x18TypeCmdGetPropertyValues\x10\x04\x12\x1d\n\x19TypeRespGetPropertyValues\x10\x05\x12\x1c\n\x18TypeCmdSetPropertyValues\x10\x06\x12\x1d\n\x19TypeRespSetPropertyValues\x10\x07\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'esp_local_ctrl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCALCTRLMSGTYPE._serialized_start=883
  _LOCALCTRLMSGTYPE._serialized_end=1082
  _CMDGETPROPERTYCOUNT._serialized_start=41
  _CMDGETPROPERTYCOUNT._serialized_end=62
  _RESPGETPROPERTYCOUNT._serialized_start=64
  _RESPGETPROPERTYCOUNT._serialized_end=126
  _PROPERTYINFO._serialized_start=128
  _PROPERTYINFO._serialized_end=225
  _CMDGETPROPERTYVALUES._serialized_start=227
  _CMDGETPROPERTYVALUES._serialized_end=266
  _RESPGETPROPERTYVALUES._serialized_start=268
  _RESPGETPROPERTYVALUES._serialized_end=346
  _PROPERTYVALUE._serialized_start=348
  _PROPERTYVALUE._serialized_end=393
  _CMDSETPROPERTYVALUES._serialized_start=395
  _CMDSETPROPERTYVALUES._serialized_end=448
  _RESPSETPROPERTYVALUES._serialized_start=450
  _RESPSETPROPERTYVALUES._serialized_end=498
  _LOCALCTRLMESSAGE._serialized_start=501
  _LOCALCTRLMESSAGE._serialized_end=880
# @@protoc_insertion_point(module_scope)
