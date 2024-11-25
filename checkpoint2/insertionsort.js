function insertionSort(arr) {
    
    for (let i = 1; i < arr.length; i++) {
        
        let currentElement = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > currentElement) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = currentElement;
    }
    return arr;
}

let array = [12, 11, 13, 5, 6];
console.log("Sorted Array: " + insertionSort(array));
