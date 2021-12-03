//
//  main.swift
//  AoC2
//
//  Created by Marijn Doeve on 01-12-2021.
//

import Foundation

var dept = 0
var horizontalPosition = 0

let fileContent = try! String(contentsOfFile: CommandLine.arguments[1])
for line in fileContent.trimmingCharacters(in: .newlines).components(separatedBy: .newlines) {
    let parts = line.components(separatedBy: " ")
    
    let direction = parts[0]
    let number = Int(parts[1])!
    
    switch direction {
    case "forward":
        horizontalPosition += number
    case "down":
        dept += number
    case "up":
        dept -= number
    default: break
    }
}

print("a:", horizontalPosition * dept)

var aim = 0
var deptB = 0
var horizontalPositionB = 0


for line in fileContent.trimmingCharacters(in: .newlines).components(separatedBy: .newlines) {
    let parts = line.components(separatedBy: .whitespaces)
    
    let direction = parts[0]
    let number = Int(parts[1])!
    
    switch direction {
    case "up":
        aim -= number
    case "down":
        aim += number
    case "forward":
        horizontalPositionB += number
        deptB += aim * number
    default: break
    }
}

print("b:", horizontalPositionB * deptB)
