#include <iostream>
#include <sstream>
#include <bitset>
#include <string>

using namespace std;

const char *hex_char_to_bin(char c)
{
    // TODO handle default / error
    switch (toupper(c))
    {
    case '0':
        return "0000";
    case '1':
        return "0001";
    case '2':
        return "0010";
    case '3':
        return "0011";
    case '4':
        return "0100";
    case '5':
        return "0101";
    case '6':
        return "0110";
    case '7':
        return "0111";
    case '8':
        return "1000";
    case '9':
        return "1001";
    case 'A':
        return "1010";
    case 'B':
        return "1011";
    case 'C':
        return "1100";
    case 'D':
        return "1101";
    case 'E':
        return "1110";
    case 'F':
        return "1111";
    default:
        return "error";
    }
}

string hex_str_to_bin_str(const string &hex)
{
    // TODO use a loop from <algorithm> or smth
    string bin;
    for (unsigned i = 0; i != hex.length(); ++i)
        bin += hex_char_to_bin(hex[i]);
    return bin;
}

string suma(const string &a_hex, const string &b_hex)
{
    stringstream ans;
    string a_bin = hex_str_to_bin_str(a_hex);
    string b_bin = hex_str_to_bin_str(b_hex);
    if (a_bin.length() != 8 || b_bin.length() != 8)
    {
        return "error";
    }
    bitset<8> a_bitset(a_bin);
    bitset<8> b_bitset(b_bin);
    bitset<8> xor_ab = a_bitset ^ b_bitset;
    ans << hex << uppercase << xor_ab.to_ulong();
    return ans.str();
    // return xor_ab.to_ulong();
}

string xtimes(const string &a_hex)
{
    stringstream ans;
    string bin = hex_str_to_bin_str(a_hex);
    bitset<8> bitset(bin);
    cout << bitset << endl;
    // cout << bitset.test(0) << endl;
    bitset = bitset << 1;
    cout << bitset << endl;
    ans << hex << uppercase << bitset.to_ulong();
    cout << ans.str() << endl;
    if (!bitset.test(0))
    {
        // cout << "zero" << endl;
        return ans.str();
    }
    else if (bitset.test(0))
    {
        string b = "1B";
        return suma(ans.str(), b);
    }

    return "error";
}

int main()
{
    string hex = "a3";
    string bin = hex_str_to_bin_str(hex);
    cout << "hex = " << hex << " bin = " << bin << endl;

    // Zad1:
    // Przyklad 1
    string a = "a3";
    string b = "f2";

    string suma_ab = suma(a, b);
    cout << "a ^ b = " << suma_ab << endl;

    // Przyklad 2
    a = "03";
    b = "1f";

    suma_ab = suma(a, b);
    cout << "a ^ b = " << suma_ab << endl;

    // Zad2:
    // Przykład 1
    a = "32";
    string x_times = xtimes(a);
    cout << "xa = " << x_times << endl;

    // Przykład 2
    a = "ff";
    x_times = xtimes(a);
    cout << "xa = " << x_times << endl;

    // Przykład 2
    a = "bc";
    x_times = xtimes(a);
    cout << "xa = " << x_times << endl;
    // bitset<8> b("01110010");
    // cout << "initial value: " << b << '\n';

    // while (b.any())
    // {
    //     while (!b.test(0))
    //     {
    //         b >>= 1;
    //     }
    //     cout << b << '\n';
    //     b >>= 1;
    // }
}