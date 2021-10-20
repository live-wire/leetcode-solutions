class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)
