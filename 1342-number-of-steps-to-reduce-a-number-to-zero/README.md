<h2><a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero">1342. Number of Steps to Reduce a Number to Zero</a></h2><h3>Easy</h3><hr><p>Given an integer <code>num</code>, return <em>the number of steps to reduce it to zero</em>.</p>

<p>In one step, if the current number is even, you have to divide it by <code>2</code>, otherwise, you have to subtract <code>1</code> from it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 14
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;
Step 1) 14 is even; divide by 2 and obtain 7.&nbsp;
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.&nbsp;
Step 4) 3 is odd; subtract 1 and obtain 2.&nbsp;
Step 5) 2 is even; divide by 2 and obtain 1.&nbsp;
Step 6) 1 is odd; subtract 1 and obtain 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 8
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;
Step 1) 8 is even; divide by 2 and obtain 4.&nbsp;
Step 2) 4 is even; divide by 2 and obtain 2.&nbsp;
Step 3) 2 is even; divide by 2 and obtain 1.&nbsp;
Step 4) 1 is odd; subtract 1 and obtain 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 123
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>6</sup></code></li>
</ul>


---

# 🧠 Intuition

The problem asks how many operations it takes to reduce a given number to zero using two rules:

If the number is even, divide it by 2.

If the number is odd, subtract 1.

Each operation counts as one step.
This process continues until the number becomes 0.
Essentially, every division by 2 removes one binary digit (bit shift), and every subtraction flips an odd number to even — making it a binary reduction problem.

---

# ⚙️ Approach

Initialize a counter steps = 0 to track the number of operations.

Loop while num > 0:

If num is even (num % 2 == 0), divide it by 2 using integer division (num //= 2).

If num is odd, subtract 1 (num -= 1).

Increment the step counter after each operation (steps += 1).

When num reaches 0, return the total count of steps.

---

# Process:

Step	Operation	New Value	Explanation
1	14 / 2	7	even → divide by 2
2	7 - 1	6	odd → subtract 1
3	6 / 2	3	even → divide by 2
4	3 - 1	2	odd → subtract 1
5	2 / 2	1	even → divide by 2
6	1 - 1	0	odd → subtract 1

✅ Total Steps: 6

---

# ⏱️ Complexity

Time Complexity: O(log n) — each division by 2 reduces the number exponentially.

Space Complexity: O(1) — only a few variables are used.

