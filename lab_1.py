def find_kth_largest(arr, k):
    if k <= 0 or len(arr) < k:
        raise ValueError("Розмір масиву повинен бути не менше k і k повинно бути позитивним числом")
    
    indexed_arr = [(val, idx) for idx, val in enumerate(arr)]
    
    def partition(arr, left, right):
        point = arr[right][0] 
        i = left
        for j in range(left, right):
            if arr[j][0] > point:  
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i
    
    left, right = 0, len(arr) - 1
    k_index = k - 1

    while left <= right:
        point_index = partition(indexed_arr, left, right)
        if point_index == k_index:
            return indexed_arr[point_index][0], indexed_arr[point_index][1]
        
        elif point_index < k_index:
            left = point_index + 1
        else:
            right = point_index - 1

def main():
        arr = [1, 2, 3, 4, 5]
        k = int(input('Який елемент потрібно знайти: '))
        result = find_kth_largest(arr, k)

        print(f"Знайдений {k}-й найбільший елемент: {result[0]}")
        print(f"Позиція {k}-го найбільшого елемента в масиві: {result[1]}")

if __name__ == "__main__":
    main()    