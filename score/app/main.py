from concurrent import futures

import grpc

import src.pb.score.scoring_pb2_grpc as scoring_pb2_grpc
from src.api.score import ScoringService
from src.db.base import create_db_and_tables
from src.db.models.users import create_user_score


def on_startup():
    create_db_and_tables()
    create_user_score()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scoring_pb2_grpc.add_ScoringServicer_to_server(ScoringService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    on_startup()
    serve()
