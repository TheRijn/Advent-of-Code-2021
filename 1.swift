var depths: [Int] = []

while let line = readLine() {
    depths.append(Int(line)!)
}

var total = 0

for i in 1..<depths.count {
    if depths[i - 1] < depths[i] {
        total += 1
    }
}

print("a:", total)

var prev = 1000000
total = 0

for i in 1..<depths.count - 2 {
    let new = depths[i..<i + 3].reduce(0, +)

    if new > prev {
        total += 1
    }
    prev = new
}
print("b:", total)