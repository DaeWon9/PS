#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node* next;
} Node;

typedef struct deque {
  Node* front;
  Node* rear;
} Deque;

void initDeque(Deque* deque);
int isEmptyDeque(Deque* deque);
void pushFrontDeque(Deque* deque, int data);
void pushBackDeque(Deque* deque, int data);
int popFrontDeque(Deque* deque);
int popBackDeque(Deque* deque);

void bfs(int startVertex);
void dfs(int startVertex);

int n, m, v;
int **graph;
int *visited1;
int *visited2;

int main() {
    int v1, v2;
    scanf("%d %d %d", &n, &m, &v);
    
    graph = (int**)malloc(sizeof(int*) * (n+1));
    for(int i = 0; i < n + 1; i++){
        graph[i] = (int*)malloc(sizeof(int) * (n+1));
        for (int j = 0; j < n + 1 ; j++){
            graph[i][j] = 0; // 정점개수로 초기화 -> 인접행렬
        }
    }
    
    visited1 = (int*)malloc(sizeof(int) * (n+1)); // visted 초기화
    for (int i = 0 ; i < n + 1; i++){
        visited1[i] = 0;
    }
    visited2 = (int*)malloc(sizeof(int) * (n+1)); // visted 초기화
    for (int i = 0 ; i < n + 1; i++){
        visited2[i] = 0;
    }
    
    for (int i = 0; i < m; i++){
        scanf("%d %d", &v1, &v2);
        graph[v1][v2] = 1;
        graph[v2][v1] = 1;
    }
    
    dfs(v);
    printf("\n");
    bfs(v);
    printf("\n");
    
    free(visited1);
    free(visited2);
    for (int i = 0 ; i < n+1; i++){
        free(graph[i]);
    }
    free(graph);
    
    return 0;
}


void bfs(int startVertex){
    Deque deque;
    initDeque(&deque);
    pushBackDeque(&deque, startVertex);
    visited1[startVertex] = 1;
    
    while (!isEmptyDeque(&deque)){
        int vertex = popFrontDeque(&deque);
        printf("%d ", vertex);
        
        for (int i = 0; i < n + 1; i++){
            if (!visited1[i] && graph[vertex][i]){
                pushBackDeque(&deque, i);
                visited1[i] = 1;
            }
        }
    }
}

void dfs(int startVertex){
    visited2[startVertex] = 1;
    printf("%d ", startVertex);
    for (int i = 1; i < n + 1; i++){
        if (!visited2[i] && graph[startVertex][i]){
            dfs(i);
        }
    }
}

void initDeque(Deque* deque) {
  deque->front = NULL;
  deque->rear = NULL;
}

int isEmptyDeque(Deque* deque) {
  return deque->front == NULL;
}

void pushFrontDeque(Deque* deque, int data) {
  Node* new_node = (Node*)malloc(sizeof(Node));
  new_node->data = data;
  new_node->next = deque->front;
  deque->front = new_node;

  if (deque->rear == NULL) {
    deque->rear = new_node;
  }
}

void pushBackDeque(Deque* deque, int data) {
  Node* new_node = (Node*)malloc(sizeof(Node));
  new_node->data = data;
  new_node->next = NULL;

  if (isEmptyDeque(deque)) {
    deque->front = new_node;
    deque->rear = new_node;
  } else {
    deque->rear->next = new_node;
    deque->rear = new_node;
  }
}

int popFrontDeque(Deque* deque) {
  if (isEmptyDeque(deque)) {
    return -1;
  }

  int data = deque->front->data;
  Node* temp = deque->front;
  deque->front = deque->front->next;
  free(temp);

  if (deque->front == NULL) {
    deque->rear = NULL;
  }

  return data;
}

int popBackDeque(Deque* deque) {
  if (isEmptyDeque(deque)) {
    return -1;
  }

  int data = deque->rear->data;
  Node* temp = deque->rear;
  deque->rear = deque->rear->next;
  free(temp);

  if (deque->rear == NULL) {
    deque->front = NULL;
  }

  return data;
}
