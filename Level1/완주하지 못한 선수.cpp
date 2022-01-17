#include <string>
#include <vector>
#include <map> // Dictionary

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> label;
    
    // 참여 선수 카운팅
    for(auto c : completion)
        label[c] += 1;
    
    // 완주 선수 카운팅
    for(auto p : participant)
    {
        label[p] -= 1;
        if(label[p] < 0)
            answer += p;
    }
    
    return answer;
}
