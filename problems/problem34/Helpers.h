#pragma once

class Helpers
{
public:
	static unsigned long long Factorial(int n)
	{
		if (n == 0 || n == 1)
		{
			return 1;
		}

		unsigned long long Fac = 1;

		for (int i = 1; i <= n; i++)
		{
			Fac *= i;
		}

		return Fac;
	}
};
