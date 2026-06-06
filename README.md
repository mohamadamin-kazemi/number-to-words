# Number to Words Converter

A Python utility that converts non-negative integers into their English word representation. This project demonstrates recursion, clean code structure, and scalable number parsing logic for handling large numeric values such as thousands, millions, and billions.

---

## Description

This project takes a non-negative integer input from the user and converts it into a human-readable English phrase. It supports numbers from 0 up to the trillions and is designed with extensibility and readability in mind.

The conversion logic is built using:
* Predefined mappings for numbers under 20
* Tens-based formatting for numbers under 100
* Recursive decomposition for larger magnitudes (hundred, thousand, million, etc.)

---

## Project Structure

```text
NUMBER-TO-WORDS/
├── src/
│   ├── constants.py
│   └── main.py
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/mohamadamin-kazemi/number-to-words.git](https://github.com/mohamadamin-kazemi/number-to-words.git)
cd number-to-words
```

### 2. Run the Script
No external dependencies are required.

## Usage

Run the program using Python:

```bash
python src/main.py
```

### Example Interaction
```text
Enter a non-negative integer: 4521
Four Thousand Five Hundred Twenty One
```

## Code Overview

### Conversion Logic
* Numbers **0–19** are directly mapped using a lookup table (`UNDER_20`)
* Numbers **20–99** are constructed using `TENS` and remainder logic
* Numbers **100+** are recursively broken down using `ABOVE_100` magnitude mapping

### Example
For input `1234`:

* `1000` → "One Thousand"
* `234` → "Two Hundred Thirty Four"
* **Combined** → "One Thousand Two Hundred Thirty Four"

## Error Handling

The program intelligently handles:
* ❌ Negative numbers (raises `ValueError`)
* ❌ Non-integer inputs
* ❌ Invalid or empty input strings

## License

This project is licensed under the MIT License.
See the `LICENSE` file for more information.