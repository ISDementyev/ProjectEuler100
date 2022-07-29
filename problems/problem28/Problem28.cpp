#include <iostream>
#include <vector>

int Problem28(int n)
{
    n = (n - 1) / 2;

    std::vector<int> diagonals = { 3 };
    int start = 3;

    for (int i = 1; i < n + 1; i++)
    {
        int times;

        if (i == 1)
        {
            times = 2;
        }
        else
        {
            times = 3;
        }

        for (int j = 0; j < times + 1; j++)
        {
            start += i * 2;
            diagonals.push_back(start);
        }
    }

    int sum = 0;

    for (int d : diagonals)
    {
        sum += d;
    }

    return sum + 1;
}

int main()
{
    std::cout << Problem28(1001) << "\n";
    return 0;
}
