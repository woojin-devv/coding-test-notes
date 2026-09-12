import { execFileSync } from 'node:child_process'
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs'
import path from 'node:path'
import process from 'node:process'

const projectRoot = path.resolve(import.meta.dirname, '..')
const query = process.argv[2]?.trim()
const dateArgument = process.argv.find((argument) => argument.startsWith('--date='))?.slice('--date='.length)
const isDryRun = process.argv.includes('--dry-run')

if (!query) {
  console.error('사용법: npm run review -- <문제 ID 또는 제목> [--date=YYYY-MM-DD] [--dry-run]')
  process.exit(1)
}

const toSeoulDate = (value = new Date()) =>
  new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Seoul',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(value)

const reviewDate = dateArgument || toSeoulDate()

if (!/^\d{4}-\d{2}-\d{2}$/.test(reviewDate) || Number.isNaN(new Date(`${reviewDate}T00:00:00Z`).getTime())) {
  console.error(`올바르지 않은 날짜입니다: ${reviewDate}`)
  process.exit(1)
}

const walk = (directory) =>
  readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    if (entry.name === '.git' || entry.name === 'node_modules' || entry.name === '.DS_Store') return []
    const absolutePath = path.join(directory, entry.name)
    return entry.isDirectory() ? walk(absolutePath) : [absolutePath]
  })

const normalize = (value) => value.normalize('NFKC').replace(/[\s\u2000-\u200b]+/g, ' ').toLowerCase()
const normalizedQuery = normalize(query)
const readmes = walk(projectRoot).filter((filePath) => path.basename(filePath).toLowerCase() === 'readme.md')
const matches = readmes.filter((readmePath) => {
  const directoryName = normalize(path.basename(path.dirname(readmePath)))
  const markdown = normalize(readFileSync(readmePath, 'utf8'))
  const numericMatch = /^\d+$/.test(query)

  return numericMatch
    ? directoryName.startsWith(`${query}.`) || markdown.includes(`/lessons/${query}`)
    : directoryName.includes(normalizedQuery) || markdown.match(/^#\s+(.+)$/m)?.[1]?.includes(normalizedQuery)
})

if (matches.length === 0) {
  console.error(`문제를 찾지 못했습니다: ${query}`)
  process.exit(1)
}

if (matches.length > 1) {
  console.error(`여러 문제가 검색되었습니다. 문제 ID로 다시 실행해 주세요:\n${matches.map((file) => `- ${path.relative(projectRoot, path.dirname(file))}`).join('\n')}`)
  process.exit(1)
}

const readmePath = matches[0]
const problemDirectory = path.dirname(readmePath)
const reviewPath = path.join(problemDirectory, 'review.json')
const relativeReadmePath = path.relative(projectRoot, readmePath)
const rawHeading = readFileSync(readmePath, 'utf8').match(/^#\s+(.+)$/m)?.[1] || path.basename(problemDirectory)
const heading = rawHeading.replace(/^\[[^\]]+\]\s*/, '').replace(/\s+-\s+\d+\s*$/, '')

const getFirstSolvedDate = () => {
  const dates = execFileSync(
    'git',
    ['-C', projectRoot, 'log', '--follow', '--reverse', '--format=%aI', '--', relativeReadmePath],
    { encoding: 'utf8' },
  ).trim().split('\n').filter(Boolean)

  return dates[0]?.slice(0, 10) || reviewDate
}

const current = existsSync(reviewPath)
  ? JSON.parse(readFileSync(reviewPath, 'utf8'))
  : { problemId: query, reviews: [{ round: 1, date: getFirstSolvedDate() }] }

if (!Array.isArray(current.reviews)) {
  console.error(`${path.relative(projectRoot, reviewPath)}의 reviews 형식이 올바르지 않습니다.`)
  process.exit(1)
}

const lastRound = current.reviews.reduce((max, review) => Math.max(max, Number(review.round) || 0), 0)
const nextReview = { round: lastRound + 1, date: reviewDate }
const payload = {
  problemId: String(current.problemId || query),
  reviews: [...current.reviews, nextReview],
}

if (!isDryRun) writeFileSync(reviewPath, `${JSON.stringify(payload, null, 2)}\n`)
console.log(`${heading}: ${nextReview.round}회독을 ${isDryRun ? '기록할 예정입니다' : '기록했습니다'}. (${reviewDate})`)
console.log(`변경 파일: ${path.relative(projectRoot, reviewPath)}`)
