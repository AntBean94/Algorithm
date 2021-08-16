# 24강 단순 문자열 매칭

## String Matching

---

1. 부모 문자열과 패턴 문자열을 비교하는 알고리즘
2. 부모 문자열과 패턴 문자열을 하나씩 비교하고 다른부분이 생기면 비교할 부모 문자열을 한 칸 뒤로 이동한다.

---

**Python**

```python
# 24강 단순 문자열 매칭 (String Matching) 예제

'''
예제

Hello World!
Wor

'''

parent = input()
pattern = input()

def matching(parent, pattern):
    parent_size = len(parent)
    pattern_size = len(pattern)
    for i in range(parent_size - pattern_size):
        result = i
        for j in range(pattern_size):
            if parent[i + j] != pattern[j]:
                result = -1
                break
        if result > -1:
            return result
    return -1

result = matching(parent, pattern)
if result > -1:
    print("{}번째에서 매칭되었습니다.".format(result))
else:
    print("매칭되지 않았습니다.")
```



**C++**

```C++
#include <iostream>

using namespace std;

int findString(sting parent, string pattern) {
  int parentSize = parent.size();
  int patternSize = pattern.size();
  for(int i = 0; i <= parentSize - patternSize; i++) {
    bool finded = true;
    for(int j = 0; j < patternSize; j++) {
      if(parent[i + j] != pattern[j]) {
        finded = false;
        break;
      }
    }
    if(finded) {
      return i;
    }
  }
  return -1;
}

int main(void) {
  string parent = "Hello World!";
  string pattern = "llo W";
  int result = findString(parent, pattern);
  if(result == -1) {
    printf("찾을 수 없습니다.");
  } else {
    printf("%d번째에서 찾았습니다.", result + 1);
  }
  return 0;
}
```



## 정리

원리와 구현은 간단하지만 효율성이 떨어지는 알고리즘

**시간 복잡도**

**O(N * M)**  => (N: 부모 문자열의 길이, M: 패턴 문자열의 길이)

