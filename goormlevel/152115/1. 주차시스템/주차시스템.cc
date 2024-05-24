#include <iostream>
#include <deque>
#include <vector>
#include <utility>

using namespace std;

int N, M;
int graph[2000][2000];
int direction_x[4] = {1, -1, 0, 0};
int direction_y[4] = {0, 0, 1, -1};
bool visited[2000][2000] = {false};

bool is_movable(int dr, int dc){
    return 0 <= dr && dr < N && 0 <= dc && dc < M;
}

int bfs(int r, int c){
    int value = 0;
    deque<pair<int, int>> queue;
    queue.push_back(make_pair(r, c));
    visited[r][c] = true;
    
    if (graph[r][c] == 0){
        value += 1;
    }
    else{
        value -= 2;
    }

    while (!queue.empty()){
        pair<int, int> p = queue.front();
        queue.pop_front();
        
        for (int i = 0; i < 4; i++){
            int dr = p.first + direction_y[i];
            int dc = p.second + direction_x[i];
            
            if (is_movable(dr, dc) && !visited[dr][dc] && graph[dr][dc] != 1){
                visited[dr][dc] = true;
                if (graph[dr][dc] == 0){
                    value += 1;
                }
                else{
                    value -= 2;
                }
                queue.push_back(make_pair(dr, dc));
            }
        }
    }
    
    return value;
}

int main() {
    int maxValue = 0;
    cin >> N >> M;
    
    for (int r = 0; r < N; r++){
        for (int c = 0; c < M; c++){
            cin >> graph[r][c];
        }
    }
    
    for (int r = 0; r < N; r++){
        for (int c = 0; c < M; c++){
            if (graph[r][c] == 1){
                continue;
            }
            if (!visited[r][c]){
                int tempValue = bfs(r, c);
                if (tempValue > maxValue){
                    maxValue = tempValue;
                }
            }
        }
    }
    
    cout << maxValue;
    
    return 0;
}