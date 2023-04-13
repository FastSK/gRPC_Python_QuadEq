import logging

import grpc
import quadratic_pb2
import quadratic_pb2_grpc


def run(client):
    a = float(input('Enter coefficient a: '))
    b = float(input('Enter coefficient b: '))
    c = float(input('Enter coefficient c: '))

    response = client.solve(quadratic_pb2.Coefficients(a=a, b=b, c=c))

    if response.num_solutions == 0:
        print("No solution")
    elif response.num_solutions == 1:
        print("Solution: ", response.solutions[0])
    else:
        print("Solution: {}, {}".format(response.solutions[0], response.solutions[1]))


def connect():
    channel = grpc.insecure_channel('localhost:9999')
    client = quadratic_pb2_grpc.apiStub(channel)
    run(client)


if __name__ == '__main__':
    logging.basicConfig()
    connect()
