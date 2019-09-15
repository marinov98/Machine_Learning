#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>

// NOTE TO SELF: should have written this in js instead :p

// For the each individual point
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

// For when the distance is calculated
struct Result {
	double distance;
	char label;

	Result(double distance_, char label_) : distance(distance_), label(label_) {}

	friend std::ostream& operator<<(std::ostream& out, Result result) {
		out << "Distance: " << result.distance << " --> " << result.label;

		return out;
	}
};

// IMPORTANT: Point Marked classified as 'X' is the new example point
std::vector<Data> arr = {{5.1, 3.5, 1.3, 0.2, 'A'}, {5.7, 3.4, 1.3, 0.2, 'C'},
                         {4.7, 3.1, 1.6, 0.2, 'A'}, {5.0, 4.6, 1.4, 0.1, 'B'},
                         {5.9, 3.3, 4.0, 1.3, 'C'}, {6.5, 2.7, 4.6, 1.5, 'A'},
                         {5.7, 2.8, 4.4, 1.3, 'B'}, {6.3, 3.3, 4.7, 1.4, 'C'},
                         {4.7, 2.4, 3.2, 1.0, 'A'}, {7.7, 3.6, 6.7, 2.2, 'B'},
                         {7.7, 2.6, 6.5, 2.3, 'C'}, {6.0, 2.2, 5.0, 1.4, 'A'},
                         {6.9, 3.2, 5.7, 9.3, 'B'}, {5.6, 2.2, 4.6, 2.0, 'C'},
                         {5.0, 2.8, 4.6, 0.7, 'X'}};

double calculateEuclideanDistance(Data arrPoint, Data newExample) {
	double squaredA = (arrPoint.a - newExample.a) * (arrPoint.a - newExample.a);
	double squaredB = (arrPoint.b - newExample.b) * (arrPoint.b - newExample.b);
	double squaredC = (arrPoint.c - newExample.c) * (arrPoint.c - newExample.c);
	double squaredD = (arrPoint.d - newExample.d) * (arrPoint.d - newExample.d);

	double total = squaredA + squaredB + squaredC + squaredD;

	// Square root and find the euclidean distance
	return std::sqrt(total);
}

double calculateManhattanDistance(Data arrPoint, Data newExample) {
	double absA = std::abs((arrPoint.a - newExample.a));
	double absB = std::abs((arrPoint.b - newExample.b));
	double absC = std::abs((arrPoint.c - newExample.c));
	double absD = std::abs((arrPoint.d - newExample.d));

	return (absA + absB + absC + absD);
}

double calculateChebyshevDistance(Data arrPoint, Data newExample) {
	double max = std::numeric_limits<double>::min();

	double absA = std::abs((arrPoint.a - newExample.a));

	double absB = std::abs((arrPoint.b - newExample.b));
	double absC = std::abs((arrPoint.c - newExample.c));
	double absD = std::abs((arrPoint.d - newExample.d));

	return std::max({absA, absB, absC, absD});
}

std::vector<Result> findEuclideanDistances(std::vector<Data> dataArr, Data newExample) {
	std::vector<Result> data;
	data.reserve(dataArr.size());
	for (const Data& dataPoint : dataArr) {
		double eDistance = calculateEuclideanDistance(dataPoint, newExample);

		// add calculated distance and the label of the current data point
		data.emplace_back(Result{eDistance, dataPoint.label});
	}

	std::cout << "\nExample Point " << newExample;

	return data;
}

std::vector<Result> findManhantanDistances(std::vector<Data> dataArr, Data newExample) {
	std::vector<Result> data;
	data.reserve(dataArr.size());
	for (const Data& dataPoint : dataArr) {
		double mDistance = calculateManhattanDistance(dataPoint, newExample);

		data.emplace_back(Result{mDistance, dataPoint.label});
	}

	std::cout << "\nExample Point " << newExample;

	return data;
}

std::vector<Result> findChebyshevDistances(std::vector<Data> dataArr, Data newExample) {
	std::vector<Result> data;

	data.reserve(dataArr.size());

	for (const Data& dataPoint : dataArr) {
		double cDistance = calculateChebyshevDistance(dataPoint, newExample);

		data.emplace_back(Result{cDistance, dataPoint.label});
	}

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

char classifyKthNearestNeighbors(std::vector<Result> dataSet, int k) {
	if (dataSet.size() < k + 1)
		throw std::underflow_error("dataSet is too small!");

	int maxCountA = 0;
	int maxCountB = 0;
	int maxCountC = 0;

	// K + 1 Because the first point will always be the example point
	for (int i = 0; i < k + 1; i++) {
		if (dataSet[i].label == 'A')
			maxCountA++;
		else if (dataSet[i].label == 'B')
			maxCountB++;
		else if (dataSet[i].label == 'C')
			maxCountC++;
	}

	int targetClassification = std::max({maxCountA, maxCountB, maxCountC});

	if (targetClassification == maxCountA)
		return 'A';
	else if (targetClassification == maxCountB)
		return 'B';
	else if (targetClassification == maxCountC)
		return 'C';
}

void sortAndDisplayData(std::vector<Result> dataSet) {
	std::sort(dataSet.begin(), dataSet.end(),
	          [&](Result a, Result b) { return a.distance < b.distance; });

	std::cout << "\nSORTED DISTANCES: \n";

	for (const auto& distance : dataSet)
		std::cout << distance << '\n';

	// Classify sorted data

	std::cout << "\nCLASSIFICATIONS:\n";
	// 1th index instead of 0th since the first one is the example point
	std::cout << "Knn classification for k = 1: " << dataSet[1].label << '\n';
	std::cout << "Knn classification for k = 4: " << classifyKthNearestNeighbors(dataSet, 4)
	          << '\n';
	std::cout << "Knn classification for k = 6: " << classifyKthNearestNeighbors(dataSet, 6)
	          << '\n';
}

int main() {
	Data newExample{5.0, 2.8, 4.6, 0.7, 'X'};

	std::vector<Data> normalizedData = normalizeData(arr);

	std::cout << "\nEUCLIDEAN distances" << '\n';

	sortAndDisplayData(findEuclideanDistances(arr, newExample));

	std::cout << "\nNORMALIZED EUCLIDEAN distances" << '\n';
	sortAndDisplayData(
	    findEuclideanDistances(normalizedData, normalizedData[normalizedData.size() - 1]));

	std::cout << "\nMANHATTAN distances" << '\n';
	sortAndDisplayData(findManhantanDistances(arr, newExample));

	std::cout << "\nNORMALIZED MANHATTAN distances" << '\n';
	sortAndDisplayData(
	    findManhantanDistances(normalizedData, normalizedData[normalizedData.size() - 1]));

	std::cout << "\nCHEBYSHEV distances" << '\n';
	sortAndDisplayData(findChebyshevDistances(arr, newExample));

	std::cout << "\nNORMALIZED CHEBYSHEV distances" << '\n';
	sortAndDisplayData(
	    findChebyshevDistances(normalizedData, normalizedData[normalizedData.size() - 1]));

	return 0;
}
