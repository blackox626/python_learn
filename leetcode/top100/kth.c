/**
 *
 * @param a int整型一维数组
 * @param aLen int a数组长度
 * @param n int整型
 * @param K int整型
 * @return int整型
 */
int position(int* a ,int start, int end) {
    int temp = a[start];
    int left = start;
    int right = end;

    while(left < right) {
        while (left < right && a[right] > temp) {
            right --;
        }
        a[left] = a[right];
        while (left < right && a[left] <= temp) {
            left ++;
        }
        a[right] = a[left];
    }

    a[right] = temp;

    return right;
}

void sort(int* a,int start, int aLen) {
    if(start > aLen) {
        return;
    }
    if (aLen < 2) {
        return;
    }
    int pos = position(a,start,aLen);
    sort(a,start,pos-1);
    sort(a,pos+1,aLen);
}


int findKth(int* a, int aLen, int n, int K ) {
    // write code here

    sort(a,0,aLen-1);
    int count = 0;
    int num = 0;
    for(int i = aLen -1; i>=0; i --) {
        if(num != a[i]) {
            count ++;
        }
        num = a[i];

        if(count == K) {
//             printf("%d",a[i]);
            return a[i];
        }
    }

    return -1;
}

