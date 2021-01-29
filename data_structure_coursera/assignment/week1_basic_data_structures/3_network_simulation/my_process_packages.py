# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process", "index"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        return Response(False, -1)

def process(S, requests):
    processing_queue = []
    start_time = [0 for i in range(len(requests))]
    abs_time = 0
    ind = 0
    current_required_time_to_process = 0
    while len(processing_queue) > 0 or ind < len(requests) or current_required_time_to_process > 0:
        while ind < len(requests) and requests[ind].arrived_at == abs_time:
            if requests[ind].time_to_process == 0 and len(processing_queue) == 0 and current_required_time_to_process==0:
                start_time[ind] = abs_time
            elif current_required_time_to_process > 0 and len(processing_queue) < S-1:
                processing_queue.append(requests[ind])
            elif current_required_time_to_process == 0 and len(processing_queue) < S:
                processing_queue.append(requests[ind])
            else:
                start_time[ind] = -1
            ind += 1

        if current_required_time_to_process == 0:
            if processing_queue:
                current = processing_queue.pop(0)
                current_required_time_to_process = current.time_to_process
                start_time[current.index] = abs_time
        if current_required_time_to_process>0:
            current_required_time_to_process -= 1
        abs_time += 1

    return start_time

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for i in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process, i))

    # buffer = Buffer(buffer_size)
    # responses = process_requests(requests, buffer)
    #
    # for response in responses:
    #     print(response.started_at if not response.was_dropped else -1)
    if not n_requests:
        return None
    out = process(buffer_size, requests)
    for item in out:
        print(item)


if __name__ == "__main__":
    main()
