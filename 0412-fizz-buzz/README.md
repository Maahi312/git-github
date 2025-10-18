<h2><a href="https://leetcode.com/problems/fizz-buzz/">412. Fizz Buzz</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <em>a string array </em><code>answer</code><em> (<strong>1-indexed</strong>) where</em>:</p>

<ul>
	<li><code>answer[i] == &quot;FizzBuzz&quot;</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>.</li>
	<li><code>answer[i] == &quot;Fizz&quot;</code> if <code>i</code> is divisible by <code>3</code>.</li>
	<li><code>answer[i] == &quot;Buzz&quot;</code> if <code>i</code> is divisible by <code>5</code>.</li>
	<li><code>answer[i] == i</code> (as a string) if none of the above conditions are true.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["1","2","Fizz"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> ["1","2","Fizz","4","Buzz"]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🧠 Intuition

The task is to generate a list of strings for numbers from 1 to n with specific substitution rules:

Numbers divisible by 3 → "Fizz"

Numbers divisible by 5 → "Buzz"

Numbers divisible by both 3 and 5 → "FizzBuzz"
Otherwise, return the number itself as a string.

This tests basic modulus logic, conditional statements, and simple string handling.

---

# ⚙️ Approach

Initialize an empty list result = [] to hold the output.

Iterate through each integer i from 1 to n (inclusive).

# Check divisibility using the modulus % operator:

If i % 3 == 0 and i % 5 == 0 → append "FizzBuzz".

Else if i % 3 == 0 → append "Fizz".

Else if i % 5 == 0 → append "Buzz".

Otherwise → append str(i) (the number itself as a string).

Return the result list after the loop.

# 💻 Example
Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]


# Explanation:

1 → not divisible → "1"

2 → not divisible → "2"

3 → divisible by 3 → "Fizz"

4 → not divisible → "4"

5 → divisible by 5 → "Buzz"

---

# ⏱️ Complexity

Time Complexity: O(n) → Each number from 1 to n is processed once.

Space Complexity: O(n) → The output list stores n strings.
