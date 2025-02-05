#include <iostream>

using namespace std;

// C++ 독학하는 중
int main() {
	int N;
	string snow;
	cin >> N;
	for (int i = 0; i < N; i++) {
		snow += "* ";
	}
	for (int i = 0; i < N; i++) {
		if (i % 2 == 0) cout << snow << endl;
		else cout << " " << snow << endl;
	}
	return 0;
}