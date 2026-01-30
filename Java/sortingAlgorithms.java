import java.util.Random;

public class sortingAlgorithms {
    // Function to swap elements
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Function to print array
    static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Function to generate random pivot
    static int generateRandomPivot(int low, int high) {
        Random rand = new Random();
        return low + rand.nextInt(high - low + 1);
    }

    // QuickSort with Lomuto Partitioning
    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    static void quickSortRandomPivot(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = generateRandomPivot(low, high);
            int pivotValue = arr[pivotIndex];
            swap(arr, pivotIndex, high);

            int i = low - 1;
            for (int j = low; j < high; j++) {
                if (arr[j] < pivotValue) {
                    i++;
                    swap(arr, i, j);
                }
            }
            swap(arr, i + 1, high);
            quickSortRandomPivot(arr, low, i);
            quickSortRandomPivot(arr, i + 2, high);
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];
        int i = left, j = mid + 1, k = 0;
        
        while (i <= mid && j <= right) {
            temp[k++] = (arr[i] <= arr[j]) ? arr[i++] : arr[j++];
        }
        while (i <= mid) temp[k++] = arr[i++];
        while (j <= right) temp[k++] = arr[j++];
        
        System.arraycopy(temp, 0, arr, left, temp.length);
    }

    static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    static void bubbleSort(int[] arr) {
        boolean didSwap;
        for (int i = arr.length - 1; i >= 0; i--) {
            didSwap = false;
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    didSwap = true;
                }
            }
            if (!didSwap) break;
        }
    }

    static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            swap(arr, minIndex, i);
        }
    }

    public static void main(String[] args) {
        int[] arr = {13, 46, 24, 52, 20, 9};
        System.out.println("Array before Sorting:");
        printArray(arr);

        // selectionSort(arr);
        // bubbleSort(arr);
        // insertionSort(arr);
        // mergeSort(arr, 0, arr.length - 1);
        quickSort(arr, 0, arr.length - 1);


        System.out.println("Array after Sorting:");
        printArray(arr);
    }
}
