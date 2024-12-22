import grpc
from src.pb.auth.auth_pb2 import AuthenticateRequest
from src.pb.auth.auth_pb2_grpc import AuthStub
from src.config.base import settings


async def authenticate(login: str, password: str) -> bool:
    channel = grpc.insecure_channel(settings.auth_url)
    client = AuthStub(channel)
    request = AuthenticateRequest(login=login, password=password)
    return client.Authenticate(request).allowed_access