from sqlmodel import Session

import src.pb.score.scoring_pb2_grpc as scoring_pb2_grpc
from src.db.base import engine
from src.db.models.users import UserScore
from src.pb.score.scoring_pb2 import ScoreRequest, ScoreResponse


class ScoringService(scoring_pb2_grpc.ScoringServicer):
    def Score(self, request: ScoreRequest, context):
        with Session(engine) as session:
            user_score = session.get(UserScore, request.login)
            if not user_score:
                raise Exception("User not found")
            return ScoreResponse(score=user_score.score)
