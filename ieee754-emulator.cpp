#include <iostream>
#include <unordered_map>
#include <vector>
#include <bitset>
#include <cstdint>  
#include <cstring>  

using namespace std;

uint32_t hexToUint32(const string &hex) {
    uint32_t result;
    sscanf(hex.c_str(), "%x", &result);
    return result;
}

uint32_t fmaOperation(uint32_t a, uint32_t b, uint32_t c) {
    float fa, fb, fc, fresult;
    memcpy(&fa, &a, sizeof(float));
    memcpy(&fb, &b, sizeof(float));
    memcpy(&fc, &c, sizeof(float));
    fresult = fa * fb + fc;
    uint32_t result;
    memcpy(&result, &fresult, sizeof(uint32_t));
    return result;
}

uint32_t nandOperation(uint32_t a, uint32_t b) {
    return ~(a & b);
}

int extractBits(uint32_t value, int j, int b) {
    return (value >> j) & ((1 << b) - 1);
}

int main() {
    int T;
    cin >> T;
    vector<uint32_t> results(T);

    for (int t = 0; t < T; ++t) {
        string c0_hex;
        cin >> c0_hex;
        uint32_t c0 = hexToUint32(c0_hex);

        int L;
        cin >> L;
        vector<vector<uint32_t>> LUT(L);
        for (int i = 0; i < L; ++i) {
            int size;
            cin >> size;
            LUT[i].resize(size);
            for (int j = 0; j < size; ++j) {
                string hex_value;
                cin >> hex_value;
                LUT[i][j] = hexToUint32(hex_value);
            }
        }

        int Q;
        cin >> Q;
        vector<uint32_t> C = {c0};
        for (int i = 0; i < Q; ++i) {
            char cmd;
            cin >> cmd;
            if (cmd == 'C') {
                string h;
                cin >> h;
                C.push_back(hexToUint32(h));
            } else if (cmd == 'N') {
                int x, y;
                cin >> x >> y;
                C.push_back(nandOperation(C[x], C[y]));
            } else if (cmd == 'F') {
                int x, y, z;
                cin >> x >> y >> z;
                C.push_back(fmaOperation(C[x], C[y], C[z]));
            } else if (cmd == 'L') {
                int i, j, b;
                cin >> i >> j >> b;
                int index = extractBits(C[0], j, b);
                C.push_back(LUT[i][index]);
            }
        }

        results[t] = C.back();
    }

    for (uint32_t result : results) {
        printf("%08x\n", result);
    }

    return 0;
}