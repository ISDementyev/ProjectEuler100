#pragma once

#include <cmath>

class Helpers
{
public:
	static int FibonacciBinet(int n)
	{
		double Root5 = std::sqrt(5);
		double Phi = (1 + Root5) / 2;
		double PhiN = (1 - Root5) / 2;

		return std::round((std::pow(Phi, n) - std::pow(PhiN, n)) / Root5);
	}
};
