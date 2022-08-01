#include <iostream>
#include "Helpers.h"

int Problem34(int n)
{
    int Total = 0;

    for (int i = 10; i <= n; i++)
    {
        int FacSum = 0;

        for (char Digit : std::to_string(i))
        {
            FacSum += Helpers::Factorial((int)Digit - 48); // Use ASCII + typecasting to our advantage
        }

        if (FacSum == i)
        {
            Total += i;
        }
    }
    return Total;
}

int main()
{
    std::cout << Problem34(100000);
}
