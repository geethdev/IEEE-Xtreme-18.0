#include <bits/stdc++.h>
using namespace std;

const int MODULO = 998244353;

int numPairs;
vector<int> cardColors, rules, boundaries;
map<pair<int, vector<int>>, int> memoization;

int findArrangements(int position, vector<int>& availableNumbers) {
    if (position == numPairs) return 1;

    pair<int, vector<int>> state = {position, availableNumbers};
    if (memoization.count(state)) return memoization[state];

    int arrangements = 0;
    int cardIndex = 2 * position;

    vector<int> firstCardOptions;
    if (cardColors[cardIndex] != -1) firstCardOptions = {cardColors[cardIndex]};
    else firstCardOptions = availableNumbers;

    for (int firstCard : firstCardOptions) {
        if (cardColors[cardIndex] != -1 && cardColors[cardIndex] != firstCard) continue;

        vector<int> secondCardOptions;
        if (cardColors[cardIndex + 1] != -1) secondCardOptions = {cardColors[cardIndex + 1]};
        else {
            secondCardOptions = availableNumbers;
            if (find(secondCardOptions.begin(), secondCardOptions.end(), firstCard) != secondCardOptions.end())
                secondCardOptions.erase(find(secondCardOptions.begin(), secondCardOptions.end(), firstCard));
        }

        for (int secondCard : secondCardOptions) {
            if (cardColors[cardIndex + 1] != -1 && cardColors[cardIndex + 1] != secondCard) continue;
            if (firstCard == secondCard) continue;

            int smallerCard = min(firstCard, secondCard);
            int largerCard = max(firstCard, secondCard);

            if ((rules[position] == 0 && boundaries[position] == smallerCard) ||
                (rules[position] == 1 && boundaries[position] == largerCard)) {

                vector<int> updatedAvailableNumbers = availableNumbers;
                if (cardColors[cardIndex] == -1)
                    updatedAvailableNumbers.erase(find(updatedAvailableNumbers.begin(), updatedAvailableNumbers.end(), firstCard));
                if (cardColors[cardIndex + 1] == -1)
                    updatedAvailableNumbers.erase(find(updatedAvailableNumbers.begin(), updatedAvailableNumbers.end(), secondCard));

                arrangements = (arrangements + findArrangements(position + 1, updatedAvailableNumbers)) % MODULO;
            }
        }
    }

    return memoization[state] = arrangements;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> numPairs;
    cardColors.resize(2 * numPairs);
    rules.resize(numPairs);
    boundaries.resize(numPairs);

    vector<int> availableNumbers;
    vector<bool> isUsed(2 * numPairs + 1, false);

    for (int i = 0; i < 2 * numPairs; i++) {
        cin >> cardColors[i];
        if (cardColors[i] != -1) isUsed[cardColors[i]] = true;
    }

    for (int i = 1; i <= 2 * numPairs; i++) {
        if (!isUsed[i]) availableNumbers.push_back(i);
    }

    for (int i = 0; i < numPairs; i++) cin >> rules[i];
    for (int i = 0; i < numPairs; i++) cin >> boundaries[i];

    cout << findArrangements(0, availableNumbers) << endl;

    return 0;
}
