
# Goldbach's Conjecture Explanation

This script is designed to check whether an even number greater than 2 can be expressed as the sum of two prime numbers, as proposed by **Goldbach's Conjecture**. Goldbach's Conjecture states that every even integer greater than 2 can be written as the sum of two prime numbers. This Python script allows you to test this conjecture for individual numbers.

## Table of Contents

1. [What is Goldbach's Conjecture?](#what-is-goldbachs-conjecture)
2. [How the Script Works](#how-the-script-works)
3. [How to Use the Script](#how-to-use-the-script)
4. [Functions](#functions)
5. [Example Usage](#example-usage)
6. [Additional Notes](#additional-notes)

---

## What is Goldbach's Conjecture?

Goldbach's Conjecture is one of the oldest unsolved problems in number theory. It states that every **even integer greater than 2** can be written as the sum of two **prime numbers**. For example:

- **4** = 2 + 2
- **6** = 3 + 3
- **8** = 3 + 5
- **10** = 3 + 7 or 5 + 5

The conjecture has been tested for a huge range of numbers, and no counterexamples have been found, but it still remains unproven for all integers.

---

## How the Script Works

This Python script does the following:

1. **Checks if a number is prime**: The script includes a function to check if a given number is a prime number. Prime numbers are numbers that are only divisible by 1 and themselves (e.g., 2, 3, 5, 7, 11).
   
2. **Finds two primes that sum to the given even number**: The script takes an even number (greater than 2) and searches for two prime numbers that sum to that number, based on Goldbach's Conjecture.

### The main steps the script follows:
- **Input**: You provide an even number.
- **Prime Generation**: It generates a list of primes up to that number.
- **Searching for pairs**: It then checks if two primes from that list sum to the provided even number.
- **Output**: The script returns the two primes if they are found, otherwise an error message if the input is invalid (i.e., if it's not an even number greater than 2).

*idk why i made this lol*

---

## How to Use the Script

To use the script, follow these steps:

1. **Clone or Download** this repository to your local machine.
2. Open the terminal and navigate to the directory containing the `goldbach.py` file.
3. Run the script with Python 3:
   ```bash
   python3 goldbach.py
   ```
4. The script will ask you to enter an even number greater than 2.
5. It will then return two prime numbers that sum up to the input number (if valid).

*bruh*

---

## Functions

The script includes the following functions:

### 1. `is_prime(n)`
- **Purpose**: Checks if the given number `n` is a prime number.
- **Arguments**:
  - `n` (int): The number to check.
- **Returns**: `True` if `n` is prime, otherwise `False`.

*The `is_prime()` function is kinda basic... it just checks if the number is divisible by anything other than 1 or itself.*

### 2. `goldbach_check(even_num)`
- **Purpose**: Given an even number greater than 2, checks if it can be expressed as the sum of two prime numbers.
- **Arguments**:
  - `even_num` (int): The even number to check.
- **Returns**: A tuple of two primes that sum to `even_num`, or an error message if the number is invalid.

*to make sure that it works for different numbers, i made `goldbach_check()`. It checks if your number can be made by adding two primes. hopefully that was the correct way to do it*

---

## Example Usage

Here are some example inputs and outputs for the `goldbach_check()` function:

### Example 1:
```python
goldbach_check(4)
```
**Output**:
```
(2, 2)
```
Explanation: 4 can be expressed as the sum of the two prime numbers 2 and 2.

### Example 2:
```python
goldbach_check(6)
```
**Output**:
```
(3, 3)
```
Explanation: 6 can be expressed as the sum of the two prime numbers 3 and 3.

### Example 3:
```python
goldbach_check(8)
```
**Output**:
```
(3, 5)
```
Explanation: 8 can be expressed as the sum of the two prime numbers 3 and 5.

---

## Additional Notes

- The script uses the **Sieve of Eratosthenes** to generate primes efficiently up to the given number. This method is much faster than checking primality for each number individually.
- While Goldbach's Conjecture has been verified for very large numbers using computational methods, it still remains an unsolved problem in mathematics. This python script lets you test the conjecture for specific even numbers you choose, but will still not be able to solve it (yet?).
- If you input an odd number or a number less than or equal to 2, the script will return an error message.

* i love trying stuff i don't understand lmao *
---

## Contributing

if you wanna help go ahead, i desperately need help with this s**t anyway. fork and open a pull request, i will try checking it out!
---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
