# 26강 라빈 카프

## Rabin-Karp 문자열 알고리즘

---

**라빈 카프 알고리즘은 문자열의 해시 값을 비교하여 그 일치 여부를 검사하는 알고리즘**

긴 데이터를 그것을 상징하는 짧은 데이터로 바꿔주는 기법이며, 항상 빠르지는 않지만 일반적인 경우 빠르게 작동하는 간단한 구조의 문자열 매칭 알고리즘

1. 해시값을 활용해 매칭 여부를 판별하는 알고리즘

2. 초기값으로 패턴 문자열과 부모 문자열의 해시값을 구한다.

   - 각 문자의 해시값: ord(문자열) * 2^i
   - 각 문자의 해시값을 모두 더한값이 문자열의 해시값
   - ex) 2^3 x ord(a) + 2^2 x ord(b) + 2^1 x ord(a) + 2^0 x ord(d)

3. 문자열을 하나씩 탐색하며 부모 해시값을 변경하고 패턴 해시값과 비교

   - 부모 해시값을 변경할 때 다음의 수식을 적용

     2 x (부모 해시값 - 맨앞 문자의 해시값) + 다음 문자의 해시값

4. 부모 해시값과 패턴 해시값이 일치하면 문자가 실제로 일치하는지 확인



해시값이 일치할 확률이 굉장히 낮기 때문에 대부분의 상황에서 O(N)의 시간복잡도를 보인다.

단, 오버플로가 발생할 수 있기때문에 나머지(mod)연산을 추가하는 것도 좋은 방법이다.

---

**Python**

```python
# 26강 라빈 카프 (Rabin-Karp) 문자열 매칭 알고리즘 예제

'''
예제

ababacabacaabacaaba
abacaaba

'''

P = input()
S = input()
P_size = len(P)
S_size = len(S)
P_hash = 0
S_hash = 0
ans = []

# 초기 해시값 계산
cnt = S_size - 1
for i in range(S_size):
    P_hash += ord(P[i]) * (2 ** cnt)
    S_hash += ord(S[i]) * (2 ** cnt)
    cnt -= 1

# 초기 해시값 비교
if P_hash == S_hash:
    if P[:S_size] == S:
        ans.append(0)

# 문자열 비교
for i in range(P_size - S_size):
    # 해시값 변경
    P_hash = 2 * (P_hash - ord(P[i]) * (2 ** (S_size - 1))) + ord(P[i + S_size])
    # 해시값이 같다면 문자열 비교
    if P_hash == S_hash:
        for j in range(S_size):
            if P[i + j + 1] != S[j]:
                break
            if j == S_size - 1:
                ans.append(i + 1)

print(ans)
```



**C++**

```C++
#include <iostream>

using namespace std;

void findString(string parent, string pattern) {
  int parentSize = parent.size();
  int patternSize = pattern.size();
  int parentHash = 0, patternHash = 0; power = 1;
  for(int i = 0; i <= parentSize - patternSize; i++) {
    if(i == 0) {
      for(int j = 0; j < patternSize; j++) {
        parentHash += parent[patternSize - 1 - j] * power;
        patternHash += pattern[patternSize - 1 - j] * pawer;
        if(j < patternSize - 1) power *= 2;
      } else {
        parentHash = 2 * (parentHash - parent[i - 1] * power) + parent[patternSize - 1 + i];
      }
      if(parentHash == patternHash) {
        bool finded = true;
        for(int j = 0; j < patternSize; j++) {
          if(parent[i + j] != pattern[j]) {
            finded = false;
            break;
          }
        }
        if(finded) {
          printf("%d번째에서 발견했습니다.\ㅜ", i + 1);
        }
      }
    }
  }
}

int main(void) {
  string parent = "ababacabacaabacaaba";
  string pattern = "abacaaba";
  findString(parent, pattern);
  return 0;
}
```

