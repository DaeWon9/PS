function solution(dice) {
    let answer = [];
    let dice_id_lists = [];
    let combinations = [];
    let N = dice.length;
    let M = N / 2;
    let max_win_count = 0;
    
    for (let i = 0; i < N; i++){
        dice_id_lists.push(i);
    }
    
    function bisect_left(arr, target) {
        let left = 0;
        let right = arr.length;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
    
    function cartesianProduct(arrays) {
        return arrays.reduce((acc, array) => {
            return acc.flatMap(a => array.map(b => [...a, b]));
        }, [[]]);
    }
    
    function difference(A) {
        return new Set([...dice_id_lists].filter(x => !A.has(x)));
    }

    function generateCombinations(start, combination) {
        if (combination.length === M) {
            combinations.push([...combination]);
            return;
        }
        for (let i = start; i < N; i++) {
            combination.push(dice_id_lists[i]);
            generateCombinations(i + 1, combination);
            combination.pop(); // back tracking
        }
    }

    generateCombinations(0, []);
    
    for (const A_dices of combinations){
        let B_dices = difference(new Set(A_dices));
        
        let A_score_data = [];
        let A_scores = [];
        let B_score_data = [];
        let B_scores = [];
        
        for (let id of A_dices){
            A_score_data.push(dice[id])
        }
        
        for (let item of cartesianProduct(A_score_data)){
            let sum = item.reduce((s, c) => s + c);
            A_scores.push(sum)
        }
        
        for (let id of B_dices){
            B_score_data.push(dice[id])
        }
        
        for (let item of cartesianProduct(B_score_data)){
            let sum = item.reduce((s, c) => s + c);
            B_scores.push(sum)
        }
        
        A_scores.sort((a, b) => b - a);
        B_scores.sort((a, b) => a - b);
        
        let win_count = 0;
        
        for (let A_score of A_scores){
            let count = bisect_left(B_scores, A_score);
            if (count < 1) break;
            win_count += count;
        }
        
        if (max_win_count < win_count){
            answer = A_dices.map((id) => id + 1)
            max_win_count = win_count;
        }
          
    }    
    
    return answer;

}