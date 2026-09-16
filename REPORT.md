# Course Evaluation Project Report: Personal Expense Tracker

## 1. Project Objective & Scope
The purpose of this software implementation task is to build a high-performance personal accounting tracking engine using a Command-Line Interface (CLI). The program manages financial inputs, aggregates categorical item costs, and dynamically evaluates whether the user has retained active net savings or exceeded their defined monetary budget ceiling limits.

## 2. Technical Design & Architecture
* **Interface Layer:** Built with a continuous interactive logical while loop that takes inputs via natural CLI terminal interaction hooks.
* **Storage Layer:** Uses a customized plain-text parsing algorithm (expenses.txt) separating internal fields using custom || text layout boundary flags to achieve database persistence without depending on external parsing libraries.
* **Logic Calculations:** Uses iterative evaluation math checks to accurately track structural data differences between budget constraints and ongoing expenditure values to pinpoint precise remaining savings.
