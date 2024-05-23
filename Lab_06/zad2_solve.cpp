#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <limits>
#include <fstream>
#include <sstream>

struct Point {
    int x, y;
};

double distance(const Point& a, const Point& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double totalDistance(const std::vector<Point>& points, const std::vector<int>& cycle) {
    double dist = 0.0;
    for (size_t i = 0; i < cycle.size(); ++i) {
        int j = (i + 1) % cycle.size();
        dist += distance(points[cycle[i]], points[cycle[j]]);
    }
    return dist;
}

void swapEdges(std::vector<int>& cycle, int a, int b) {
    std::reverse(cycle.begin() + a, cycle.begin() + b + 1);
}

std::vector<Point> readPointsFromFile(const std::string& filename) {
    std::vector<Point> points;
    std::ifstream file(filename);
    if (file.is_open()) {
        int x, y;
        while (file >> x >> y) {
            points.push_back({x, y});
        }
        file.close();
    } else {
        std::cerr << "Could not open file " << filename << std::endl;
    }
    return points;
}

void writeResultToFile(const std::string& filename, double best_distance, const std::vector<int>& best_cycle) {
    std::ofstream file(filename);
    if (file.is_open()) {
        // file << "Najkrótszy znaleziony cykl ma długość: " << best_distance << "\n";
        // file << "Cykl: ";
        for (int i=0;i<best_cycle.size()-1;i+=2) {
            file << best_cycle[i] << " " << best_cycle[i+1] << "\n";
        }
        file.close();
    } else {
        std::cerr << "Could not open file " << filename << std::endl;
    }
}

int main() {
    std::vector<Point> points = readPointsFromFile("xqf131.dat");

    if (points.empty()) {
        std::cerr << "No points to process." << std::endl;
        return 1;
    }

    std::vector<int> cycle(points.size());
    for (size_t i = 0; i < points.size(); ++i) {
        cycle[i] = i;
    }

    std::srand(unsigned(std::time(0)));

    double T_initial = 0.1;
    double T_min = 0.0001;
    double cooling_rate = 0.999;

    std::random_shuffle(cycle.begin(), cycle.end());

    double current_distance = totalDistance(points, cycle);
    std::vector<int> best_cycle = cycle;
    double best_distance = current_distance;

    double T = T_initial;
    while (T > T_min) {
        for (int it = 0; it < 1000; ++it) {
            int a = std::rand() % points.size();
            int b = (a + 1 + std::rand() % (points.size() - 1)) % points.size();

            if (a > b) std::swap(a, b);

            std::vector<int> new_cycle = cycle;
            swapEdges(new_cycle, a, b);

            double new_distance = totalDistance(points, new_cycle);

            if (new_distance < current_distance || exp((current_distance - new_distance) / T) > (double)rand() / RAND_MAX) {
                cycle = new_cycle;
                current_distance = new_distance;

                if (current_distance < best_distance) {
                    best_cycle = cycle;
                    best_distance = current_distance;
                }
            }
        }
        
        T *= cooling_rate;
    }

    std::cout << "Najkrótszy znaleziony cykl ma długość: " << best_distance << std::endl;
    std::cout << "Cykl: ";
    for (int i : best_cycle) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    writeResultToFile("result.txt", best_distance, best_cycle);

    return 0;
}