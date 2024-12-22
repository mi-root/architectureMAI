from sqlmodel import Session

import src.pb.auth.auth_pb2_grpc as auth_pb2_grpc
from src.db.base import engine
from src.db.models.users import User
from src.pb.auth.auth_pb2 import AuthenticateRequest, AuthenticateResponse
from src.utils.password import get_hashed_password


class AuthService(auth_pb2_grpc.AuthServicer):
    def Authenticate(self, request: AuthenticateRequest, context):
        allowed_access = False
        with Session(engine) as session:
            user = session.get(User, request.login)
            if user and user.password == get_hashed_password(
                request.password, user.salt
            ):
                allowed_access = True
        return AuthenticateResponse(allowed_access=allowed_access)
