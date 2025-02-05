#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 0, j = N; i < N, j > 0; i++, j--) {
		for (int x = 0; x < i; x++) {
			cout << ' ';
		}
		for (int y = 0; y < j; y++) {
			if (y != j - 1) {
				cout << '*';
			} else {
				cout << '*' << endl;
			}
		}
	}
	return 0;
}