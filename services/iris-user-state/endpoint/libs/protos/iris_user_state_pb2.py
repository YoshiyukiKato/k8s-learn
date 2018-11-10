# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/iris_user_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/iris_user_state.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cprotos/iris_user_state.proto\x12\x06protos\x1a\x1cgoogle/api/annotations.proto\"\x17\n\x06Vector\x12\r\n\x05value\x18\x01 \x03(\x02\"!\n\x0eGetIrisRequest\x12\x0f\n\x07iris_id\x18\x01 \x01(\t\"0\n\x0fGetIrisResponse\x12\x1d\n\x05state\x18\x01 \x01(\x0b\x32\x0e.protos.Vector\"D\n\x11UpdateIrisRequest\x12\x0f\n\x07iris_id\x18\x01 \x01(\t\x12\x1e\n\x06params\x18\x02 \x01(\x0b\x32\x0e.protos.Vector\"\x14\n\x12UpdateIrisResponse\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"0\n\x0fGetUserResponse\x12\x1d\n\x05state\x18\x01 \x01(\x0b\x32\x0e.protos.Vector\"H\n\x11UpdateUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\"\n\nparamsList\x18\x02 \x03(\x0b\x32\x0e.protos.Vector\"\x14\n\x12UpdateUserResponse\";\n\x17UpdateUserByIrisRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07iris_id\x18\x02 \x01(\t\"\x1a\n\x18UpdateUserByIrisResponse2\xee\x03\n\rIrisUserState\x12S\n\x07GetIris\x12\x16.protos.GetIrisRequest\x1a\x17.protos.GetIrisResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/iris/{iris_id}\x12_\n\nUpdateIris\x12\x19.protos.UpdateIrisRequest\x1a\x1a.protos.UpdateIrisResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/iris/{iris_id}:\x01*\x12S\n\x07GetUser\x12\x16.protos.GetUserRequest\x1a\x17.protos.GetUserResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/user/{user_id}\x12_\n\nUpdateUser\x12\x19.protos.UpdateUserRequest\x1a\x1a.protos.UpdateUserResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/user/{user_id}:\x01*\x12q\n\x10UpdateUserByIris\x12\x1f.protos.UpdateUserByIrisRequest\x1a .protos.UpdateUserByIrisResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/user/{user_id}:\x01*b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_VECTOR = _descriptor.Descriptor(
  name='Vector',
  full_name='protos.Vector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.Vector.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=93,
)


_GETIRISREQUEST = _descriptor.Descriptor(
  name='GetIrisRequest',
  full_name='protos.GetIrisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iris_id', full_name='protos.GetIrisRequest.iris_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=128,
)


_GETIRISRESPONSE = _descriptor.Descriptor(
  name='GetIrisResponse',
  full_name='protos.GetIrisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='protos.GetIrisResponse.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=178,
)


_UPDATEIRISREQUEST = _descriptor.Descriptor(
  name='UpdateIrisRequest',
  full_name='protos.UpdateIrisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iris_id', full_name='protos.UpdateIrisRequest.iris_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='protos.UpdateIrisRequest.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=248,
)


_UPDATEIRISRESPONSE = _descriptor.Descriptor(
  name='UpdateIrisResponse',
  full_name='protos.UpdateIrisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=270,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='protos.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='protos.GetUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=305,
)


_GETUSERRESPONSE = _descriptor.Descriptor(
  name='GetUserResponse',
  full_name='protos.GetUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='protos.GetUserResponse.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=355,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='protos.UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='protos.UpdateUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramsList', full_name='protos.UpdateUserRequest.paramsList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=429,
)


_UPDATEUSERRESPONSE = _descriptor.Descriptor(
  name='UpdateUserResponse',
  full_name='protos.UpdateUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=451,
)


_UPDATEUSERBYIRISREQUEST = _descriptor.Descriptor(
  name='UpdateUserByIrisRequest',
  full_name='protos.UpdateUserByIrisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='protos.UpdateUserByIrisRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iris_id', full_name='protos.UpdateUserByIrisRequest.iris_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=512,
)


_UPDATEUSERBYIRISRESPONSE = _descriptor.Descriptor(
  name='UpdateUserByIrisResponse',
  full_name='protos.UpdateUserByIrisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=540,
)

_GETIRISRESPONSE.fields_by_name['state'].message_type = _VECTOR
_UPDATEIRISREQUEST.fields_by_name['params'].message_type = _VECTOR
_GETUSERRESPONSE.fields_by_name['state'].message_type = _VECTOR
_UPDATEUSERREQUEST.fields_by_name['paramsList'].message_type = _VECTOR
DESCRIPTOR.message_types_by_name['Vector'] = _VECTOR
DESCRIPTOR.message_types_by_name['GetIrisRequest'] = _GETIRISREQUEST
DESCRIPTOR.message_types_by_name['GetIrisResponse'] = _GETIRISRESPONSE
DESCRIPTOR.message_types_by_name['UpdateIrisRequest'] = _UPDATEIRISREQUEST
DESCRIPTOR.message_types_by_name['UpdateIrisResponse'] = _UPDATEIRISRESPONSE
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUserResponse'] = _GETUSERRESPONSE
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserResponse'] = _UPDATEUSERRESPONSE
DESCRIPTOR.message_types_by_name['UpdateUserByIrisRequest'] = _UPDATEUSERBYIRISREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserByIrisResponse'] = _UPDATEUSERBYIRISRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.Vector)
  ))
_sym_db.RegisterMessage(Vector)

GetIrisRequest = _reflection.GeneratedProtocolMessageType('GetIrisRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETIRISREQUEST,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetIrisRequest)
  ))
_sym_db.RegisterMessage(GetIrisRequest)

GetIrisResponse = _reflection.GeneratedProtocolMessageType('GetIrisResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETIRISRESPONSE,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetIrisResponse)
  ))
_sym_db.RegisterMessage(GetIrisResponse)

UpdateIrisRequest = _reflection.GeneratedProtocolMessageType('UpdateIrisRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEIRISREQUEST,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.UpdateIrisRequest)
  ))
_sym_db.RegisterMessage(UpdateIrisRequest)

UpdateIrisResponse = _reflection.GeneratedProtocolMessageType('UpdateIrisResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEIRISRESPONSE,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.UpdateIrisResponse)
  ))
_sym_db.RegisterMessage(UpdateIrisResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERREQUEST,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetUserRequest)
  ))
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERRESPONSE,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetUserResponse)
  ))
_sym_db.RegisterMessage(GetUserResponse)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERREQUEST,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.UpdateUserRequest)
  ))
_sym_db.RegisterMessage(UpdateUserRequest)

UpdateUserResponse = _reflection.GeneratedProtocolMessageType('UpdateUserResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERRESPONSE,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.UpdateUserResponse)
  ))
_sym_db.RegisterMessage(UpdateUserResponse)

UpdateUserByIrisRequest = _reflection.GeneratedProtocolMessageType('UpdateUserByIrisRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERBYIRISREQUEST,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.UpdateUserByIrisRequest)
  ))
_sym_db.RegisterMessage(UpdateUserByIrisRequest)

UpdateUserByIrisResponse = _reflection.GeneratedProtocolMessageType('UpdateUserByIrisResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERBYIRISRESPONSE,
  __module__ = 'protos.iris_user_state_pb2'
  # @@protoc_insertion_point(class_scope:protos.UpdateUserByIrisResponse)
  ))
_sym_db.RegisterMessage(UpdateUserByIrisResponse)



_IRISUSERSTATE = _descriptor.ServiceDescriptor(
  name='IrisUserState',
  full_name='protos.IrisUserState',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=543,
  serialized_end=1037,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetIris',
    full_name='protos.IrisUserState.GetIris',
    index=0,
    containing_service=None,
    input_type=_GETIRISREQUEST,
    output_type=_GETIRISRESPONSE,
    serialized_options=_b('\202\323\344\223\002\021\022\017/iris/{iris_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateIris',
    full_name='protos.IrisUserState.UpdateIris',
    index=1,
    containing_service=None,
    input_type=_UPDATEIRISREQUEST,
    output_type=_UPDATEIRISRESPONSE,
    serialized_options=_b('\202\323\344\223\002\024\"\017/iris/{iris_id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='protos.IrisUserState.GetUser',
    index=2,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_GETUSERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\021\022\017/user/{user_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUser',
    full_name='protos.IrisUserState.UpdateUser',
    index=3,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=_UPDATEUSERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\024\"\017/user/{user_id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUserByIris',
    full_name='protos.IrisUserState.UpdateUserByIris',
    index=4,
    containing_service=None,
    input_type=_UPDATEUSERBYIRISREQUEST,
    output_type=_UPDATEUSERBYIRISRESPONSE,
    serialized_options=_b('\202\323\344\223\002\024\"\017/user/{user_id}:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_IRISUSERSTATE)

DESCRIPTOR.services_by_name['IrisUserState'] = _IRISUSERSTATE

# @@protoc_insertion_point(module_scope)