# 25강 KMP

## Knuth-Morris-Pratt 문자열 알고리즘

---

1. 변수 초기화
2. 실패함수 (Fail Function)
   - 접두사, 접미사를 비교
   - 문자열의 길이별로 일치하는 접두사, 접미사의 길이를 테이블에 저장
   - 문자열 매칭시 문자가 일치하지 않을때 패턴 문자열의 위치를 결정한다.
3. KMP 문자열 매칭
   - i, j 두개의 위치로 문자열을 비교
   - i 는 부모 문자열을 하나씩 탐색
   - j 는 패턴 문자열을 하나씩 탐색
   - 불일치시 j를 실패함수에 넣고 새로운 위치 반환

---

**Python**

```python
# 25강 KMP(Knuth-Morris-Pratt) 문자열 알고리즘 예제

'''
예제

ababacabacaabacaaba
abacaaba

'''

# 초기값 설정
parent = input()
pattern = input()
parent_size = len(parent)
pattern_size = len(pattern)
fail_table = [0] * (pattern_size)

# 실패함수
def failFunc(pattern):
    cnt = 0
    j = 0
    for i in range(1, pattern_size):
        if pattern[i] == pattern[j]:
            cnt += 1
            j += 1
        else:
            cnt = 0
            j = 0
            if pattern[j] == pattern[i]:
                cnt += 1
                j += 1
        fail_table[i] = cnt
# 실패함수 실행
failFunc(pattern)

# 문자열 매칭 함수
def kmpMatching(parent, pattern):
    ans = []
    j = 0
    for i in range(parent_size):
        if parent[i] == pattern[j]:
            j += 1
        else:
            j = fail_table[j]
            if parent[i] == pattern[j]:
                j += 1
        if j == pattern_size:
            ans.append(i - j + 1)
            j = fail_table[j - 1]
    return ans

# KMP 문자열 매칭 함수 실행
print(kmpMatching(parent, pattern))
```



**C++**

```C++
#include <iostream>
#include <vector>

using namespace std;

vector<int> makeTable(string pattern) {
  int patternSize = pattern.size();
  vector<int> table(patternSize, 0);
  int j = 0;
  for(int i = 1; i < patternSize; i++) {
    while(j > 0 && pattern[i] != pattern[j]) {
      j = table[j - 1];
    }
    if(pattern[i] == pattern[j]) {
      table[i] = ++j;
    }
  }
  return table;
}

void KMP(string parent, streing pattern) {
  vector<int> table = makeTable(pattern);
  int parentSize = parent.size();
  int patternSize = pattern.size();
  int j = 0;
  for(int i = 0; i < parentSize; i++) {
    while(j > 0 && parent[i] != pattern[j]) {
      j = table[j - 1];
    }
    if(parent[i] == pattern[j]) {
      if(j == patternSize - 1) {
        printf("%d번째에서 찾았습니다.\n", i - patternSize + 2);
        j = table[j];
      } else {
        j++;
      }
    }
  }
}

int main(void) {
  string pattern = "abacaaba";
  vector<int> table = makeTable(pattern);
  for(int i = 0; i < table.size(); i++) {
    printf("%d ", table[i]);
  }
  return 0;
}
```



## 정리

시간복잡도

O(M + N)

M: 부모 문자열의 길이

N: 패턴 문자열의 길이