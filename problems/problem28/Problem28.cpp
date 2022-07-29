#include <iostream>

int Problem28(int n)
{
    n = (n - 1) / 2;

    int start = 3, times, sum = 3;

    for (int i = 1; i < n + 1; i++)
    {
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
            sum += start;
        }
    }
    return sum + 1;
}

int main()
{
    std::cout << Problem28(1001) << "\n";
    return 0;
}
