
# Given an array of integers temperatures represents the daily temperatures, return 
# an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# time complexity for the solution is optimal
# the outer loop does n iterations and the inner while loop inserts and pops at most n times so O(n + n) = O(2n) = O(n) time



def dailyTemperatures(temperatures: List[int]) -> List[int]:

    stack = [0]
    n = len(temperatures)
    res = [0] * n
    for i in range(1, n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            indice = stack.pop()
            days = i - indice
            res[indice] = days
        stack.append(i)


    return res
                


# C++
# vector<int> dailyTemperatures(vector<int>& temperatures) {

#     int n = temparture.size();
#     vector<int> v(n, 0);
#     stack<int> s;

#     for (int i = 0; i < n; i++){

#         while (!s.empty() && temperatures[i] > temperatures[s.top()]){
#             int indice = s.top();
#             s.pop();
#             int days = i - indice;
#             res[indice] = day;
#         }
#         s.push(i);
#     }

#     return res;





}

