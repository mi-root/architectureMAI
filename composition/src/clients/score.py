import grpc
from src.pb.score.scoring_pb2 import ScoreRequest
from src.pb.score.scoring_pb2_grpc import ScoringStub
from src.config.base import settings


async def get_score(login: str) -> float:
    channel = grpc.insecure_channel(settings.score_url)
    client = ScoringStub(channel)
    request = ScoreRequest(login=login)
    return client.Score(request).score
