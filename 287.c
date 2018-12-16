// http://www.bjfuacm.com/problem/287/

#include <stdio.h>
#include <stdbool.h>

bool search(int* a, int lo, int hi, int key) {
    int mid = (hi + lo) / 2;
    if (key == *(a + mid)) return true;
    if (lo >= hi) {
        return false;
    } else if (key > *(a + mid)) {
        return search(a, mid + 1, hi, key);
    } else if (key < *(a + mid)) {
        return search(a, lo, mid - 1, key);
    }
    return false;
}

int main() {
    int n, query;
    int a[10005];
    while (scanf("%d", &n) && n) {
        for (int i = 0; i < n; i++) scanf("%d", a + i);
        scanf("%d", &query);
        printf("%s\n", (search(a, 0, n - 1, query)) ? "YES" : "NO");
    }
}