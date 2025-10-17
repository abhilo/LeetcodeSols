# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Okay, whenever I see something like K points or something that has to do with a param K, intuition leads to me to think heaps.

# So in this case, we're trying to find the k closts points to the origin, so we can use a heap to maintain those points

import heapq


def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    maxHeap = []

    for x, y in points:
        distance = -(x * x + y * y)
        if len(maxHeap) < k:
            heapq.heappush(maxHeap, (distance, x, y))

        else:
            currentMax = maxHeap[0][0]
            if distance > currentMax:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (distance, x, y))


    return [[x, y] for (_, x, y) in maxHeap]



# in C++
# vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
#     // max-heap to store {distance, point}
#     priority_queue<pair<int, vector<int>>> maxHeap;

#     for (auto& point : points) {
#         int x = point[0];
#         int y = point[1];
#         int dist = x * x + y * y;

#         // Push into heap
#         maxHeap.push({dist, point});

#         // Keep only k elements
#         if (maxHeap.size() > k) {
#             maxHeap.pop();
#         }
#     }

#     // Extract k closest points
#     vector<vector<int>> result;
#     while (!maxHeap.empty()) {
#         result.push_back(maxHeap.top().second);
#         maxHeap.pop();
#     }

#     return result;
# }
    

