from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticateRequest(_message.Message):
    __slots__ = ("login", "password")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    def __init__(
        self, login: _Optional[str] = ..., password: _Optional[str] = ...
    ) -> None: ...

class AuthenticateResponse(_message.Message):
    __slots__ = ("allowed_access",)
    ALLOWED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    allowed_access: bool
    def __init__(self, allowed_access: bool = ...) -> None: ...
