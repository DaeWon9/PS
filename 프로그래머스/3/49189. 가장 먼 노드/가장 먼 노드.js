function solution(n, edge) {
    const visited = Array.from({ length: n + 1}, () => false);
    const adjVertices = Array.from({ length: n + 1 }, () => []);
    const distance = Array.from({ length: n + 1}, () => Number.MAX_SAFE_INTEGER)
    distance[1] = 0
    
    for (const [v1, v2] of edge) {
        adjVertices[v1].push(v2)
        adjVertices[v2].push(v1)
    }
    
    const queue = []
    queue.push([1, 0])
    visited[1] = true
    
    while (queue.length > 0) {
        const [v, d] = queue.shift();
        
        for (const adjVertex of adjVertices[v]) {
            if (!visited[adjVertex]) {
                queue.push([adjVertex, d + 1]);
                distance[adjVertex] = d + 1;
                visited[adjVertex] = true;
            }
        }
    }
    
    const maxDistance = Math.max(...distance.slice(1));
    const answer = distance.filter((dist) => dist === maxDistance).length;
    
    return answer;
    
}