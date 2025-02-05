#include <iostream>

using namespace std;

// 놀랍게도 C++을 독학하는 중 + 파이썬에서 사용되는 문자열 연산이 있을까?
int main() {
	int N;
	cin >> N;
	for (int i = N - 1, j = 1; i > 0; i--, j+=2) {
		for (int x = 0; x < i; x++) {
			cout << ' ';
		}
		for (int y = 0; y < j; y++) {
			if (y < j - 1) {
				cout << '*';
			} else {
				cout << '*' << endl;
			}
		}
	}
	for (int z = 0; z < (N * 2) - 1; z++) {
		cout << '*';
	}
	return 0;
}