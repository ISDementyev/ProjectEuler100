#include <iostream>
#include "Helpers.h"

int Problem9()
{
    int i = 1, Term, Sum = 0;

    while (Helpers::FibonacciBinet(i) < 4000000)
    {
        Term = Helpers::FibonacciBinet(i);

        if (Term % 2 == 0)
        {
            Sum += Term;
        }
        i++;
    }
    return Sum;
}

int main()
{
    std::cout << Problem9() << "\n";
    return 0;
}
