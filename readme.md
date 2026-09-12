# Algorithm Practice

> 알고리즘 문제 정리

## 회독 기록

처음 푼 문제는 자동으로 `1회독`으로 집계합니다. 같은 문제를 다시 풀었을 때 아래 명령을 실행하면 문제 폴더의 `review.json`에 다음 회독과 날짜가 기록됩니다.

```bash
npm run review -- 154540
```

문제 ID 대신 제목으로 검색하거나 날짜를 직접 지정할 수도 있습니다.

```bash
npm run review -- "무인도 여행"
npm run review -- 154540 --date=2026-09-12
```

파일을 만들지 않고 대상을 먼저 확인하려면 `--dry-run`을 사용합니다.

```bash
npm run review -- 154540 --dry-run
```
