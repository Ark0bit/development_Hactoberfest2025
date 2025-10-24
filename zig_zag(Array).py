def is_zig_zag(arr):
    n = len(arr)
    for i in range(1, n-1):
        if not ((arr[i-1] < arr[i] > arr[i+1]) or (arr[i-1] > arr[i] < arr[i+1])):
            return False
    return True
if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter elements: ").split()))

    if is_zig_zag(arr):
        print("The array is in zig-zag pattern.")
    else:
        print("The array is NOT in zig-zag pattern.")
