
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

struct Data {
	double a;
	double b;
	double c;
	double d;
	char label;

	Data(double a_, double b_, double c_, double d_, char label_) :
	    a(a_),
	    b(b_),
	    c(c_),
	    d(d_),
	    label(label_) {}

	friend std::ostream& operator<<(std::ostream& out, Data point) {
		out << point.a << " " << point.b << " " << point.c << " " << point.d << " " << point.label;

		return out;
	}
};

std::vector<Data> arr = {{5.1, 3.5, 1.3, 0.2, 'A'}, {5.7, 3.4, 1.3, 0.2, 'C'},
                         {4.7, 3.1, 1.6, 0.2, 'A'}, {5.0, 4.6, 1.4, 0.1, 'B'},
                         {5.9, 3.3, 4.0, 1.3, 'C'}, {6.5, 2.7, 4.6, 1.5, 'A'},
                         {5.7, 2.8, 4.4, 1.3, 'B'}, {6.3, 3.3, 4.7, 1.4, 'C'},
                         {4.7, 2.4, 3.2, 1.0, 'A'}, {7.7, 3.6, 6.7, 2.2, 'B'},
                         {7.7, 2.6, 6.5, 2.3, 'C'}, {6.0, 2.2, 5.0, 1.4, 'A'},
                         {6.9, 3.2, 5.7, 9.3, 'B'}, {5.6, 2.2, 4.6, 2.0, 'C'},
                         {5.0, 2.8, 4.6, 0.7, 'X'}};

std::vector<double> findEuclideanDistance(std::vector<Data> dataArr, Data newExample) {
	std::vector<double> data;
	data.reserve(15);
	for (int i = 0; i < dataArr.size(); i++) {
		double squaredA = (dataArr[i].a - newExample.a) * (dataArr[i].a - newExample.a);
		double squaredB = (dataArr[i].b - newExample.b) * (dataArr[i].b - newExample.b);
		double squaredC = (dataArr[i].c - newExample.c) * (dataArr[i].c - newExample.c);
		double squaredD = (dataArr[i].d - newExample.d) * (dataArr[i].d - newExample.d);

		double total = squaredA + squaredB + squaredC + squaredD;

		// Square root and find the euclidean distance
		double eDistance = std::sqrt(total);

		std::cout << "Euclidean Distance: " << eDistance
		          << "\nLabel of current Index : " << dataArr[i].label << "\n\n\n";

		data.emplace_back(eDistance);
	}

	std::cout << "Example Point " << newExample;

	return data;
}

std::vector<double> findManhantanDistance(std::vector<Data> dataArr, Data newExample) {
	std::vector<double> data;
	data.reserve(15);
	for (int i = 0; i < dataArr.size(); i++) {
		double squaredA = std::abs((dataArr[i].a - newExample.a));
		double squaredB = std::abs((dataArr[i].b - newExample.b));
		double squaredC = std::abs((dataArr[i].c - newExample.c));
		double squaredD = std::abs((dataArr[i].d - newExample.d));

		double total = squaredA + squaredB + squaredC + squaredD;

		// Square root and find the euclidean distance

		std::cout << "Manhattan Distance: " << total
		          << "\nLabel of current Index : " << dataArr[i].label << "\n\n\n";

		data.emplace_back(total);
	}

	std::cout << "Example Point " << newExample;

	return data;
}

double findMax(std::vector<Data> arr, char field) {
	double max = std::numeric_limits<double>::min();

	if (field == 'a') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].a > max) {
				max = arr[i].a;
			}
		}
	}
	else if (field == 'b') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].b > max) {
				max = arr[i].b;
			}
		}
	}
	else if (field == 'c') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].c > max) {
				max = arr[i].c;
			}
		}
	}
	else if (field == 'd') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].d > max) {
				max = arr[i].d;
			}
		}
	}

	return max;
}

double findMin(std::vector<Data> arr, char field) {
	double min = std::numeric_limits<double>::max();

	if (field == 'a') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].a < min) {
				min = arr[i].a;
			}
		}
	}
	else if (field == 'b') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].b < min) {
				min = arr[i].b;
			}
		}
	}
	else if (field == 'c') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].c < min) {
				min = arr[i].c;
			}
		}
	}
	else if (field == 'd') {
		for (int i = 0; i < arr.size(); i++) {
			if (arr[i].d < min) {
				min = arr[i].d;
			}
		}
	}

	return min;
}

std::vector<Data> normalizeData(std::vector<Data> arr) {
	std::vector<Data> normalizedSet;
	normalizedSet.reserve(15);

	for (int i = 0; i < arr.size(); i++) {
		char label = arr[i].label;
		// A
		double maxA = findMax(arr, 'a');
		double minA = findMin(arr, 'b');

		double normalA = ((arr[i].a - minA) / (maxA - minA));

		// B
		double maxB = findMax(arr, 'b');
		double minB = findMin(arr, 'b');

		double normalB = ((arr[i].b - minB) / (maxB - minB));

		// C
		double maxC = findMax(arr, 'c');
		double minC = findMin(arr, 'c');

		double normalC = ((arr[i].c - minC) / (maxC - minC));

		// D
		double maxD = findMax(arr, 'd');
		double minD = findMin(arr, 'd');

		double normalD = ((arr[i].d - minD) / (maxD - minD));

		Data normalizedIndex{normalA, normalB, normalC, normalD, label};
		normalizedSet.emplace_back(normalizedIndex);
	}

	return normalizedSet;
}

void sortAndDisplayData(std::vector<double> dataSet) {
	std::sort(dataSet.begin(), dataSet.end());

	std::cout << "\nSORTED DISTANCES: \n";

	for (const auto& distance : dataSet) {
		std::cout << distance << '\n';
	}
}

int main() {
	Data newExample{5.0, 2.8, 4.6, 0.7, 'X'};

	std::vector<Data> normalizedData = normalizeData(arr);

	sortAndDisplayData(findEuclideanDistance(arr, newExample));
	sortAndDisplayData(findManhantanDistance(arr, newExample));

	sortAndDisplayData(
	    findEuclideanDistance(normalizedData, normalizedData[normalizedData.size() - 1]));

	sortAndDisplayData(
	    findManhantanDistance(normalizedData, normalizedData[normalizedData.size() - 1]));

	return 0;
}
