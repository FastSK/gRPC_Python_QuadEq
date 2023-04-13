from concurrent import futures
import logging
import time

import grpc
import quadratic_pb2
import quadratic_pb2_grpc
import math


class SolveServicer(quadratic_pb2_grpc.apiServicer):
    def solve(self, request, context):
        a = request.a
        b = request.b
        c = request.c

        discriminant = b ** 2 - 4 * a * c

        if a == 0 or discriminant < 0:
            # return quadratic_pb2.Solution()
            return quadratic_pb2.Solution(num_solutions=0)

        elif discriminant == 0:
            # One real solution
            sol = (-b / (2 * a))
            return quadratic_pb2.Solution(num_solutions=1, solutions=[sol])
        else:
            # Two real solutions
            sol1 = (-b + math.sqrt(discriminant)) / (2 * a)
            sol2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return quadratic_pb2.Solution(num_solutions=2, solutions=[sol1, sol2])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quadratic_pb2_grpc.add_apiServicer_to_server(SolveServicer(), server)
    server.add_insecure_port('[::]:9999')
    server.start()
    while True:
        time.sleep(860000)

    # server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
