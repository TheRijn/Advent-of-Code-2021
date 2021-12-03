//
//  main.swift
//  AoC1
//
//  Created by Marijn Doeve on 01-12-2021.
//

import Foundation

var depths = [Int]()

let fileContent = try! String(contentsOfFile: CommandLine.arguments[1])
for line in fileContent.components(separatedBy: .newlines) {
    if let line = Int(line) {
        depths.append(line)
    }
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
