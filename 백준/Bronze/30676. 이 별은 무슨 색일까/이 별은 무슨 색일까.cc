#include <iostream>
using namespace std;

int main(void) {
	int star;
	cin >> star;

	if (star >= 620) cout << "Red" << endl;
	else if (star >= 590) cout << "Orange" << endl;
	else if (star >= 570) cout << "Yellow" << endl;
	else if (star >= 495) cout << "Green" << endl;
	else if (star >= 450) cout << "Blue" << endl;
	else if (star >= 425) cout << "Indigo" << endl;
	else cout << "Violet" << endl;

	return 0;
}