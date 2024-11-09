#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int largestRectangleArea(vector<int>& heights) {
    stack<int> indexStack;
    int maxArea = 0;
    heights.push_back(0); 

    for (int i = 0; i < heights.size(); ++i) {
        while (!indexStack.empty() && heights[i] < heights[indexStack.top()]) {
            int height = heights[indexStack.top()];
            indexStack.pop();
            int width = i - (indexStack.empty() ? 0 : indexStack.top() + 1);
            maxArea = max(maxArea, height * width);
        }
        indexStack.push(i);
    }

    heights.pop_back(); 
    return maxArea;
}

int maxRectangleAreaWithOneModification(int numBars, int newHeight, vector<int>& heights) {
    int baseMaxArea = largestRectangleArea(heights);
    int maxAreaWithModification = baseMaxArea;

    vector<int> left(numBars, 0), right(numBars, 0);
    
    for (int i = 0; i < numBars; ++i) {
        if (i == 0 || heights[i] >= heights[i - 1]) {
            left[i] = i;  
        } else {
            left[i] = left[i - 1];  
        }
    }
    
    for (int i = numBars - 1; i >= 0; --i) {
        if (i == numBars - 1 || heights[i] >= heights[i + 1]) {
            right[i] = i;  
        } else {
            right[i] = right[i + 1];  
        }
    }

    for (int i = 0; i < numBars; ++i) {
        int originalValue = heights[i];
        if (originalValue != newHeight) {
            heights[i] = newHeight;  
            
            int width = right[i] - left[i] + 1;
            int modifiedArea = newHeight * width;  
            maxAreaWithModification = max(maxAreaWithModification, modifiedArea);

            heights[i] = originalValue;  
        }
    }

    return maxAreaWithModification;
}

int main() {
    int numBars, newHeight;
    cin >> numBars >> newHeight;
    vector<int> heights(numBars);
    for (int i = 0; i < numBars; ++i) {
        cin >> heights[i];
    }

    cout << maxRectangleAreaWithOneModification(numBars, newHeight, heights) << endl;

    return 0;
}
